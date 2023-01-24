# Outline

- Think of task as a function
  - Takes files as inputs, writes out files as outputs
  - Initial example had exactly one of each
  - Now will look at multiple outputs


# [VS Code

- Remember task has two outputs, final result and log
- Just use dictionary, CAPITAL LETTERS to remind ourselves that it is a constant
- Type:

```python
PRODUCES = {
  "result": BLD / "optimization.pkl",
  "log": BLD / "optimization.db"
}


@pytask.mark.produces(PRODUCES)
def task_run_optimization(produces):
```

- Copy:

```python
    start_params = pd.DataFrame(1, index=["a", "b", "c"], columns=["value"])
    res = minimize(
        criterion=_sphere,
        params=start_params,
        algorithm="scipy_lbfgsb",
        logging=produces["log"],
    )
    pd.to_pickle(res, produces["result"])

def _sphere(params):
    return (params["value"] ** 2).sum()
```

- Run pytask

## [Show graph with duplication and combining two optimizers in a graph]

- Think of task as a function
- Call with different arguments now
- "parametrization"
- Start by re-writing our example,
  - then add second algorithm
  - then graph with both outputs

## [VS Code]

- Add 2x square brackets around `{"result" ...}` -- `[[{"result" ...}]]`
- Will need two iterables eventually:
  - One for the different parametrizations
  - One for different parameters (just having one `produces` argument is not special-cased)
- Change `@pytask.mark.produces(PRODUCES)` to `@pytask.mark.parametrize("produces", PRODUCES)`
- Run pytask
- Change `PRODUCES = ` to `PRODUCES_ALGO = `
- Add `"scipy_lbfgsb"` to inner list
- Change parametrization to `"produces, algo", PRODUCES_ALGO`
- Add `, algo` to task function arguments
- Replace `"scipy_lbfgsb"` by `algo`

## [Now second algorithm]

- change `PRODUCES_ALGO` to `PRODUCES_ALGOS`
- make list comprehension:

```
PRODUCES_ALGOS = [
    [
        {
            "result": BLD / algo / "parametrized" / "optimization.pkl",
            "log": BLD / algo / "parametrized" / "optimization.db",
        },
        algo,
    ]
    for algo in ["scipy_lbfgsb", "scipy_neldermead"]
]
```

- Run pytask
- Hard to know what 0, 1 is in complex projects

## [Now add IDs]

- Factor out `_ALGOS`
- `_ALGOS = ["scipy_lbfgsb", "scipy_neldermead"]`
- Change list comprehension
- Add `, ids=_ALGOS` to task function arguments
- Run pytask

## [Copy over task for plot]

```python
@pytask.mark.depends_on(pa[0]["log"] for pa in PRODUCES_ALGOS)
@pytask.mark.produces(BLD / "history_plot.png")
def task_plot_histories(depends_on, produces):
    to_concat = []
    for algo, path in depends_on.items():
        history = read_optimization_histories(path)["values"].to_frame(name="value")
        history["eval"] = np.arange(len(history))
        history["algorithm"] = algo
        to_concat.append(history)

    data = pd.concat(to_concat)

    fig = px.line(data, x="eval", y="value", color="algorithm", template="plotly_dark")
    fig.write_image(produces)
```

- No need to understand in detail
- Important bit: Re-use parts of targets of previous task

## [Full screen]

- Last examples might have been a bit fast, but have a look at repo
- Important take-aways:
- High level of abstraction for describing workflow
  - Just define dependencies, targets
  - Pytask will figure out the rest
- All the power of Python at your hands
- No need to learn new syntax, as with all other build tools
