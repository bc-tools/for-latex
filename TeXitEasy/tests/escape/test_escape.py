#!/usr/bin/env python3

from cbdevtools import *

from pytest import fixture


# ------------------------------------ #
# -- FUNCTION(S) / CLASS(ES) TESTED -- #
# ------------------------------------ #

MODULE_DIR = addfindsrc(
    file    = __file__,
    project = 'TeXitEasy',
)

from src.escape import escape as ESCAPE_FUNCTION


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


# ------------------- #
# -- GOOD ESCAPING -- #
# ------------------- #

def test_latex_use_escape(orpyste_fix_block):
    tests = THE_DATAS_FOR_TESTING.mydict("std nosep nonb")

    for testname, infos in tests.items():
        source        = infos['source']
        escaped_texts = {}

        if 'text' in infos:
            escaped_texts['text'] = infos['text']
        else:
            escaped_texts['text'] = infos['both']

        if 'math' in infos:
            escaped_texts['math'] = infos['math']
        else:
            escaped_texts['math'] = infos['both']

        for mode in ['text', 'math']:
            answer_found = ESCAPE_FUNCTION(
                text = source,
                mode = mode
            )

            answer_wanted = escaped_texts[mode]

            assert answer_wanted == answer_found
