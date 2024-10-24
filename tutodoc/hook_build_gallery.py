from pathlib import Path


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_DIR = Path(__file__).parent
MAIN_CSS_DIR = THIS_DIR.parent / "main" / "css"

MANUAL_FILE = THIS_DIR / "debug-gallery.tex"


TEMPLATE_SWOWCASE_THEME = "color"

TEMPLATE_SWOWCASE_COLOR = THIS_DIR / "tmpl-theme-showcase-color.tex"
TEX_CODE_SWOWCASE_COLOR = TEMPLATE_SWOWCASE_COLOR.read_text()

TEMPLATE_ANNEX_PAGE = THIS_DIR / "tmpl-theme-annex-page.tex"
TEMPLATE_ANNEX_PAGE = TEMPLATE_ANNEX_PAGE.read_text()

_ , _ , TEMPLATE_ANNEX_PAGE = TEMPLATE_ANNEX_PAGE.partition(r"\begin{document}")
TEMPLATE_ANNEX_PAGE, _ , _  = TEMPLATE_ANNEX_PAGE.partition(r"\end{document}")

TEMPLATE_ANNEX_PAGE = TEMPLATE_ANNEX_PAGE.strip()


TEMPLATE_FOR_MANUAL = r"""
<<THE-FILE-CONTENTS>>

\documentclass[10pt, a4paper]{../main/main}

\input{../preamble.cfg.tex}

\usepackage{../admonitions/admonitions.cls}

\begin{document}

% The following AT-END-DOCUMENT lines of code have been generated
% automatically. Don't judge their relative beauty...
\AtEndDocument{ % AT-END-DOCUMENT - START

% An annex page for a pretty doc.
\newpage

<<ANNEX-PAGE>>

\newpage

% Let's build the PDFs.
<<BUILD-PDFs>>

% The gallery starts here...
<<THE-THEMES>>

} % AT-END-DOCUMENT - END

\end{document}
""".strip() + "\n"

TEMPLATE_ONE_FILE_CONTENTS = r"""
\begin{filecontents*}[overwrite]{gallery-showcase-<<THEME>>.tex}
<<TEX-CODE-THEME-SHOWCASE>>
\end{filecontents*}
""".strip()

TEX_BUILD_CMD = r"""
\immediate\write18{SOURCE_DATE_EPOCH=0 FORCE_SOURCE_DATE=1 latexmk -shell-escape -pdflatex gallery-showcase-<<THEME>>}
""".strip()

TEMPLATE_INCLUDE_PDF = r"""
\includepdf[
	pages=1-2,
	fitpaper=true
]{gallery-showcase-<<THEME>>}
""".strip()


# ---------- #
# -- TOOL -- #
# ---------- #

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


# ----------------- #
# -- LET'S WORK! -- #
# ----------------- #

file_contents_code = []
build_pdfs_code    = []
include_pdfs       = []

main_theme_brackets = f"{{{TEMPLATE_SWOWCASE_THEME}}}"
option_theme        = f"theme = {TEMPLATE_SWOWCASE_THEME}]"


all_themes = []

for cssfile in MAIN_CSS_DIR.glob("*.cls.sty"):
    theme = Path(cssfile.stem).stem
    theme = theme.split('-')[-1]

    all_themes.append(theme)

all_themes.sort()


for theme in all_themes:
    contents = multireplace(
        text         = TEX_CODE_SWOWCASE_COLOR,
        replacements = {
            main_theme_brackets: f"{{{theme}}}",
            option_theme       : f"theme = {theme}]"
        },
    )

    file_contents_code.append(
        multireplace(
            text         = TEMPLATE_ONE_FILE_CONTENTS,
            replacements = {
              rafterit("THEME")                  : theme,
              rafterit("TEX-CODE-THEME-SHOWCASE"): contents
            },
        )
    )

    build_pdfs_code.append(
        TEX_BUILD_CMD.replace(rafterit("THEME"), theme)
    )

    include_pdfs.append(
        TEMPLATE_INCLUDE_PDF.replace(rafterit("THEME"), theme)
    )


tex_code = multireplace(
    text         = TEMPLATE_FOR_MANUAL,
    replacements = {
        rafterit("ANNEX-PAGE")       : TEMPLATE_ANNEX_PAGE,
        rafterit("THE-FILE-CONTENTS"): jointhis(file_contents_code),
        rafterit("BUILD-PDFs")       : jointhis(build_pdfs_code),
        rafterit("THE-THEMES")       : jointhis(include_pdfs),
    },
)

MANUAL_FILE.write_text(tex_code)
