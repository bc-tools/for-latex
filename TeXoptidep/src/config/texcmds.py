import re

from .tags import TAG_CLS, TAG_PACK

TEX_IMPORT_CMDS = {
    "LoadClass"     : TAG_CLS,
    "RequirePackage": TAG_PACK,
    "usepackage"    : TAG_PACK,
}


TEX_SETUP_LIBS_OR_OPTS_CMDS = {
    "geometry"      : "geometry",
    "hypersetup"    : "hyperref",
    "tcbuselibrary" : "tcolorbox",
    "usetikzlibrary": "tikz",
}


TEX_ALL_CMDS = list(TEX_IMPORT_CMDS) + list(TEX_SETUP_LIBS_OR_OPTS_CMDS)


IMPORT_PATTERN = re.compile(
    r"\\(?P<kind>" + "|".join(TEX_ALL_CMDS) + ")"
    +                                 #  XXXX
    r"""
        (\[(?P<options>[^][]*)\])?    #  XXXX
        (?P<xtra_1>[^{]*)             #  XXXX
        {(?P<name>[^{}]*)}            #  XXXX
        (?P<xtra_2>.*)                #  XXXX
        (?:\n\s*\[(?P<date>[^][]*)])? #  XXXX
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
