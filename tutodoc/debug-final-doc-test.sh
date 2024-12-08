#!/bin/bash

# --------------- #
# -- CONSTANTS -- #
# --------------- #

THISDIR=`dirname $0 | while read a; do cd $a && pwd && break; done`
PROJECTNAME=$(basename "$THISDIR")


# ------------------- #
# -- NO ARG NEEDED -- #
# ------------------- #

if [ ! $# -eq 0 ]
then
    echo "CRITICAL - No argument expected!"
    exit 1
fi


# ------------------------------- #
# -- COMPILATION OF FINAL DOCS -- #
# ------------------------------- #

function nocompile {
    echo "LaTeX compilation failed with\n$1"
    open "$1"
}


cd "$THISDIR/rollout"


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


# ------------------------ #
# -- OPEN ONLY PDF DOCS -- #
# ------------------------ #

cd debug

for f in *.pdf
do
    case $f in
      ("$PROJECTNAME"*) open "$f";;
    esac
done # for f in *.pdf;
