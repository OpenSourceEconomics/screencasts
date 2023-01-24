## [Example in background, face big]

- Welcome
- Will show how to use some more complex features of pytask
- Again will be using a minimal example
  - Actually simpler in some ways than that in the earlier screencasts
  - Initially, just a single task

## Outline

- Complex projects
  - will be distributed across multiple files and directories
  - Need way to import stuff
  - Standard Python package imports, but not everyone will be familiar with them

## [Full screen picture with initial example]

- Distributed across multiple directories
- Example from our friends over at estimagic
  - Benchmark optimizers
  - No input
  - Two files as outputs — database with logs, pickle file with results

# [VS Code, directory tree / config.py ]

- Define variables SRC and BLD in central config.py file.
- In main directory, type `pip install -e .`
- In config file, define often-used variables, very often paths
- CAPITAL LETTERS to remind ourselves these are constants
- Python's Pathlib module is very handy here

# [VS Code ]

- [start with 3 imports]
- Type: `from config import BLD`
- Remember task has output with final result
- use CAPITAL LETTERS to remind ourselves that it is a constant
- Type:

```python
PRODUCES = BLD / "optimization.pkl"


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

# Important take-aways:

- High level of abstraction for describing workflow
  - Just define dependencies, targets
  - Pytask will figure out the rest
- All the power of Python at your hands
- No need to learn new syntax, as with all other build tools
