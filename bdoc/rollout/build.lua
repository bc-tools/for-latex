module = "bdoc"

docfiledir = "doc"
sourcefiledir = "code"
sourcefiles = {"*.sty"}


typesetfiles     = {"*.tex"}
typesetsourcefiles = {"*/**"}

checkopts   = "-interaction=nonstopmode --shell-escape"
-- checkopts   = "-interaction=batchmode --shell-escape"
typesetopts = checkopts
