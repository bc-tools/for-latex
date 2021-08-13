#!/usr/bin/env python3

from cbdevtools import *


# ------------------------------------ #
# -- FUNCTION(S) / CLASS(ES) TESTED -- #
# ------------------------------------ #

MODULE_DIR = addfindsrc(
    file    = __file__,
    project = 'TeXitEasy',
)

from src.escape import escape


# ------------------- #
# -- GOOD ESCAPING -- #
# ------------------- #

def test_latex_use_escape(peuf_fixture):
    datas = peuf_fixture(__file__)

    for infos in datas.values():
        source  = infos['source']

        for mode in ['text', 'math']:
            found = escape(
                text = source,
                mode = mode
            )

            if 'both' in infos:
                wanted = infos['both']

            elif not mode in infos:
                continue

            else:
                wanted = infos[mode]

            assert wanted == found
