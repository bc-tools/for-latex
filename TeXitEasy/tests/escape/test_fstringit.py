#!/usr/bin/env python3

from pytest import fixture

from cbdevtools import *


# ------------------------------------ #
# -- FUNCTION(S) / CLASS(ES) TESTED -- #
# ------------------------------------ #

MODULE_DIR = addfindsrc(
    file    = __file__,
    project = 'TeXitEasy',
)

from src.escape import fstringit


# --------------------- #
# -- GOOD FSTRINGIFY -- #
# --------------------- #

def test_latex_use_fstringit(peuf_fixture):
    datas = peuf_fixture(__file__)

    for infos in datas.values():
        found  = fstringit(code = infos['source'])
        wanted = infos['fstring']

        assert wanted == found
