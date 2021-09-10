#!/usr/bin/env python3

from cbdevtools import *


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

PROJECT_DIR = Path("/Users/projetmbc/Google Drive/git[NEW]/coding/tools/for-latex") / 'bdoc'

project = TeXProject(
    project = PROJECT_DIR,
    source  = PROJECT_DIR / 'src',
    target  = '',
    ignore  = '''
        tool_*/
        tool_*.*

        test_*/
        test_*.*

        *-FR.pdf
        *-EN.pdf
    ''',
    usegit = True
)

project.build()

print('--- STY ---')

for f in project.lof_sty_src:
    print(f)

print('--- TEX ---')

for f in project.lof_tex_src:
    print(f)
