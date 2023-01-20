import pandas as pd
import plotly.express as px
import pytask


@pytask.mark.depends_on("bld/auto_final.dta")
@pytask.mark.produces("bld/scatter.pdf")
def task_plot(depends_on, produces):
    # Input.
    data = pd.read_stata(depends_on)
    # Core task.
    graph = px.scatter(
        data_frame=data,
        x="weight",
        y="mpg",
        color="price",
        template="plotly_dark",
    )
    # Output.
    graph.write_image(produces)
