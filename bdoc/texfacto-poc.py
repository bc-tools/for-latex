from src2prod import *

from texfacto import *

PROJECT_DIR = Path(__file__).parent
SOURCE_DIR  = PROJECT_DIR / Path('src')
TARGET_DIR  = PROJECT_DIR.parent / PROJECT_DIR.name.lower()


# ----------------------- #
# -- ALL USEFULL FILES -- #
# ----------------------- #

allfiles = buildlof(
    project = PROJECT_DIR,
    source  = Path('src'),
    target  = TARGET_DIR,
    readme  = Path('README.md'),
)


# ------------------------------ #
# -- ONLY SOURCE FILES SORTED -- #
# ------------------------------ #

allfiles_sorted = buildlof_sorted(
    source   = SOURCE_DIR,
    allfiles = allfiles
)


# -------------------- #
# -- XXXXXX -- #
# -------------------- #

for f in allfiles:
    if f.suffix == ".sty":
        print(f.name)
