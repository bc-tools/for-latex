import re

from .tags import *

TEX_IMPORT_CMDS = {
    "LoadClass"     : TAG_CLS,
    "RequirePackage": TAG_PACK,
    "usepackage"    : TAG_PACK,
}

TAG_CMD_SET_ABREVS = {
    "opt": TAG_OPTION,
    "lib": TAG_LIBRARY,
}

TEX_SETUP_CMDS = {
# Special option settings.
    "geometry"      : "opt:geometry",
    "hypersetup"    : "opt:hyperref",
# Additional libraries.
    "tcbuselibrary" : "lib:tcolorbox",
    "usetikzlibrary": "lib:tikz",
}


TEX_ALL_CMDS = list(TEX_IMPORT_CMDS) + list(TEX_SETUP_CMDS)


IMPORT_PATTERN = re.compile(
    r"\\(?P<kind>" + "|".join(TEX_ALL_CMDS) + ")"
    +                                 #  XXXX
    r"""
        (\[(?P<option>[^][]*)\])?    #  XXXX
        (?P<xtra_1>[^{]*)             #  XXXX
        {(?P<name>[^{}]*)}            #  XXXX
        (?P<xtra_2>.*)                #  XXXX
        (?:\n\s*\[(?P<version>[^][]*)])? #  XXXX
    """.strip(),
    re.VERBOSE
)


CLASS_OPTS_PASSED_PATTERN = re.compile(
    r"""
        \\(?:PassOptionsToClass) #  XXXX
        (?:[^{]*)                #  XXXX
        {(?P<option>[^{}]*)}    #  XXXX
        (?:[^{]*)                #  XXXX
        {(?P<name>[^{}]*)}       #  XXXX
    """.strip(),
    re.VERBOSE
)


TEX_KIND_2_CMDS = {
    TAG_CLS_PASS_OPT: ["PassOptionsToClass"],
}

for cmd, kind in TEX_IMPORT_CMDS.items():
    if kind in TEX_KIND_2_CMDS:
        TEX_KIND_2_CMDS[kind].append(cmd)

    else:
        TEX_KIND_2_CMDS[kind] = [cmd]


TEXLOG_INFOS_PATTERN = re.compile(
    r"""
        (?P<name>[a-zA-Z-][a-zA-Z-\d]*)
        .
        (?P<ext>[a-zA-Z]+)
        \s*
        (?P<date>\d+[/-]\d+[/-]\d+)
    """.strip(),
    re.VERBOSE
)
