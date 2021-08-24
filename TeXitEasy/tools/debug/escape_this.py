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

from src.escape import *

txt = "\OH/ & ..."

print("Default mode (MODE_TEXT):")
print(escape(txt))
print()
print("Math mode:")
print(escape(text = txt, mode = 'MODE_MATH'))
