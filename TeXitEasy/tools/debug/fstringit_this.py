#! /usr/bin/env python3

from cbdevtools import *


# ------------------------------------ #
# -- MODULES IMPORTED FROM SOURCES! -- #
# ------------------------------------ #

MODULE_DIR = addfindsrc(
    file    = __file__,
    project = 'TeXitEasy',
)


# -------------- #
# -- LET'S GO -- #
# -------------- #

from src.escape import fstringit

texcode = r'''
\NewDocumentCommand{ \fictivenv }
                   { O{abc}m }{
    \onemacro{<:PYVAR_FOR_FSTRING:>}{#2}
}
'''

print(fstringit(texcode))
