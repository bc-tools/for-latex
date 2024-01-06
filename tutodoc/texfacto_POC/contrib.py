from .gather import *


def contrib_tex_template(text, localtools = ""):
    if localtools:
        localtools = f"""
% == FORDOC == %

{localtools}
"""


    return f"""
\\documentclass[12pt, a4paper]{{article}}

\\input{{../preamble.cfg.tex}}

{localtools}
\\begin{{document}}

{text}

\\end{{document}}
    """.lstrip()


def clean_main_tex(texfile):
    content     = texfile.read_text()
    new_content = []
    localtools  = []

    kind = ""

    for oneline in content.split('\n'):
        if kind == 'content':
            new_content.append(oneline)

        elif kind == 'tools':
            localtools.append(oneline)

        elif oneline.strip() == '\\begin{document}':
            kind = 'content'

        elif oneline.strip() == '% == FORDOC == %':
            kind = 'tools'

    new_content = '\n'.join(new_content)
    localtools  = '\n'.join(localtools)

    texfile.write_text(
        data = contrib_tex_template(
            text       = new_content,
            localtools = localtools
        )
    )


def update_contrib(
    projdir,
    toc_doc,
    toc_doc_resrces,
    main_lang = 'fr'
):
    contribdir = projdir / "contrib" / "doc" / "manual"
    srcdir     = projdir / "src"

# Update main doc.
    maindoc = contribdir / main_lang

    emptydir(maindoc)

    preambule = maindoc / "preamble.cfg.tex"

    copyfromto(
        srcdir  / "preamble.cfg.tex",
        preambule
    )

    preambule.write_text(
        data = f"""{preambule.read_text()}
\\usepackage[lang = french]{{tutodoc}}
"""
    )

    for docfile in toc_doc:
        copyfromto(
            srcdir  / docfile,
            maindoc / docfile
        )

        clean_main_tex(maindoc / docfile)


    copyfromto(
        srcdir  / "abstract" / "abstract.tex",
        maindoc / "abstract" / "abstract.tex"
    )

    clean_main_tex(maindoc / "abstract" / "abstract.tex")


    for resfile in toc_doc_resrces:
        copyfromto(
            resfile,
            maindoc / resfile.relative_to(srcdir)
        )


    for logfile in (srcdir / "changelog").glob("*/*/*.tex"):
        day   = logfile.name
        month = logfile.parent.name
        year  = logfile.parent.parent.name

        contrib_logfile = maindoc / "changelog" / year / f"{month}-{day}"

        copyfromto(
            logfile,
            contrib_logfile
        )

        contrib_logfile.write_text(
            data = contrib_tex_template(
                logfile.read_text(),
            )
        )


def add_contrib_doc(
    tmpdir,
    projdir,
    rolloutdir,
    toc_doc,
    main_lang = 'fr'
):
    projectname = projdir.name
    contribdir  = projdir / "contrib" / "doc" / "manual"

    for langdir in contribdir.glob("*"):
        if (
            not langdir.is_dir()
            or
            langdir.name.startswith('.')
            or
            langdir.name in ['changes', 'status', main_lang]
        ):
            continue

        lang = langdir.name

        print(f"+ MANUAL - New translation: {lang.upper()}.")

        destfile = rolloutdir / 'doc' / f'{projectname}-{lang}.tex'

        code = r"""
\documentclass[10pt, a4paper]{article}

\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}

\usepackage[english]{babel, varioref}

\usepackage{enumitem}

\usepackage{tabularray}
\usepackage{fmtcount}

\setlength{\parindent}{0em}
    """.strip() + f"""

% Package documented.
\\usepackage[lang = english]{{{projectname}}}
        """.rstrip() + '\n'*3

        locale_tmpdir = tmpdir / f"{langdir.name}"

        emptydir(locale_tmpdir)

        for docpartfile in toc_doc:
            pieces = extractfrom_TEX(docpartfile)
            prepare_TEX(_, locale_tmpdir, *pieces)
