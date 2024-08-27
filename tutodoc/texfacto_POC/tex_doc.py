from .constants import *
from .misc      import *


# --------------------------- #
# -- BUILD SINGLE STY FILE -- #
# --------------------------- #

def prebuild_single_tex(
    source,
    temp_dir,
    sorted_useful_files,
    dev_lang,
    other_lang,
    versions
):
    all_langs = [dev_lang] + other_lang

    contrib_dir = source.parent / TAG_CONTRIB / TAG_DOC / TAG_MANUAL

    for i, lang in enumerate(all_langs, 0):
        if i != 0:
            print()

        kind = "dev." if i == 0 else "contrib."

        print(f"## {kind.upper()} LANG ''{lang}'' ##")
        print()

        lang_dir      = contrib_dir / lang
        lang_temp_dir = temp_dir / lang

# Empty lang dir.
        emptydir(lang_temp_dir)

# Preamble file.
        print()
        print(f"+ [RES-TEX] Copying ''{lang}/preamble.cfg.tex''")

        copyfromto(
            srcfile  = lang_dir / "preamble.cfg.tex",
            destfile = lang_temp_dir / "preamble.cfg.tex"
        )

# Change log.
        print()
        print(f"+ Change log")

        chge_dir = lang_dir / TAG_CHGE_LOG
        content  = []

        for vers in versions[TAG_ALL]:
            print(
                f"    * {vers[TAG_YEAR]}-{vers[TAG_MONTH]}-{vers[TAG_DAY]}  "
                f"[{vers[TAG_NB]}]"
            )

            chge_file = (
                chge_dir / vers[TAG_YEAR] / f"{vers[TAG_MONTH]}-{vers[TAG_DAY]}.tex"
            )

            if not chge_file.is_file():
                raise IOError(
                    f"missing file.\n{chge_file.relative_to(lang_dir)}"
                )

            content = chge_file.read_text()

            print(content)

            match = re.search(LATEX_CONTENT_PATTERN, content)

            if match:
                content = match.group(1)

            else:
                raise IOError(f"illegal TEX file.\n{chge_file}")


        exit()

# Abstract.




        for onedir, srcfile, kind in iter_sorted_useful_files(
            source              = source,
            sorted_useful_files = sorted_useful_files,
            ext_wanted          = TAG_TEX,
            fake_src_name       = lang
        ):
            curdir  = lang_dir / onedir.name
            srcfile = curdir / srcfile.relative_to(onedir)

            if kind == TAG_FILE:
                print(f"   * Analyzing ''{srcfile.name}''")

                pieces = extract_from_TEX(srcfile)
                prepare_TEX(onedir, lang_temp_dir, *pieces)

            else:
                relpath = srcfile.relative_to(curdir)

                print(f"   * [RES-TEX] Copying ''{relpath}'")

                copyfromto(
                    srcfile  = srcfile,
                    destfile = lang_temp_dir / relpath
                )


def content_from_TEX(srcfile):
    ...


def extract_from_TEX(srcfile):
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
