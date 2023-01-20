import pandas as pd
import pytask
import estimagic as em

from config import BLD

ALGOS = ["scipy_lbfgsb", "scipy_neldermead"]


for algo in ALGOS:
    product = BLD / algo / "optimization.pkl"
    @pytask.mark.task
    def task_run_optimization(produces=product, algo=algo):
        res = em.minimize(
            criterion=_sphere,
            params=pd.Series({"a": 1, "b": 2, "c": 3}),
            algorithm=algo,
        )
        pd.to_pickle(res, produces)


def _sphere(params):
    return (params ** 2).sum()


DEPENDENCIES = {algo: BLD / algo / "optimization.pkl" for algo in ALGOS}

@pytask.mark.depends_on(DEPENDENCIES)
@pytask.mark.produces(BLD / "history_plot.png")
def task_plot_histories(depends_on, produces):
    results = {name: pd.read_pickle(path) for name, path in depends_on.items()}
    fig = em.criterion_plot(results, max_evaluations=100)
    fig.write_image(produces)
