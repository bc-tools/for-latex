PRE_HOOK  = {}
POST_HOOK = {}

from pathlib import Path


# --------------- #
# -- CONSTANTS -- #
# --------------- #

TMPL_CONTENT_CODE = r"""
% ----------------------------- %
% -- AT END DOCUMENT - START -- %
% ----------------------------- %

% The following AT-END-DOCUMENT lines of codes have been generated
% automatically. Don't judge their relative beauty...

\AtEndDocument{

% An annex page for a pretty doc.
\newpage

<<ANNEX-PAGE>>

\newpage

% Let's build the PDFs.
<<BUILD-PDFs>>

% The gallery starts here...
<<THE-THEMES>>

}

% --------------------------- %
% -- AT END DOCUMENT - END -- %
% --------------------------- %
""".strip()

TEX_BUILD_CMD = r"""
\immediate\write18{SOURCE_DATE_EPOCH=0 FORCE_SOURCE_DATE=1 latexmk -shell-escape -pdflatex gallery-showcase-<<THEME>>}
""".strip()

TMPL_INCLUDE_PDF = r"""
\includepdf[
	pages=1-2,
	fitpaper=true
]{gallery-showcase-<<THEME>>}
""".strip()

TMPL_VIRTUAL_PATH = r"gallery-showcase-<<THEME>>.tex"


THIS_DIR     = Path(__file__).parent
MAIN_CSS_DIR = THIS_DIR.parent / "src" / "main" / "css"

ALL_THEMES = []

for cssfile in MAIN_CSS_DIR.glob("*.cls.sty"):
    theme = Path(cssfile.stem).stem
    theme = theme.split('-')[-1]

    ALL_THEMES.append(theme)

ALL_THEMES.sort()


# ----------- #
# -- TOOLS -- #
# ----------- #

def jointhis(texts):
    return "\n\n".join(texts)

def rafterit(text):
    return f"<<{text}>>"

def multireplace(
    text,
    replacements
):
    for k, v in replacements.items():
        text = text.replace(k, v)

    return text


# ----------- #
# -- TOOLS -- #
# ----------- #

# We have to work with the folder conaining the hooks real file.
# TeXfacto will only send us the folder conaining the fole associated to the hooks.
def theme_gallery(
    curdir,
    isfordebug = False
):
# Template for the showcase.
    tmpl_theme = "color"

    tmpl_showcase_code = curdir / "tmpl-theme-showcase-color.tex"

    if not tmpl_showcase_code.is_file():
        raise IOError(
            f'missing template file:\n{tmpl_showcase_code}'
        )

    tmpl_showcase_code = tmpl_showcase_code.read_text()

    # print(tmpl_showcase_code[:200]);print('+++')

    if not isfordebug:
        tmpl_showcase_code = tmpl_showcase_code.replace(
            r"""
\documentclass[10pt, a4paper, theme = color]{../main/main}

\input{../preamble.cfg.tex}

\usepackage{../admonitions/admonitions.cls}
\usepackage{../listing/listing.cls}
\usepackage{../version-n-change/version-n-change.cls}
            """.strip(),
            r"""
\documentclass[10pt, a4paper, theme = color]{tutotoc}

\input{../preamble.cfg.tex}
            """.strip()
        )

# Template for the annex front page.
    tmpl_annex_code = curdir / "tmpl-theme-annex-page.tex"

    if not tmpl_annex_code.is_file():
        raise IOError(
            f'missing template file:\n{tmpl_annex_code}'
        )

    tmpl_annex_code = tmpl_annex_code.read_text()

    _ , _ , tmpl_annex_code = tmpl_annex_code.partition(r"\begin{document}")
    tmpl_annex_code, _ , _  = tmpl_annex_code.partition(r"\end{document}")

    tmpl_annex_code = tmpl_annex_code.strip()

# Let's build the pieces of our work.
    virtual_resrc   = {}
    build_pdfs_code = []
    include_pdfs    = []

    main_theme_brackets = f"{{{tmpl_theme}}}"
    option_theme        = f"theme = {tmpl_theme}]"

    for theme in ALL_THEMES:
        # print(tmpl_showcase_code[:200]);print('---')

        contents = multireplace(
            text         = tmpl_showcase_code,
            replacements = {
                main_theme_brackets: f"{{{theme}}}",
                option_theme       : f"theme = {theme}]"
            },
        )

        # print(contents[:200]);exit()

        virtual_resrc[
            TMPL_VIRTUAL_PATH.replace(
                rafterit("THEME")                  ,
                theme
            )
        ] = contents

        build_pdfs_code.append(
            TEX_BUILD_CMD.replace(rafterit("THEME"), theme)
        )

        include_pdfs.append(
            TMPL_INCLUDE_PDF.replace(rafterit("THEME"), theme)
        )

    tex_code = multireplace(
        text         = TMPL_CONTENT_CODE,
        replacements = {
            rafterit("ANNEX-PAGE"): tmpl_annex_code,
            rafterit("BUILD-PDFs"): jointhis(build_pdfs_code),
            rafterit("THE-THEMES"): jointhis(include_pdfs),
        },
    )

    return virtual_resrc, tex_code


POST_HOOK['theme/theme.tex'] = theme_gallery


# ------------------- #
# -- MAIN AS DEBUG -- #
# ------------------- #

if __name__ == "__main__":
    src_theme_dir = THIS_DIR.parent / "src" / "theme"
    debug_file    = src_theme_dir / "debug-gallery.tex"

    tmpl_debug_file = r"""
<<THE-FILE-CONTENTS>>

\documentclass[10pt, a4paper]{../main/main}

\input{../preamble.cfg.tex}

\usepackage{../admonitions/admonitions.cls}

\begin{document}

<<TEX-CONTENT>>

\end{document}
    """.strip()

    tmpl_file_contents = r"""
\begin{filecontents*}[overwrite]{<<VIRTUAL-PATH>>}
<<TEX-CODE-THEME-SHOWCASE>>
\end{filecontents*}
""".strip()

    virtual_resrc, tex_code = theme_gallery(
        curdir = src_theme_dir,
        isfordebug   = True
    )

    file_contents_code = [
        multireplace(
            text         = tmpl_file_contents,
            replacements = {
                rafterit("VIRTUAL-PATH")           : vpath,
                rafterit("TEX-CODE-THEME-SHOWCASE"): content,
            },
        )
        for vpath, content in virtual_resrc.items()
    ]

    tex_code = multireplace(
        text         = tmpl_debug_file,
        replacements = {
            rafterit("THE-FILE-CONTENTS"): jointhis(file_contents_code),
            rafterit("TEX-CONTENT")      : tex_code,
        },
    )

    debug_file.write_text(tex_code)

    print("Job done!")
