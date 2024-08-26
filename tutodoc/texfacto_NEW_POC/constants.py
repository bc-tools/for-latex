from pathlib import Path
import              re


# ---------- #
# -- TAGS -- #
# ---------- #

TAG_DIR      = "dir"
TAG_FILE     = "file"
TAG_RESOURCE = "resource"

TAG_TOC  = "toc"

TAG_ABOUT_FILE = "about.yaml"

TAG_STY = "sty"
TAG_TEX = "tex"

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
TAG_DOC_LANG  = "doc-lang"
TAG_MANUALS   = "manuals"
TAG_PROJ_DIR  = "proj-dir"
TAG_PROJ_NAME = "proj-name"
TAG_ROLLOUT   = "rollout"
TAG_SRC       = "source"

TAG_VERSION      = "version"
TAG_ALL_VERSIONS = "all-stable-versions"
TAG_LAST_VERSION = "last-stable-versions"


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
