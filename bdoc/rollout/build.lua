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
