#!/usr/bin/env python3

from cbdevtools import *

projectname = 'bdoc'


# ------------------------------------ #
# -- MODULES IMPORTED FROM SOURCES! -- #
# ------------------------------------ #

MODULE_DIR = addfindsrc(
    file    = __file__,
    project = 'TeXfactory',
)


# -------------- #
# -- LET'S GO -- #
# -------------- #

from src import *

MONOREPO_DIR = MODULE_DIR.parent
PROJECT_DIR  = Path(projectname)

project = TeXProject(
    project = MONOREPO_DIR / PROJECT_DIR,
    source  = 'src',
    target  = projectname.lower(),
    ignore  = MONOREPO_DIR / 'ignore-for-prod.txt',
    usegit  = True,
    # readme  = 'README.md',
    readme  = 'readme',
)

project.build()
