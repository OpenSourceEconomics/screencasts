import pandas as pd
import pytask
from estimagic import minimize

from config import BLD


@pytask.mark.produces(BLD / "optimization.pkl")
def task_run_optimization(produces):
    res = minimize(
        criterion=_sphere,
        params=pd.Series({"a": 1, "b": 2, "c": 3}),
        algorithm="scipy_lbfgsb",
    )
    pd.to_pickle(res, produces)


def _sphere(params):
    return (params ** 2).sum()
