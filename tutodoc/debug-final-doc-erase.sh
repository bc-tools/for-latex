#!/bin/bash

# --------------- #
# -- CONSTANTS -- #
# --------------- #

THISDIR=$(dirname $0 | while read a; do cd $a && pwd && break; done)

# Do not make error here, because a ''rm'' is coming soon!
DEBUGDIR="$THISDIR/rollout/debug"


# ------------------- #
# -- NO ARG NEEDED -- #
# ------------------- #

if [ ! $# -eq 0 ]
then
    echo "CRITICAL - No argument expected!"
    exit 1
fi


# -------------------------- #
# -- JUST REMOVE ANYTHING -- #
# -------------------------- #

find "$DEBUGDIR" -mindepth 1 -delete
