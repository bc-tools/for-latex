# ----------------- #
# -- ASCII FRAME -- #
# ----------------- #

def frame(
    projname,
    title
):
    deco = '-'*(len(projname) + len(title) + 4)

    return f"""
{deco}
"{projname}": {title}
{deco}
    """.strip()


def print_frame(
    projname,
    title
):
    print()
    print()
    print(frame(projname, title))
    print()
