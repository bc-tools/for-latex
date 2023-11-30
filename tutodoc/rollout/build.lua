-- Sources.
--     * https://www.latex-project.org/news/2019/04/16/l3build-upload/
--     * https://ctan.org/help/submit
--     * https://ctan.org/license
--     * https://ctan.org/topics/highscore
--     * https://ctan.org/incoming

module = "tutodoc"

sourcefiledir = "code"
sourcefiles   = {"*.sty"}

flatten = false
flattentds = false

docfiledir = "doc"
typesetfiles = {"tutodoc-fr.tex"}
-- typesetsourcefiles = {"**/*"}

checkopts   = "-interaction=nonstopmode --shell-escape"
-- checkopts   = "-interaction=batchmode --shell-escape"
typesetopts = checkopts


uploadconfig = {
    author     = "Christophe BAL",
    uploader   = "Christophe BAL",
    email      = "projetmbc@gmail.com",
    license    = "gpl3",
    pkg        = "tutodoc",
    version    = "1.0.0 [2023-11-29]",
    update     = false,
    summary    = 'This package proposes tools for writing "human friendly" documentations of LaTeX packages.',
    topic      = {"doc-tool"},
    ctanPath   = "/macros/latex/contrib/tutodoc",
    repository = "https://github.com/bc-tools/for-latex",
    bugtracker = "https://github.com/bc-tools/for-latex/issues",
    note       = [[Uploaded automatically by l3build...]]
}
