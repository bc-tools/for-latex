# --------------- #
# -- CONSTANTS -- #
# --------------- #

THISDIR=$(dirname "$0")
WORKINGDIR=$(pwd)


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

cd rollout/debug

rm -r *
