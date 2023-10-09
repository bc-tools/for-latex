from src2prod import *

from texfacto import *

PROJECT_DIR = Path(__file__).parent
SOURCE_DIR  = PROJECT_DIR / Path('src')
TARGET_DIR  = PROJECT_DIR.parent / PROJECT_DIR.name.lower()


# ----------------------- #
# -- ALL USEFULL FILES -- #
# ----------------------- #

allfiles = build_tree(
    project = PROJECT_DIR,
    source  = Path('src'),
    target  = TARGET_DIR,
    readme  = Path('README.md'),
)


# ----------------------------------- #
# -- LET'S REMOVE UNUSED PDF FILES -- #
# ----------------------------------- #

for directdir, content in allfiles[TAG_DIR].items():
    subfiles = content[TAG_FILE]

    for directsubfile in subfiles:
        if directsubfile.suffix == '.tex':
            pdf_unused = directsubfile.parent / f"{directsubfile.stem}.pdf"

            if pdf_unused in subfiles:
                subfiles.remove(pdf_unused)


# ------------------------------ #
# -- ONLY SOURCE FILES SORTED -- #
# ------------------------------ #

from pprint import pprint;pprint(allfiles)
exit()

allfiles_sorted = build_tree_sorted(
    source   = SOURCE_DIR,
    allfiles = allfiles
)


# -------------------- #
# -- XXXXXX -- #
# -------------------- #

for f in allfiles:
    if f.suffix == ".sty":
        print(f.name)
