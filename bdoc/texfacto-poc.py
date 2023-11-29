import re

from src2prod import *

from texfacto_POC import *

PROJECT_DIR = Path(__file__).parent
SOURCE_DIR  = PROJECT_DIR / 'src'
ROLLOUT_DIR = PROJECT_DIR / "rollout"

PATTERNS = [
    re.compile(r"^([^%\\]*)(.*)(\\" + macroname + ")(\[.*\][\t ]*\n?[\t ]*)?{(.*)}(.*)$")
    for macroname in [
        'input',
        'bdoclatexshow',
        'bdoclatexinput',
        'bdocshowcaseinput',
    ]
]
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
    target  = ROLLOUT_DIR,
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

# debug_treeview(SOURCE_DIR, treeview);exit()
# from pprint import pprint;pprint(list(treeview[TAG_DIR].keys()));exit()

tmpdir = build_tmp_proj(
    source   = SOURCE_DIR,
    treeview = treeview
)

tmpdir = Path("/Users/projetmbc/Mon Drive/git[NEW]-G-Drive/coding/bc-tools/for-latex/bdoc/.bdoc")

build_rollout_proj(
    patterns   = PATTERNS,
    tmpdir     = tmpdir,
    rolloutdir = ROLLOUT_DIR,
)
