import pytask
import pytask_markdown.compilation_steps as cs
import pathlib

pt = pathlib.Path("pytask")

@pytask.mark.markdown(
    script=pt.joinpath("1-motivation-overview", "screencast.md"),
    document=pt.joinpath("1-motivation-overview", "screencast.html"),
    css=pathlib.Path("custom.scss"),
    compilation_steps=cs.marp(options=["--html", "--allow-local-files"]),
)
def task_render_presentation():
    pass
