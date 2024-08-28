DEBUG = False
# DEBUG = True


# ------------------- #
# -- PACKAGES USED -- #
# ------------------- #

from src2prod import *

from texfacto_builder import *

if DEBUG:
    from pprint import pprint


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_DIR = Path(__file__).parent


# ---------------------- #
# -- METADATA PROJECT -- #
# ---------------------- #

print_frame(
    THIS_DIR.name,
    "METADATA"
)

metadata = build_metadata(project_dir = THIS_DIR)

if DEBUG:
    print("# -- METADATA -- #")

    pprint(metadata)
    exit()

print(f"Manual - Dev lang : {metadata[TAG_MANUAL_DEV_LANG]}")
print()

# exit()


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


# ---------------------- #
# -- CONTRIB. FOLDERS -- #
# ---------------------- #

CONTRIB_DIR        = metadata[TAG_PROJ_DIR] / TAG_CONTRIB
CONTRIB_API_DIR    = CONTRIB_DIR / TAG_API / TAG_LOCALE
CONTRIB_MANUAL_DIR = CONTRIB_DIR / TAG_DOC / TAG_MANUAL


# ------------------ #
# -- API CONTRIB. -- #
# ------------------ #

print_frame(
    metadata[TAG_PROJ_NAME],
    "API, MAIN to CONTRIB."
)

glob_search = f"*/{TAG_LOCALE}/*"
first_lang  = False

for locale_dir in metadata[TAG_SRC].glob(glob_search):
    lang = locale_dir.name
    ctxt = list(
        locale_dir.relative_to(metadata[TAG_SRC]).parents
    )[1]

    if first_lang:
        first_lang = False
    else:
        print()

    print(f"+ Working in ''src/{locale_dir.relative_to(metadata[TAG_SRC])}''")

    this_contrib_dir = CONTRIB_API_DIR / lang / ctxt

    emptydir(
        folder  = this_contrib_dir,
        rel_dir = CONTRIB_DIR
    )

    for locale_file in locale_dir.glob("*"):
        if (
            not locale_file.is_file()
            or
            locale_file.name[0] == "."
        ):
            continue

        copyfromto(locale_file, this_contrib_dir / locale_file.name)

    print(f"+ Update done.")


# ------------------ #
# -- DOC CONTRIB. -- #
# ------------------ #

print_frame(
    metadata[TAG_PROJ_NAME],
    "DOC, MAIN to CONTRIB."
)
