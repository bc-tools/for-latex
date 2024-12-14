# --------------- #
# -- CONSTANTS -- #
# --------------- #

CHANGELOG_NEXT="changelog/next.tex"


# ----------------------- #
# -- ONE FOLDER NEEDED -- #
# ----------------------- #

if [ -z "$1" ]
then
    echo "CRITICAL - Missing arg: absolute target folder needed."
    exit 1
fi

if [ ! $# -eq 1 ]
then
    echo "CRITICAL - Too much arguments!"
    exit 1
fi

TARGET=$1

if [ ! -d "$TARGET" ]
then
    echo "CRITICAL - Missing absolute target folder: ''$TARGET''."
    exit 1
fi


# ----------------------------------------- #
# -- COMPILATION OF ALL DEV. LATEX FILES -- #
# ----------------------------------------- #

function nocompile {
    echo "LaTeX compilation failed with\n$1"
    open "$1"
}


cd "$TARGET"

for f in */*.tex
do
    fdir=$(dirname "$f")

    if [ "$f" != "$CHANGELOG_NEXT" ]
    then
        cd "$TARGET/$fdir"

        echo "-- NEW TEX FILE --"
        echo "$f"
        echo ""
        SOURCE_DATE_EPOCH=0 FORCE_SOURCE_DATE=1 latexmk -quiet -pdf -pdflatex="pdflatex --interaction=nonstopmode --halt-on-error --shell-escape  %O %S" "$TARGET/$f" || nocompile "$TARGET/$f"
    fi
done # for f in */*.tex;
