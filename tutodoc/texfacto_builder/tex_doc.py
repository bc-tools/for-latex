import babel

from .constants import *
from .misc      import *


# ----------- #
# -- HOOKS -- #
# ----------- #

def call_hook(
    lang_temp_dir,
    srcfile,
    hookfunc
):
    lang_temp_srcfile_indoc = lang_temp_dir / TAG_TMP_SRCFILE_INDOC
    lang_temp_doc           = lang_temp_dir / TAG_TMP_TEX_THE_DOC

    virtual_resrc, tex_code = hookfunc(srcfile.parent)

    with lang_temp_srcfile_indoc.open(
        mode = 'a',
    ) as temp_file:
        for vpath, tcode in virtual_resrc.items():
            tcode = tcode.replace(
                r"\input{../preamble.cfg.tex}" + "\n"*2,
                ""
            )

            temp_file.write(
                TMPL_FILE_CONTENTS.format(
                    virtual_path = vpath,
                    tex_code     = tcode
                ) + '\n'*2
            )

    with lang_temp_doc.open(
        mode = 'a',
    ) as temp_file:
        temp_file.write(tex_code + '\n'*2)


# ------------ #
# -- LOCALE -- #
# ------------ #

def lang_long_name_in(
    shortname,
    curlang
):
    return babel.Locale.parse(shortname).get_display_name(curlang)


# --------------------------- #
# -- BUILD SINGLE STY FILE -- #
# --------------------------- #

def prebuild_single_tex(
    projname,
    source,
    temp_dir,
    sorted_useful_files,
    versions,
    hooks,
    about_langs,
):
    manual_langs  = about_langs[TAG_MANUAL_OTHER_LANG] \
                  + [about_langs[TAG_MANUAL_DEV_LANG]]
    translate_dir = source.parent / TAG_CONTRIB / TAG_TRANSLATE

# English abstract.
    if not TAG_LANG_EN in manual_langs:
        print(f"+ Abstract: no English!")

    else:
        print(f"+ Abstract: English version.")

        abstract_EN = abstract_of(
            lang          = TAG_LANG_EN,
            translate_dir = translate_dir
        )

        abstract_EN = "\n    ".join(
            abstract_EN.split("\n")
        )

        abstract_EN = other_manual_langs(
            content      = abstract_EN,
            lang         = TAG_LANG_EN,
            manual_langs = manual_langs
        )

# Let's work lang by lang.
    for i, lang in enumerate(manual_langs, 0):
        print()

        kind = "dev." if i == 0 else "contrib."

        print(f"## {kind.upper()} LANG ''{lang}'' ##")
        print()

        lang_dir_manual = translate_dir / lang / TAG_DOC / TAG_MANUAL

        lang_temp_dir           = temp_dir / lang
        lang_temp_file_contents = lang_temp_dir / ".tmp_file_contents.tex"

# Empty lang dir + add temp. file for source contents.
        emptydir(
            folder  = lang_temp_dir,
            rel_dir = source.parent
        )

        lang_temp_file_contents.touch()

# Preamble file.
        print()
        print(f"+ [RES-TEX] Copying ''{TAG_TMP_PREAMBLE}''")

        copyfromto(
            srcfile  = lang_dir_manual / TAG_TMP_PREAMBLE,
            destfile = lang_temp_dir / TAG_TMP_PREAMBLE
        )

# Change log.
        print()
        print(f"+ Change log")

        chge_dir = lang_dir_manual / TAG_CHGE_LOG
        content  = []

        last_chges_explained = ""

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
                    # f"missing file.\n{chge_file}"
                    f"missing file.\n{chge_file.relative_to(translate_dir)}"
                )

            about_this_change = content_from_TEX(chge_file)

            if not last_chges_explained:
                last_chges_explained = about_this_change

            content.append(
                version_date_changes(vers, about_this_change)
            )

        content = "\n\n\\tdocsep\n\n\n% ------------------ %\n\n\n".join(content)
        content = content.strip()

        chge_file = lang_temp_dir / f"{TAG_CHGE_LOG}.tex"
        chge_file.write_text(content)

# Abstract.
        abstract = content_from_TEX(
            srcfile = lang_dir_manual / TAG_ABSTRACT / f"{TAG_ABSTRACT}.tex"
        )

        if lang != TAG_LANG_EN:
            abstract = abstract.replace(
                "\\end{abstract}",
                f"""
    \\tdocsep

    {{\\small\\itshape
        \\vspace{{-5pt}}
        \\begin{{center}}
            \\textbf{{Abstract.}}
        \\end{{center}}

        {abstract_EN}
    }}
\\end{{abstract}}
                """.rstrip()
            )

        abstract = other_manual_langs(
            content   = abstract,
            lang      = lang,
            manual_langs = manual_langs
        )

        abstract += f"""

\\medskip

\\begin{{center}}
\\small
\\begin{{minipage}}{{.9\\textwidth}}
\\begin{{tdocnote}}[{LAST_CHGES_IN[lang]}]
{last_chges_explained}
\\end{{tdocnote}}
\\end{{minipage}}
\\end{{center}}
        """.rstrip()

        abstract_file = lang_temp_dir / f"{TAG_ABSTRACT}.tex"
        abstract_file.write_text(abstract)

# Manual.
        print()

        for onedir, srcfile, kind in iter_sorted_useful_files(
            source              = source,
            sorted_useful_files = sorted_useful_files,
            ext_wanted          = TAG_TEX,
            fake_src_name       = lang
        ):
            curdir  = lang_dir_manual / onedir.name
            srcfile = curdir / srcfile.relative_to(onedir)

            if kind == TAG_FILE:
                print(f"   * Analyzing ''{srcfile.name}''")

                hook_ref = f"{srcfile.parent.name}/{srcfile.name}"

# A prehook ?
                if hook_ref in hooks[TAG_PRE]:
                    PRE_HOOKS_NOT_DONE

# WARNING!
# No magic comment inside the manual of the dev contrib.
                thedoc = srcfile.read_text()

                _     , _, thedoc = thedoc.partition("\\input{../preamble.cfg.tex}")
                fordoc, _, thedoc = thedoc.partition("\\begin{document}")
                thedoc, _, _      = thedoc.partition("\\end{document}")

                fordoc = fordoc.strip()
                thedoc = thedoc.strip()

                api_lang_items = '\n        \\item '.join(
                    f"\\tdocinlatex|{l}| : {lang_long_name_in(l, lang)}."
                    for l in sorted(about_langs[TAG_API_LANGS])
                )

                thedoc = thedoc.replace(
                    """
% Do not touch the following placeholder.
<<API-LANGS>>
                    """.strip(),
                    f"""
\\begin{{tasks}}[label=\\small\\textbullet](3)
    \\task {api_lang_items}
\\end{{tasks}}
                    """
                )

                pieces = extract_from_DEV_TEX(srcfile)
                prepare_TEX(onedir, lang_temp_dir, fordoc, thedoc)

# A posthook ?
                if hook_ref in hooks[TAG_POST]:
                    print(f"   * POST HOOK for ''{srcfile.name}''")

                    call_hook(
                        lang_temp_dir = lang_temp_dir,
                        srcfile       = srcfile,
                        hookfunc      = hooks[TAG_POST][hook_ref]
                    )

            else:
                relpath = srcfile.relative_to(curdir)

                print(f"   * [RES-TEX] Copying ''{relpath}'")

                copyfromto(
                    srcfile  = srcfile,
                    destfile = lang_temp_dir / relpath
                )


def version_date_changes(about_vers, about_changes):
    finalcontent = []
    dateadded    = False

    for i, line in enumerate(about_changes.split("\n")):
        if not dateadded:
            shortline = line.strip()

            if i == 0 and shortline == r"\small":
                continue

            if not shortline and not finalcontent:
                continue

            if shortline.startswith("\\tdocstartproj{"):
                dateadded = True

                line = f"""
\\tdocversion{{{about_vers[TAG_NB]}}}[{nb_date_EN(about_vers)}]
{line}
                """.strip()

            else:
                for pattern in BEGIN_WHAT_ENV_PATTERNS:
                    m = pattern.match(line.strip())

                    if m:
                        dateadded = True

                        line += (
                            f"[version = {about_vers[TAG_NB]}, "
                            f"date = {nb_date_EN(about_vers)}]"
                        )

        finalcontent.append(line)


    finalcontent = "\n".join(finalcontent)

    return finalcontent


def content_from_TEX(
    srcfile,
    start_block = "\\begin{document}",
    end_block   = "\\end{document}"
):
    content  = []
    store_in = False

    for oneline in srcfile.read_text().split('\n'):
        shortline = oneline.strip()

        if shortline == start_block:
            store_in = True
            continue

        if shortline == end_block:
            break

        if store_in:
            content.append(oneline)


    content = "\n".join(content)
    content = content.strip()

    return content


def extract_from_DEV_TEX(srcfile):
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

        if shortline == TAG_MC_FORDOC:
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
    fordoc_file = tmpdir / '.tmp_fordoc.tex'
    thedoc_file = tmpdir / '.tmp_thedoc.tex'

    createfile(fordoc_file)
    createfile(thedoc_file)

    if fordoc:
        fordoc += '\n'*3

        addcontentto(
            content  = fordoc,
            destfile = fordoc_file
        )

    if thedoc:
        thedoc += '\n'*3

        addcontentto(
            content  = thedoc,
            destfile = thedoc_file
        )



def other_manual_langs(
    content,
    lang,
    manual_langs,
):
    others = [
        lang_long_name_in(l, lang)
        for l in manual_langs
        if l != lang
    ]

    content = content.replace(
        "<<DOC-LANGS>>",
        ", ".join(others)
    )

    return content


def abstract_of(
    lang,
    translate_dir
):
    abstract_file = translate_dir / lang /  TAG_DOC / TAG_MANUAL / TAG_ABSTRACT / f"{TAG_ABSTRACT}.tex"

    if not abstract_file.is_file():
        raise IOError(f"missing file.\n{abstract_file}")

    return content_from_TEX(
        srcfile     = abstract_file,
        start_block = f"\\begin{{{TAG_ABSTRACT}}}",
        end_block   = f"\\end{{{TAG_ABSTRACT}}}"
    )
