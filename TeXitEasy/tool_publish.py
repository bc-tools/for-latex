#! /usr/bin/env python3

from pathlib import Path
from shutil  import rmtree, copy


# -------------------- #
# -- PROJECT'S NAME -- #
# -------------------- #

THIS_DIR = Path(__file__).parent

PROJECT_NAME = THIS_DIR.name.lower()

PROJECT_SRC       = THIS_DIR / 'src'
PROJECT_FINAL_DIR = THIS_DIR / PROJECT_NAME

README_SRC   = THIS_DIR / 'README.md'
README_FIANL = PROJECT_FINAL_DIR / 'README.md'

# --------------------------------- #
# -- RESET THE PROJECT FINAL DIR -- #
# --------------------------------- #

if PROJECT_FINAL_DIR.is_dir():
    rmtree(PROJECT_FINAL_DIR)
    
PROJECT_FINAL_DIR.mkdir(parents = True)


# ------------------------------------ #
# -- POPULATE THE PROJECT FINAL DIR -- #
# ------------------------------------ #

DIR_TAG  = "dir"
FILE_TAG = "file"


def recwalk(onedir):
    for onepath in onedir.iterdir():
        if (
            onepath.is_dir()
            and 
            keepit(onepath, DIR_TAG)
        ):
            recwalk(onepath)

        elif keepit(onepath, FILE_TAG):
            yield onepath


def keepit(onepath, kind):
    name = onepath.name

    if name.startswith('tool'):
        return False

    if name.startswith('.'):
        return False

    if name.startswith('x-'):
        return False

    if 'cpython' in name:
        return False
    
    return True


for onepath in recwalk(PROJECT_SRC):
    finalpath = PROJECT_FINAL_DIR / onepath.relative_to(PROJECT_SRC)

    copy(onepath, finalpath)


copy(README_SRC, README_FIANL)