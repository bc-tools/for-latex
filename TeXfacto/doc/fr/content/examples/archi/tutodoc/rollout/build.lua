module = "tutodoc"

sourcefiledir = "code"
sourcefiles   = {"*.cls", "*.cls.sty", "DEPENDS.yaml"}

flatten    = false
flattentds = false

docfiledir   = "doc"
typesetfiles = {"*.tex"}

testfiledir = "tests"

checkopts   = "-interaction=nonstopmode --shell-escape"
-- checkopts   = "-interaction=batchmode --shell-escape"
typesetopts = checkopts

uploadconfig = {
    version      = "?",
    announcement = "TODO",
    author       = "Christophe BAL",
    uploader     = "Christophe BAL",
    email        = "?",
    license      = "gpl3",
    pkg          = "tutodoc",
    -- update       = false,
    summary      = 'This class proposes tools for writing "human friendly" documentations of LaTeX packages.',
    topic        = {},
    ctanPath     = "/macros/latex/contrib/tutodoc",
    repository   = "https://github.com/bc-tools/for-latex/tree/main/tutodoc",
    -- bugtracker   = "",
    note         = [[Uploaded automatically by l3build...]]
}
