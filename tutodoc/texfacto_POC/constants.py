from pathlib import Path
import              re


# ---------- #
# -- TAGS -- #
# ---------- #

TAG_DIR  = "dir"
TAG_FILE = "file"

TAG_TOC  = "toc"

TAG_ABOUT_FILE = "about.yaml"

TAG_STY = "sty"
TAG_TEX = "tex"

TAG_RESRC     = "resource"
TAG_STY_RESRC = f"{TAG_STY}-{TAG_RESRC}"
TAG_TEX_RESRC = f"{TAG_TEX}-{TAG_RESRC}"

TAG_CFG_STY = "cfg.sty"
TAG_CFG_TEX = "cfg.tex"

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

TAG_VERSIONS = "versions"
TAG_NB       = "nb"
TAG_ALL      = "all"
TAG_LAST     = "last"

TAG_CONTRIB           = "contrib"
TAG_DOC               = "doc"
TAG_CHGE_LOG          = "changelog"
TAG_MANUAL            = "manual"
TAG_MANUAL_DEV_LANG   = "manual-dev-lang"
TAG_MANUAL_OTHER_LANG = "manual-other-lang"

TAG_STATUS         = "status"
TAG_STATUS_ON_HOLD = "on hold"
TAG_STATUS_KO      = "ko"
TAG_STATUS_OK     = "ok"
TAG_STATUS_UPDATE = "update"

# -------------- #
# -- PATTERNS -- #
# -------------- #

CMDS_FOR_FILE_PATTERNS = [
    re.compile(r"^([^%\\]*)(.*)(\\" + macroname + ")(\[.*\][\t ]*\n?[\t ]*)?{(.*)}(.*)$")
    for macroname in [
        "input",
        "tdoclatexshow",
        "tdoclatexinput",
        "tdocshowcaseinput",
        "tdocdocbasicinput",
    ]
]


DATE_PATTERN = re.compile(r"==\n(\d+)\s+\((.+)\)\n==")


LATEX_CONTENT_PATTERN = re.compile(r"begin(.*)end")
