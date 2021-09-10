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

project = Project(
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

print('---')

for f in project.lof:
    relpath = f.relative_to(PROJECT_DIR / 'src')

    if (
        len(relpath.parents) - 1 == 1
        and
        relpath.suffix in ['.sty', '.tex']
    ):
        print(relpath)
