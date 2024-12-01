import re

from .tags import *

TEX_IMPORT_CMDS = {
    "LoadClass"     : TAG_CLS,
    "RequirePackage": TAG_PACK,
    "usepackage"    : TAG_PACK,
}

TAG_CMD_SET_ABREVS = {
    "opt": TAG_OPTIONS,
    "lib": TAG_LIBRARIES,
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
        (\[(?P<options>[^][]*)\])?    #  XXXX
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
        {(?P<options>[^{}]*)}    #  XXXX
        (?:[^{]*)                #  XXXX
        {(?P<name>[^{}]*)}       #  XXXX
    """.strip(),
    re.VERBOSE
)


TEX_KIND_2_CMDS = {
    TAG_CLS_PASS_OPTS: ["PassOptionsToClass"],
}

for cmd, kind in TEX_IMPORT_CMDS.items():
    if kind in TEX_KIND_2_CMDS:
        TEX_KIND_2_CMDS[kind].append(cmd)

    else:
        TEX_KIND_2_CMDS[kind] = [cmd]