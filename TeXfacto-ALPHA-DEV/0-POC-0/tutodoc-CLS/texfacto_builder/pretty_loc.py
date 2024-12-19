from collections import defaultdict

from .constants import *
from .misc      import *


# --------------------------- #
# -- END IS COMING SOON... -- #
# --------------------------- #

def prettyloc(
    metadata,
):
    projname = metadata[TAG_PROJ_NAME]

    code_dir = metadata[TAG_ROLLOUT] / "code"

    for p in code_dir.glob("*-locale-*.cfg.*"):
        _ , _ , lang  = p.name.partition("-locale-")
        lang, _ , _ , = lang.partition(".cfg.")

        newpath = p.parent / f"{projname}-{lang}.loc.cls"

        copyfromto(
            srcfile  = p,
            destfile = newpath
        )

        p.unlink()


    projfile = code_dir / f"{projname}.cls"

    projcode = projfile.read_text()

    for old, new in [
        (
            r"{tutodoc-main-locale-\tdoclang.cfg.cls.sty}",
            r"{tutodoc-\tdoclang.loc.cls}",
        ),
        (
            "{tutodoc-main-locale-en.cfg.cls.sty}",
            "{tutodoc-en.loc.cls}",
        ),
    ]:
        projcode = projcode.replace(old, new)

    projfile.write_text(projcode)
