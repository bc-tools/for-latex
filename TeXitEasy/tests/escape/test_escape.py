#!/usr/bin/env python3

from pathlib import Path
from pytest import fixture
import sys

from orpyste.data import ReadBlock as READ


# ----------------------- #
# -- GENERAL CONSTANTS -- #
# ----------------------- #

THIS_DIR = Path(__file__).parent


# ------------------------------------ #
# -- MODULES IMPORTED FROM SOURCES! -- #
# ------------------------------------ #

PROJECT_NAME = 'TeXitEasy'
MODULE_DIR   = THIS_DIR

if not PROJECT_NAME in str(MODULE_DIR):
    raise Exception(
        "call the script from a working directory containing the project."
    )

while(not MODULE_DIR.name.startswith(PROJECT_NAME)):
    MODULE_DIR = MODULE_DIR.parent

sys.path.append(str(MODULE_DIR))

from src.escape import escape


# ------------------------------------ #
# -- FUNCTION(S) / CLASS(ES) TESTED -- #
# ------------------------------------ #

ESCAPE_FUNCTION = escape


# ----------------------- #
# -- DATAS FOR TESTING -- #
# ----------------------- #

WHAT_IS_TESTED = Path(__file__).stem
WHAT_IS_TESTED = WHAT_IS_TESTED.replace('test_', '')

THE_DATAS_FOR_TESTING = READ(
    content = THIS_DIR / f'{WHAT_IS_TESTED}.peuf',
    mode    = {"keyval:: =": ":default:"}
)

@fixture(scope="module")
def or_datas(request):
    THE_DATAS_FOR_TESTING.build()

    def remove_extras():
        THE_DATAS_FOR_TESTING.remove_extras()

    request.addfinalizer(remove_extras)


# ------------------- #
# -- GOOD ESCAPING -- #
# ------------------- #

def test_latex_use_escape(or_datas):
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
