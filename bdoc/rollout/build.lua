module = "bdoc"

sourcefiles = {"code/*.sty"}

typesetfiles     = {"doc/*.tex"}
typesetsuppfiles = {"doc/*/*"}

checkopts   = "-interaction=nonstopmode --shell-escape"
-- checkopts   = "-interaction=batchmode --shell-escape"
typesetopts = checkopts
