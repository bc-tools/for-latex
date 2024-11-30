from copy import deepcopy

from .config.texcmds import *


def shorten(content: str) -> str:
    useful_content = []

    for line in content.split("\n"):
        short_line = line.strip()

        if not short_line or short_line.startswith("%"):
            continue

        useful_content.append(line)

    useful_content = "\n".join(useful_content)

    return useful_content


def clean_options(option: str) -> str:
    option = option.split("=")
    option = [x.strip() for x in option]
    option = " = ".join(option)

    return option


def extract_dep(content: str) -> dict:
    data   = {}
    errors = {}

    useful_content = shorten(content)

    matches = IMPORT_PATTERN.finditer(useful_content)

    if matches is None:
        return data, errors

    setup_libs_or_opts = {}

    for m in matches:
        kind = m["kind"].strip()

# Library import / Setup options lately.
        if kind in TEX_SETUP_LIBS_OR_OPTS_CMDS:
            last_settings = setup_libs_or_opts.get(kind, [])
            this_settings = [
                clean_options(x)
                for x in m["name"].split(',')
            ]

            print(this_settings)

            continue

    print(setup_libs_or_opts)



    return data, errors
