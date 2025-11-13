#!/usr/bin/env python3

from pathlib import Path
from yaml    import safe_load


# ----------------------- #
# -- GENERAL CONSTANTS -- #
# ----------------------- #

THIS_DIR = Path(__file__).parent

def test_OK():
    print("OK")
