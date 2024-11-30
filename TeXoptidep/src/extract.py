from copy import deepcopy

from .config.patterns import *


def shorten(content):
    useful_content = []

    for line in content.split("\n"):
        short_line = line.strip()

        if not short_line or short_line.startswith("%"):
            continue

        useful_content.append(line)

    useful_content = "\n".join(useful_content)

    return useful_content


def extract_dep(content):
    useful_content = shorten(content)

    print(useful_content)
