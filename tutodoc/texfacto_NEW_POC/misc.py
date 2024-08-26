from shutil      import rmtree

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


# ------------------- #
# -- OS OPERATIONS -- #
# ------------------- #

def emptydir(folder):
    if folder.is_dir():
        print(f'+ Cleaning {folder.parent.name}/{folder.name}')

        rmtree(folder)

    else:
        print(f'+ Creation of {folder.name}')

    folder.mkdir(parents = True)


def copyfromto(
    srcfile,
    destfile,
    mode = "w"
):
    with srcfile.open(
        encoding = "utf-8",
        mode = "r"
    ) as f:
        content = f.read()

    destfile.parent.mkdir(parents=True, exist_ok=True)
    destfile.touch()

    with destfile.open(
        encoding = "utf-8",
        mode = mode
    ) as f:
        f.write(content)


def addcontentto(
    content,
    destfile
):
    with destfile.open(
        encoding = "utf-8",
        mode = "a"
    ) as f:
        f.write(content)


def adddocsubdir(
    source,
    tmpdir,
    dirview,
    firstcall = True
):
    for onedir, dircontent in dirview.items():
        if firstcall and onedir.name == "locale":
            continue

        relpath = onedir.relative_to(source)

        if firstcall:
            print(f'   * [RES-DOC] Copying {relpath}/')

        destdir = tmpdir / relpath

        if not destdir.is_dir():
            destdir.mkdir(parents = True)

        for srcfile in dircontent[TAG_FILE]:
            copyfromto(srcfile, destdir / srcfile.name)

            TOC_DOC_RESRCES.append(srcfile)

        adddocsubdir(source, tmpdir, dircontent[TAG_DIR], firstcall=False)


# ----------------------- #
# -- SPECIFIC ITERATOR -- #
# ----------------------- #

def iter_sorted_useful_files(
    source,
    sorted_useful_files,
    ext_wanted,
    all_kinds
):
    not_first_dir = False

    for onedir, files_n_resrc in sorted_useful_files.items():
        if not_first_dir:
            print()

        else:
            not_first_dir = True

        print(f'+ Working in src/{onedir.relative_to(source)}/')

        for kind in all_kinds:
            for srcfile in files_n_resrc[kind]:
                ext = srcfile.suffix[1:]

                if ext != ext_wanted:
                    continue

                yield onedir, srcfile, kind
