from .constants import *
from .misc      import *


# --------------------------- #
# -- BUILD SINGLE STY FILE -- #
# --------------------------- #

# TODO: pour contrib qui sera le lieu de la doc fbarictauio entenan compte du statut d'une trad
def build_single_tex(
    source,
    temp_dir,
    sorted_useful_files,
    dev_lang,
    other_lang
):
    all_langs = [dev_lang] + other_lang

    contrib_dir = source.parent / TAG_CONTRIB / TAG_DOC / TAG_MANUAL

    for i, lang in enumerate(all_langs, 0):
        if i != 0:
            print()

        kind = "dev." if i == 0 else "contrib."

        print(f"-- {kind.upper()} LANG ''{lang}'' --")
        print()

        lang_dir      = contrib_dir / lang
        lang_temp_dir = temp_dir / lang

        emptydir(lang_temp_dir)

        for onedir, srcfile, kind in iter_sorted_useful_files(
            source              = source,
            sorted_useful_files = sorted_useful_files,
            ext_wanted          = TAG_TEX,
            extra_info          = lang
        ):
            srcfile       = lang_dir / onedir.name / srcfile.relative_to(onedir)

            if kind == TAG_FILE:
                print(f"   * Analyzing ''{srcfile.name}''")

                pieces = extractfrom_TEX(srcfile)
                prepare_TEX(onedir, lang_temp_dir, *pieces)

            else:
                print(f"   * [RES-TEX]")
                print(f"       -> Copying ''{srcfile.name}'")

                exit()

                destdir = tmpdir / relpath

                if not destdir.is_dir():
                    destdir.mkdir(parents = True)

                for srcfile in dircontent[TAG_FILE]:
                    copyfromto(srcfile, destdir / srcfile.name)

                    TOC_DOC_RESRCES.append(srcfile)

                copyfromto(
                    srcfile  = srcfile,
                    destfile = lang_temp_dir / srcfile.name
                )

        exit()


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
    _     ,  # factorization needs ths unused argument...
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
