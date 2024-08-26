from .constants import *


# ----------------- #
# -- ASCII FRAME -- #
# ----------------- #

def frame(
    projname,
    title,
    extra = ""
):
    deco = '-'*(len(projname) + len(title) + 4)

    if extra:
        extra = " "*2 + extra

    return f"""
{deco}
"{projname}": {title}{extra}
{deco}
    """.strip()


def print_frame(
    projname,
    title,
    extra = ""
):
    print()
    print(frame(projname, title, extra))
    print()


# -------------------- #
# -- DATE / VERSION -- #
# -------------------- #

def str_date(dict_date):
    return (
        f"{dict_date[TAG_YEAR]}-"
        f"{dict_date[TAG_MONTH]}-"
        f"{dict_date[TAG_DAY]}"
    )
