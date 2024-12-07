# --------------- #
# -- CONSTANTS -- #
# --------------- #

THISDIR=$(dirname "$0")
WORKINGDIR=$(pwd)

PROJECTNAME=$(basename "$WORKINGDIR")


# ----------------------- #
# -- ONE FOLDER NEEDED -- #
# ----------------------- #

if [ ! $# -eq 0 ]
then
    echo "CRITICAL - No argument expected!"
    exit 1
fi


# --------------------- #
# -- LISTED PROJECTS -- #
# --------------------- #

function nocompile {
    open "$1"
    exit 1
}

cd "rollout"

for f in code/*
do
    dest=$(basename "$f")
    dest="debug/$dest"

    cp "$f"  "$dest"
done # for f in code/*;

for f in doc/*.tex
do
    name=$(basename "$f")

    cp "$f"  "debug/$name"

    cd debug

    SOURCE_DATE_EPOCH=0 FORCE_SOURCE_DATE=1 latexmk -pdf -pdflatex="pdflatex --interaction=nonstopmode --halt-on-error --shell-escape  %O %S" "$name" || nocompile "$name"

    cd ../
done # for f in doc/*tex;

cd debug

for f in *.pdf
do
    echo "$PROJECTNAME  ||  $f"
    case $f in
      ("$PROJECTNAME"*) open "$f";;
    esac
done # for f in doc/*tex;
