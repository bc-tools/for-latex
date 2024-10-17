from pathlib import Path
import              re


# ---------- #
# -- TAGS -- #
# ---------- #

TAG_LANG_EN = "en"
TAG_LOCALE  = "locale"

TAG_ABSTRACT = "abstract"

TAG_DIR  = "dir"
TAG_FILE = "file"

TAG_TOC  = "toc"

TAG_ABOUT_FILE = "about.yaml"

TAG_CONF = "cfg"

TAG_CLS = "cls"
TAG_STY = "sty"
TAG_TEX = "tex"

TAG_RESRC     = "resource"
TAG_CLS_RESRC = f"{TAG_CLS}-{TAG_RESRC}"
TAG_STY_RESRC = f"{TAG_STY}-{TAG_RESRC}"
TAG_TEX_RESRC = f"{TAG_TEX}-{TAG_RESRC}"

TAG_CFG_CLS = f"{TAG_CONF}.{TAG_CLS}.{TAG_STY}"
TAG_CFG_STY = f"{TAG_CONF}.{TAG_STY}"
TAG_CFG_TEX = f"{TAG_CONF}.{TAG_TEX}"

TAG_ALL  = "all"
TAG_TEMP = "temp"

TAG_CREATION = "creation"
TAG_DATE     = "date"
TAG_DAY      = "day"
TAG_MONTH    = "month"
TAG_YEAR     = "year"

TAG_AUTHOR    = "author"
TAG_DESC      = "desc"
TAG_PROJ_DIR  = "proj-dir"
TAG_PROJ_NAME = "proj-name"
TAG_ROLLOUT   = "rollout"
TAG_SRC       = "source"

TAG_API       = "api"
TAG_LANG_API  = "lang-api"
TAG_API_LANGS = "api-langs"

TAG_VERSIONS = "versions"
TAG_NB       = "nb"
TAG_ALL      = "all"
TAG_LAST     = "last"

TAG_CONTRIB           = "contrib"
TAG_TRANSLATE         = "translate"
TAG_DOC               = "doc"
TAG_CHGE_LOG          = "changelog"

TAG_MANUAL            = "manual"
TAG_MANUAL_DEV_LANG   = "manual-dev-lang"
TAG_MANUAL_OTHER_LANG = "manual-other-lang"

TAG_STATUS          = "status"
TAG_STATUS_ON_HOLD  = "on hold"
TAG_STATUS_KO       = "ko"
TAG_STATUS_OK       = "ok"
TAG_STATUS_UPDATE   = "update"
TAG_STATUS_LANG_API = "lang-api"

TAG_TMP_CLS_IMPORT  = f'.tmp_pack_import.{TAG_CLS}'
TAG_TMP_CLS_OPTIONS = f'.tmp_pack_options.{TAG_CLS}'
TAG_TMP_CLS_SRC     = f'.tmp_pack_src.{TAG_CLS}'

TAG_TMP_STY_IMPORT  = f'.tmp_pack_import.{TAG_STY}'
TAG_TMP_STY_OPTIONS = f'.tmp_pack_options.{TAG_STY}'
TAG_TMP_STY_SRC     = f'.tmp_pack_src.{TAG_STY}'

TAG_TMP_TEX_FOR_DOC = f'.tmp_fordoc.{TAG_TEX}'
TAG_TMP_TEX_THE_DOC = f'.tmp_thedoc.{TAG_TEX}'


TAG_TMP_PREAMBLE = f'preamble.{TAG_CONF}.{TAG_TEX}'


# ------------------------- #
# -- MC = MAGIC COMMENTS -- #
# ------------------------- #

for kind in [
    "PACKAGES",
    "OPTIONS",
    "TOOLS",
    "FORDOC",
    "CONTRIB - LOAD",
]:
    varname = kind

    for old, new in [
        (' ', ''),
        ('-', '_')
    ]:
        varname = varname.replace(old, new)

    globals()[f"TAG_MC_{varname}"] = f"% == {kind} == %"


# -------------- #
# -- PATTERNS -- #
# -------------- #

CMDS_FOR_FILE_PATTERNS = [
    re.compile(
          r"^([^%\\]*)(.*)(\\"
        + macroname
        + ")(\[.*\][\t ]*\n?[\t ]*)?{(.*)}(.*)$"
    )
    for macroname in [
        "input",
        "tdoclatexshow",
        "tdoclatexinput",
        "tdocshowcaseinput",
        "tdocdocbasicinput",
    ]
]


CMD_ARG_PATTERN = re.compile('#(\d+)')


DATE_PATTERN = re.compile(r"==\n(\d+)\s+\((.+)\)\n==")


VERSION_EQUAL_PATTERN = re.compile(r"==\n(\d+)\s+\((.+)\)\n==")


TITLE_PATTERNS = [
    re.compile(
          r"% ("
        + d
        + r"{2})\s+(.+)\s+("
        + d
        + r"{2}) %"
    )
    for d in "=-:"
]

# --------------- #
# -- LANGUAGES -- #
# --------------- #

LANG_NAMES = {
    'en' : {
        'en': "English",
        'fr': "French",
    },
    'fr' : {
        'en': "anglais",
        'fr': "français",
    },
}

HISTORY_TRANS = {
    'en' : "History",
    'fr' : "Historique",
}


# -------------- #
# -- SRC CODE -- #
# -------------- #

SRC_CODE_HEADER = """
This is file `<<PROJ_NAME>>.{ext}' generated automatically.

Copyright (C) <<CREATION_YEAR>>-<<LAST_YEAR>> by <<AUTHOR>>

This file may be distributed and/or modified under
the conditions of the GNU 3 License.
""".strip()

SRC_CODE_HEADER_STY = SRC_CODE_HEADER.format(ext = "sty")
SRC_CODE_HEADER_CLS = SRC_CODE_HEADER.format(ext = "cls")


SRC_CODE_PROVIDE = """
\\ProvidesExpl{kind}
  {{<<PROJ_NAME>>}}
  {{<<LAST_DATE>>}}  % Creation: <<CREATION_DATE>>
  {{<<LAST_NB_VER>>}}
  {{<<SHORT_DESC>>}}
""".strip()

SRC_CODE_PROVIDE_PACK = SRC_CODE_PROVIDE.format(kind = "Package")
SRC_CODE_PROVIDE_CLS  = SRC_CODE_PROVIDE.format(kind = "Class")
