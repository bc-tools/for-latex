DEBUG = False
# DEBUG = True


# ------------------- #
# -- PACKAGES USED -- #
# ------------------- #

from src2prod import *

from texfacto_POC import *

if DEBUG:
    from pprint import pprint


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_DIR = Path(__file__).parent


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


# ---------------------- #
# -- METADATA PROJECT -- #
# ---------------------- #

print_frame(
    THIS_DIR.name,
    "METADATA"
)

metadata = build_metadata(project_dir = THIS_DIR)

print(f"""
Author           : {metadata[TAG_AUTHOR]}
Creation         : {str_date(metadata[TAG_CREATION][TAG_DATE])}
Last version     : {str_date(metadata[TAG_LAST_VERSION][TAG_DATE])} [{metadata[TAG_LAST_VERSION][TAG_VERSION]}]
Short desc.      : {metadata[TAG_DESC]}

Manual
  - Dev lang  : {metadata[TAG_MANUAL_DEV_LANG]}
  - Other lang: {', '.join(metadata[TAG_MANUAL_OTHER_LANG]) if metadata[TAG_MANUAL_OTHER_LANG] else 'none'}

... etc.
""".lstrip())

# exit()

if DEBUG:
    print("# -- METADATA -- #")

    pprint(metadata)
    exit()


# ----------------------- #
# -- ALL USEFULL FILES -- #
# ----------------------- #

treeview = build_tree(
    project = metadata[TAG_PROJ_DIR],
    source  = metadata[TAG_SRC],
    target  = metadata[TAG_ROLLOUT],
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
    debug_treeview(metadata[TAG_SRC], treeview)

    # exit()


# ----------------------- #
# -- SORTED MAIN FILES -- #
# ----------------------- #

print_frame(
    metadata[TAG_PROJ_NAME],
    "SORTED MAIN FILES",
    "(no resources printed)"
)

sorted_useful_files = files_2_analyze(
    source   = metadata[TAG_SRC],
    treeview = treeview
)

if DEBUG:
    for onedir, sorted2analyze in sorted_useful_files.items():
        print()
        print()
        print(f"+ {onedir}")
        print()
        pprint(sorted2analyze)

    # exit()


# --------------------------- #
# -- TEMP. VERSION - START -- #
# --------------------------- #

print_frame(
    metadata[TAG_PROJ_NAME],
    "TEMP. VERSION",
    "(start)"
)

emptydir(metadata[TAG_TEMP])


# ----------------------------------------- #
# -- TEMP. VERSION - PRE STY & TEX FILES -- #
# ----------------------------------------- #

for kind, builder in [
    ("STY", build_single_sty),
    ("TEX", build_single_tex),
]:
    print_frame(
        metadata[TAG_PROJ_NAME],
        f"SINGLE {kind} FILE",
        "(temp. version)"
    )

    builder(
        source              = metadata[TAG_SRC],
        temp_dir            = metadata[TAG_TEMP],
        sorted_useful_files = sorted_useful_files,
        dev_lang            = metadata[TAG_MANUAL_DEV_LANG],
        other_lang          = metadata[TAG_MANUAL_OTHER_LANG],
    )


# ------------------------- #
# -- TEMP. VERSION - END -- #
# ------------------------- #

print_frame(
    metadata[TAG_PROJ_NAME],
    "TEMP. VERSION",
    "(finished)"
)
