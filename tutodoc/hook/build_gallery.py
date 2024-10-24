from pathlib import Path


# --------------- #
# -- CONSTANTS -- #
# --------------- #

TEMPLATE_DEBUG_FILE = r"""
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

TEMPLATE_FILE_CONTENTS = r"""
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


THIS_DIR     = Path(__file__).parent
MAIN_CSS_DIR = THIS_DIR / "src" / "main" / "css"

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

def main(dir_analyzed):
# Template for the showcase.
    tmpl_theme = "color"

    tmpl_showcase_code = dir_analyzed / "tmpl-theme-showcase-color.tex"
    tmpl_showcase_code = tmpl_showcase_code.read_text()

# Template for the annex front page.
    tmpl_annex_code = dir_analyzed / "tmpl-theme-annex-page.tex"
    tmpl_annex_code = tmpl_annex_code.read_text()

    _ , _ , tmpl_annex_code = tmpl_annex_code.partition(r"\begin{document}")
    tmpl_annex_code, _ , _  = tmpl_annex_code.partition(r"\end{document}")

    tmpl_annex_code = tmpl_annex_code.strip()

# Let's build the pieces of our work.
    file_contents_code = []
    build_pdfs_code    = []
    include_pdfs       = []

    main_theme_brackets = f"{{{tmpl_theme}}}"
    option_theme        = f"theme = {tmpl_theme}]"

    for theme in ALL_THEMES:
        contents = multireplace(
            text         = tmpl_showcase_code,
            replacements = {
                main_theme_brackets: f"{{{theme}}}",
                option_theme       : f"theme = {theme}]"
            },
        )

        file_contents_code.append(
            multireplace(
                text         = TEMPLATE_FILE_CONTENTS,
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

# We can build the TeX code.
    tex_code = multireplace(
        text         = TEMPLATE_DEBUG_FILE,
        replacements = {
            rafterit("ANNEX-PAGE")       : tmpl_annex_code,
            rafterit("THE-FILE-CONTENTS"): jointhis(file_contents_code),
            rafterit("BUILD-PDFs")       : jointhis(build_pdfs_code),
            rafterit("THE-THEMES")       : jointhis(include_pdfs),
        },
    )

    return tex_code


# ------------------- #
# -- MAIN AS DEBUG -- #
# ------------------- #

if __name__ == "__main__":
    src_theme_dir = THIS_DIR.parent / "src" / "theme"
    debug_file    = src_theme_dir / "debug-gallery.tex"

    tex_code = main(src_theme_dir)

    debug_file.write_text(tex_code)
