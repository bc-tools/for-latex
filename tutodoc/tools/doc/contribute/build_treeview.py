from pathlib import Path


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_PROJ_NAME = "tutodoc"

THIS_DIR = Path(__file__).parent

PROJ_DIR = THIS_DIR

while(PROJ_DIR.name != THIS_PROJ_NAME):
    PROJ_DIR = PROJ_DIR.parent

DOC_SRC_DIR   = PROJ_DIR / "src" / "how-to-contribute"
TRANSLATE_DIR = PROJ_DIR / "contrib" / "translate"


# -------------------------------------- #
# -- XXX -- #
# -------------------------------------- #


# -------------------------------------- #
# -- XXX -- #
# -------------------------------------- #
