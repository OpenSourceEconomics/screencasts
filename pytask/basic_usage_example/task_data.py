import pandas as pd
import pytask


@pytask.mark.depends_on("auto.dta")
@pytask.mark.produces("bld/auto_final.dta")
def task_prepare_data(depends_on, produces):
    # Input.
    raw_data = pd.read_stata(depends_on)
    # Core task.
    data = raw_data[["price", "mpg", "weight"]]
    # Output.
    data.to_stata(produces)
