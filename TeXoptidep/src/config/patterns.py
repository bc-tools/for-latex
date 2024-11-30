import re


TEX_STD_CMDS = """
LoadClass

RequirePackage
usepackage
"""

TEX_STD_CMDS = [
    x
    for x in TEX_STD_CMDS.split('\n')
    if x
]


TEX_SPECIAL_CMDS = {
    "geometry"      : "geometry",
    "hypersetup"    : "hyperref",
    "tcbuselibrary" : "tcolorbox",
    "usetikzlibrary": "tikz",
}

TEX_ALL_CMDS = TEX_STD_CMDS + list(TEX_SPECIAL_CMDS)


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

CLASS_OPTIONS_PASSED_PATTERN = re.compile(
    r"""
        \\(?:PassOptionsToClass) #  XXXX
        (?:[^{]*)                #  XXXX
        {(?P<options>[^{}]*)}    #  XXXX
        (?:[^{]*)                #  XXXX
        {(?P<name>[^{}]*)}       #  XXXX
    """.strip(),
    re.VERBOSE
)
