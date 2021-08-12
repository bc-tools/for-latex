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

from src.escape import fstringit as FSTRINGIT_FUNCTION


# ----------------------- #
# -- DATAS FOR TESTING -- #
# ----------------------- #

THE_DATAS_FOR_TESTING = build_datas_block(__file__)

@fixture(scope="module")
def orpyste_fix_block(request):
    THE_DATAS_FOR_TESTING.build()

    def remove_extras():
        THE_DATAS_FOR_TESTING.remove_extras()

    request.addfinalizer(remove_extras)


# --------------------- #
# -- GOOD FSTRINGIFY -- #
# --------------------- #

def test_latex_use_fstringit(orpyste_fix_block):
    tests = THE_DATAS_FOR_TESTING.mydict("std nosep nonb")

    for testname, infos in tests.items():
        answer_found  = FSTRINGIT_FUNCTION(code = infos['source'])
        answer_wanted = infos['fstring']

        assert answer_wanted == answer_found
