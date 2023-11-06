from src2prod import *

from texfacto_POC import *

PROJECT_DIR = Path(__file__).parent
SOURCE_DIR  = PROJECT_DIR / Path('src')
TARGET_DIR  = PROJECT_DIR.parent / PROJECT_DIR.name.lower()

DEBUG = False
# DEBUG = True


# ----------------- #
# -- DEBUG TOOLS -- #
# ----------------- #

def debug_treeview(
    source,
    treeview,
):
    print(f"+ {source}")
    _recu_debug_treeview(
        treeview = treeview,
        depth = 1
    )

    if DEBUG:
        exit()


def _recu_debug_treeview(
    treeview,
    depth
):
    tab    = "  " * depth
    depth += 1

    for kind, content in treeview.items():
        if kind == TAG_FILE:
            for onefile in content:
                print(f"{tab}* {onefile.name}")

        else:
            for onedir, subtree in content.items():
                print(f"{tab}+ {onedir.name}")

                _recu_debug_treeview(
                    treeview = subtree,
                    depth    = depth
                )


# ----------------------- #
# -- ALL USEFULL FILES -- #
# ----------------------- #

treeview = build_tree(
    project = PROJECT_DIR,
    source  = Path('src'),
    target  = TARGET_DIR,
    readme  = Path('README.md'),
    ignore = """
test_*/
tests_*/
test_*.*
tests_*.*

tool_*/
tools_*/
tool_*.*
tools_*.*
"""
)


# --------------------------------- #
# -- IGNORE THE UNUSED PDF FILES -- #
# --------------------------------- #

for directdir, content in treeview[TAG_DIR].items():
    subfiles = content[TAG_FILE]

# We need to work on a copy of ''subfiles''.
    for directsubfile in subfiles[:]:
        if directsubfile.suffix == '.tex':
            pdf_unused = directsubfile.parent / f"{directsubfile.stem}.pdf"

            if pdf_unused in subfiles:
                subfiles.remove(pdf_unused)


# ------------------------------ #
# -- ONLY SOURCE FILES SORTED -- #
# ------------------------------ #

# debug_treeview(SOURCE_DIR, treeview)
# from pprint import pprint;pprint(treeview);exit()

for p in treeview[TAG_FILE]:
    if p.name == TAG_ABOUT_FILE:
        with p.open(
            encoding='utf8',
            mode='r',
        ) as f:
            about_cfg = safe_load(f)

        print(about_cfg)

# for k in treeview[TAG_DIR]:print(k.name)
exit()

allfiles_sorted = build_tree_sorted(
    source   = SOURCE_DIR,
    allfiles = treeview
)


# -------------------- #
# -- XXXXXX -- #
# -------------------- #

for f in treeview:
    if f.suffix == ".sty":
        print(f.name)
