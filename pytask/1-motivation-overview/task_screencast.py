from pathlib import Path

import pytask

from config import OUT
from config import plain_pandoc
from config import revealjs_pandoc
from config import SRC

this_dir = Path(__file__).parent.parent


names = ["setting-up-a-project", "project-layouts", "pytask-nifty-features"]


@pytask.mark.parametrize(
    "depends_on, produces",
    [
        (
            [
                f"{n}-screencast.md",
                SRC / "classes" / "resources" / "revealjs" / "template-revealjs.html",
            ],
            OUT / this_dir.name / f"{n}-revealjs.html",
        )
        for n in names
        if (Path(__file__).parent / f"{n}-screencast.md").is_file()
    ],
)
def task_convert_revealjs(depends_on, produces):
    return revealjs_pandoc(depends_on, produces)


@pytask.mark.parametrize(
    "depends_on, produces",
    [
        (
            f"{n}-{typ}.md",
            d / this_dir.name / f"{n}-{typ}.html",
        )
        for n in names
        for typ, d in (("script", OUT), ("screencast", OUT))
        if (Path(__file__).parent / f"{n}-{typ}.md").is_file()
    ],
)
def task_convert_plain(depends_on, produces):
    return plain_pandoc(depends_on, produces)
