DEBUG = False
# DEBUG = True


import re

from src2prod import *

from texfacto_NEW_POC import *


# --------------- #
# -- CONSTANTS -- #
# --------------- #

PROJECT_DIR = Path(__file__).parent
SOURCE_DIR  = PROJECT_DIR / 'src'
ROLLOUT_DIR = PROJECT_DIR / "rollout"
MANUALS_DIR = PROJECT_DIR / "contrib" / "doc" / "manual"


PROJECT_NAME = SOURCE_DIR.parent.name


CMDS_FOR_FILE_PATTERNS = [
    re.compile(r"^([^%\\]*)(.*)(\\" + macroname + ")(\[.*\][\t ]*\n?[\t ]*)?{(.*)}(.*)$")
    for macroname in [
        'input',
        'tdoclatexshow',
        'tdoclatexinput',
        'tdocshowcaseinput',
        'tdocdocbasicinput',
    ]
]


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

for directdir, content in treeview[TAG_DIR].items():
    subfiles = content[TAG_FILE]

# We need to work on a copy of ''subfiles''.
    for directsubfile in subfiles[:]:
        if directsubfile.suffix == '.tex':
            pdf_unused = directsubfile.parent / f"{directsubfile.stem}.pdf"

            if pdf_unused in subfiles:
                subfiles.remove(pdf_unused)


if DEBUG:
    print("# -- TREVIEW -- #")
    debug_treeview(SOURCE_DIR, treeview)


# ---------------- #
# -- MAIN FILES -- #
# ---------------- #

print_frame(PROJECT_NAME, "MAIN FILES (without resources)")

sorted_useful_files = files_2_analyze(
    source   = SOURCE_DIR,
    treeview = treeview
)


# ---------------------------------------------- #
# -- XXXXX -- #
# ---------------------------------------------- #


# ---------------------------------------------- #
# -- XXXXX -- #
# ---------------------------------------------- #
