DEBUG = False
DEBUG = True


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

HOOK_DIR = THIS_DIR / "hook"


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


# ------------ #
# -- HOOKS? -- #
# ------------ #

MANUAL_HOOKS = {
    TAG_PRE : {},
    TAG_POST: {}
}


if HOOK_DIR.is_dir():
# Auto update the __init__ for our use.
    initcode = [
        r"""
# This file has been updated automatically by TeXfacto.
        """.strip()
    ]

    tmpl_init = r"""
from .{hookname} import (
    PRE_HOOK  as PRE_HOOK_{hookname},
    POST_HOOK as POST_HOOK_{hookname}
)
    """.strip()

    for pyfile in HOOK_DIR.glob("*.py"):
        hookname = pyfile.stem

        if hookname == "__init__":
            continue

        initcode.append(
            tmpl_init.format(hookname = hookname)
        )

    initcode = "\n\n".join(initcode)

    (HOOK_DIR / "__init__.py").write_text(initcode)

    import hook

    __globals_hook = globals()["hook"]

    for hookdict_name in dir(hook):
        if (
            hookdict_name.startswith('__')
            or
            not (
                hookdict_name.startswith('PRE_HOOK_')
                or
                hookdict_name.startswith('POST_HOOK_')
            )
        ):
            continue

        KIND = (
            TAG_PRE
            if hookdict_name.startswith('PRE_HOOK_') else
            TAG_POST
        )

        MANUAL_HOOKS[KIND].update(
            getattr(
                __globals_hook,
                hookdict_name
            )
        )

# from pprint import pprint;pprint(MANUAL_HOOKS);exit()


# ---------------------- #
# -- METADATA PROJECT -- #
# ---------------------- #

assert THIS_DIR.name != ""

print_frame(
    THIS_DIR.name,
    "METADATA"
)

metadata = build_metadata(project_dir = THIS_DIR)

# if DEBUG:
#     print("# -- METADATA -- #")

#     pprint(metadata)
#     exit()

print(f"""
Author       : {metadata[TAG_AUTHOR]}
Short desc.  : {metadata[TAG_DESC]}

Last version : {nb_date_EN(metadata[TAG_VERSIONS][TAG_LAST])}  [{metadata[TAG_VERSIONS][TAG_LAST][TAG_NB]}]
Creation     : {nb_date_EN(metadata[TAG_CREATION])}  [{metadata[TAG_CREATION][TAG_NB]}]

Manual
  - Dev lang   : {metadata[TAG_MANUAL_DEV_LANG]}
  - Other lang : {', '.join(metadata[TAG_MANUAL_OTHER_LANG]) if metadata[TAG_MANUAL_OTHER_LANG] else 'none'}

... etc.
""".lstrip())

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
debug-*

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


# if DEBUG:
#     print("# -- TREVIEW FULL -- #")
#     debug_treeview(metadata, treeview)

#     exit()

#     print("# -- TREVIEW -- #")
#     debug_treeview(metadata[TAG_SRC], treeview)

#     exit()


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

# if DEBUG:
#     for onedir, sorted2analyze in sorted_useful_files.items():
#         print()
#         print()
#         print(f"+ {onedir}")
#         print()
#         pprint(sorted2analyze)

#         input("next?")

#     exit()


# --------------------------- #
# -- TEMP. VERSION - START -- #
# --------------------------- #

print_frame(
    metadata[TAG_PROJ_NAME],
    "TEMP. VERSION",
    "(start)"
)

emptydir(
    folder  = metadata[TAG_TEMP],
    rel_dir = metadata[TAG_PROJ_DIR]
)



# ----------------------------------------- #
# -- TEMP. VERSION - PRE STY & TEX FILES -- #
# ----------------------------------------- #

for kind, prebuilder, hooks in [
    (TAG_CLS, prebuild_single_cls, {}),
    (TAG_STY, prebuild_single_sty, {}),
    (TAG_TEX, prebuild_single_tex, MANUAL_HOOKS,),
]:
    print_frame(
        metadata[TAG_PROJ_NAME],
        f"SINGLE {kind.upper()} FILE",
        "(temp. version)"
    )

    prebuilder(
        projname            = metadata[TAG_PROJ_NAME],
        source              = metadata[TAG_SRC],
        temp_dir            = metadata[TAG_TEMP],
        sorted_useful_files = sorted_useful_files,
        versions            = metadata[TAG_VERSIONS],
        hooks               = hooks,
        about_langs         = {
            TAG_MANUAL_DEV_LANG  : metadata[TAG_MANUAL_DEV_LANG],
            TAG_MANUAL_OTHER_LANG: metadata[TAG_MANUAL_OTHER_LANG],
            TAG_API_LANGS        : metadata[TAG_API_LANGS],
        },
    )


# if DEBUG:
#     exit()


# --------------- #
# -- CSS FILES -- #
# --------------- #

for srcfile in metadata[TAG_SRC].glob("*/css/*.sty"):
    catego = srcfile.parent.parent.name

    kind = srcfile.name

    for ext in [TAG_STY, TAG_CLS]:
        ext = f".{ext}"

        if kind.endswith(ext):
            kind = kind[:-len(ext)]

        else:
            break

    tmp_css_path = ROLLOUT_CSS_PATH.format(
        projname = metadata[TAG_PROJ_NAME],
        texvar   = kind,
        catego   = catego
    )

    destfile = metadata[TAG_TEMP] / tmp_css_path

    copyfromto(
        srcfile  = srcfile,
        destfile = destfile,
    )


# ------------------- #
# -- FINAL PRODUCT -- #
# ------------------- #

print_frame(
    metadata[TAG_PROJ_NAME],
    "FINAL PRODUCT",
)

def ugly_hack(content):
    for old, new in [
        (
            "{examples/listing-latex/xyz.tex}",
            "{examples-listing-latex-xyz.tex}",
        ),
        (
            "examples/showcase/external.tex",
            "examples-showcase-external.tex",
        ),
        (
            "{../main/tutodoc-main-locale",
            "{tutodoc-main-locale",
        ),
        (
            "examples/listing-full/hello-you.tex",
            "examples-listing-full-hello-you.tex",
        ),
    ]:
        content = content.replace(old, new)

    return content

finalize(
    metadata  = metadata,
    ugly_hack = ugly_hack,
)


# ---------------- #
# -- MINIFY CSS -- #
# ---------------- #

minicss(
    metadata  = metadata,
)


# ------------------------- #
# -- PRETTY LOCALE ORGA. -- #
# ------------------------- #

prettyloc(
    metadata  = metadata,
)


# ------------------------------------- #
# -- USER'S ''l3build.lua'' - UPDATE -- #
# ------------------------------------- #

print_frame(
    metadata[TAG_PROJ_NAME],
    "USER'S ''l3build.lua''",
    "UPDATE"
)

l3build_file = metadata[TAG_ROLLOUT] / "build.lua"

l3build_content  = []
look_for_version = False

for line in l3build_file.read_text().split('\n'):
    short_line = line.strip()

    if short_line.startswith("uploadconfig"):
        look_for_version = True

    elif look_for_version:
        if short_line.startswith("version"):
            before, _ , _ = line.partition("=")
            last_version  = metadata[TAG_VERSIONS][TAG_LAST]

            lv_nb    = last_version[TAG_NB]
            lv_year  = last_version[TAG_YEAR]
            lv_month = last_version[TAG_MONTH]
            lv_day   = last_version[TAG_DAY]

            line = f'{before}= "{lv_nb} [{lv_year}-{lv_month}-{lv_day}]",'

    l3build_content.append(line)

l3build_content = '\n'.join(l3build_content)

l3build_file.write_text(l3build_content)

print("+ DON'T FORGET TO DESCRIBE THE LAST VERSION!")
print()
print(f"  --> {l3build_file}")
