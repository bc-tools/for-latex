# --------------- #
# -- CONSTANTS -- #
# --------------- #

THISDIR=$(dirname "$0")
WORKINGDIR=$(pwd)


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
    echo "CRITICAL - Missing folder: ''$TARGET''."
    exit 1
fi


# --------------------- #
# -- LISTED PROJECTS -- #
# --------------------- #

function nocompile {
    echo ""
    echo "-- COMPILE FAILES --"
    echo "See ''$1''."
    open "$1"
    exit 1
}

cd "$TARGET"

for f in */*.tex; do
    fdir=$(dirname "$f")

    cd "$TARGET/$fdir"

    if [ ! "$fdir" = "changelog" ]
    then
        SOURCE_DATE_EPOCH=0 FORCE_SOURCE_DATE=1 latexmk -silent -shell-escape -pdflatex "$TARGET/$f"
        # || nocompile "$TARGET/$f"

        # exit 0
    fi


done
