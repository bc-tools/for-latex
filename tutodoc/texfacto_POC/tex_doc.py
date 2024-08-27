from .constants import *
from .misc      import *


# --------------------------- #
# -- BUILD SINGLE STY FILE -- #
# --------------------------- #

# TODO: pour contrib qui sera le lieu de la doc fbarictauio entenan compte du statut d'une trad
def build_single_tex(
    source,
    temp_dir,
    sorted_useful_files
):
    for onedir, srcfile, kind in iter_sorted_useful_files(
        source              = source,
        sorted_useful_files = sorted_useful_files,
        ext_wanted          = TAG_TEX
    ):
        if kind == TAG_FILE:
            print(f"   * Analyzing ''{srcfile.name}''")

        else:
            print(f"   * [RES-DOC]")
            print(f"       -> Copying ''{srcfile.relative_to(onedir)}"
                  f"/{srcfile.name}'")




def extractfrom_TEX(srcfile):
    with srcfile.open(
        encoding = "utf-8",
        mode = "r"
    ) as f:
        content = f.read()

    fordoc = []
    thedoc = []

    store_fordoc = "fordoc"
    store_thedoc = "thedoc"
    store_ignore = "ignore"
    store_in     = store_ignore

    for oneline in content.split('\n'):
        shortline = oneline.strip()

        if shortline == '% == FORDOC == %':
            store_in = store_fordoc
            continue

        if shortline == '\\begin{document}':
            store_in = store_thedoc
            continue

        if shortline == '\\end{document}':
            break

        if store_in == store_fordoc:
            fordoc.append(oneline)

        elif store_in == store_thedoc:
            thedoc.append(oneline)

    fordoc = '\n'.join(fordoc)
    fordoc = fordoc.strip()

    thedoc = '\n'.join(thedoc)
    thedoc = thedoc.strip()

    return fordoc, thedoc


def prepare_TEX(
    tmpdir,
    fordoc,
    thedoc
):
    if fordoc:
        fordoc += '\n'*3

        addcontentto(
            content  = fordoc,
            destfile = tmpdir / '.tmp_fordoc.tex'
        )

    if thedoc:
        thedoc += '\n'*3

        addcontentto(
            content  = thedoc,
            destfile = tmpdir / '.tmp_thedoc.tex'
        )
