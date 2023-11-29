module = "bdoc"

sourcefiledir = "code"
sourcefiles   = {"*.sty"}

flatten = false
flattentds = false

docfiledir = "doc"
typesetfiles = {"bdoc-fr.tex"}
-- typesetsourcefiles = {"**/*"}

checkopts   = "-interaction=nonstopmode --shell-escape"
-- checkopts   = "-interaction=batchmode --shell-escape"
typesetopts = checkopts


uploadconfig = {
    author      = "Christophe BAL",
    -- license     = "lppl1.3c",
    summary     = 'This package proposes tools for writing "human friendly" documentations of LaTeX packages.',
    topic       = {"doc", "dev"},
    -- ctanPath    = "/macros/latex/contrib/l3build",
    repository  = "https://github.com/bc-tools/for-latex.git",
    -- bugtracker  = "https://github.com/latex3/l3build/issues",
    -- update      = true,
--     description = [[
--   The build system supports testing and building (La)TeX code, on
--   Linux, macOS, and Windows systems. The package offers:
--   * A unit testing system for (La)TeX code;
--   * A system for typesetting package documentation; and
--   * An automated process for creating CTAN releases.
--     ]]
}
