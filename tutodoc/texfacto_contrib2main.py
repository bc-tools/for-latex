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

WHAT = "[CONTRIB. to MAIN]"


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

print(f"Dev lang : {metadata[TAG_MANUAL_DEV_LANG]}")
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
# -- USEFUL CONSTANTS -- #
# ---------------------- #

SRC_DIR = metadata[TAG_SRC]

CONTRIB_TRANS_DIR = metadata[TAG_PROJ_DIR] / TAG_CONTRIB / TAG_TRANSLATE

PROJECT_NAME = metadata[TAG_PROJ_NAME]


# ----------- #
# -- TOOLS -- #
# ----------- #

def iter_texspec_from_esv(file):
    for oneline in file.read_text().split('\n'):
        oneline = oneline.strip()

        if not oneline or oneline[:2] == '//':
            continue

        macroname, _, texcode = oneline.partition('=')

        macroname = macroname.strip()
        texcode   = texcode.strip()

        nbparams = 0

        for m in CMD_ARG_PATTERN.finditer(texcode):
            nbparams = max(nbparams, int(m.group(1)))

        yield nbparams, macroname, texcode


def build_trans_cmds(
    projname,
    file
):
    if not file.stem in ["macros", "sentences"]:
        return []

    macrodefs = []

    for nbparams, macroname, texcode in iter_texspec_from_esv(file):
        signature = "m"*nbparams
        macroname = macroname.replace('_', '@')
        # texcode   = texcode.replace(' ', ' ~ ')

        macrodefs.append(
            f"\\NewDocumentCommand{{\\{projname}@trans@{macroname}}}"
            f"{{{signature}}}{{{texcode}}}"
        )

    return macrodefs

def keepasdir(path):
    return (
        path.is_dir()
        and
        path.name[0] != "."
    )

# ------------------ #
# -- API CONTRIB. -- #
# ------------------ #

print_frame(
    PROJECT_NAME,
    "API - LANG ACCEPTED",
    WHAT
)

first_dir = True

for lang in  metadata[TAG_API_LANGS]:
    if first_dir:
        first_dir = False
    else:
        print()

    print(f"+ {lang}")

    lang_dir = CONTRIB_TRANS_DIR / lang / TAG_API

    for srcdir in lang_dir.glob("*"):
        if not keepasdir(srcdir):
            continue

        for ctxt in srcdir.glob("*"):
            if not keepasdir(ctxt):
                continue

            print(f'    * Translations from "/{srcdir.name}/{ctxt.name}".')


            sty_cfg  = SRC_DIR / srcdir.name
            sty_cfg /= f"{PROJECT_NAME}-{srcdir.name}-{ctxt.stem}-{lang}.cfg.cls.sty"


            texmacros = []

            for esvfile in ctxt.glob("*.txt"):
                texmacros += build_trans_cmds(PROJECT_NAME, esvfile)

            texmacros = "\n".join(texmacros)

            createfile(sty_cfg)
            sty_cfg.write_text(texmacros)
