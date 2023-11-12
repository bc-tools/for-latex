from collections import defaultdict
from shutil      import rmtree
from yaml        import safe_load

from natsort import natsorted


TAG_FILE = "file"
TAG_DIR  = "dir"

TAG_TOC  = "toc"

TAG_ABOUT_FILE = "about.yaml"

TAG_STY = "sty"
TAG_TEX = "tex"

TAG_CFG_STY = "sty"
TAG_CFG_TEX = "tex"


def dirs2analyze(
    source,
    alldirs
):
    src_about = source / "about.yaml"

    if not src_about.is_file():
        sorteddirs = None

    else:
        with src_about.open(
            encoding='utf8',
            mode='r',
        ) as f:
            about_cfg = safe_load(f)

        sorteddirs = about_cfg.get(TAG_TOC, None)

    if sorteddirs is None:
        sorteddirs = natsorted(alldirs)

    else:
        for i, p in enumerate(sorteddirs):
            if p[-1] != '/':
                TODO_PB

            p  = p[:-1]
            fp = source / p

            if not fp.is_dir():
                TODO_PB

            sorteddirs[i] = fp

    # print([p.name for p in sorting])

    return sorteddirs


def files2analyze(
    onedir,
    allfiles
):
    files_about = onedir / "about.yaml"

    if not files_about.is_file():
        sorted2analyze = None

    else:
        with files_about.open(
            encoding='utf8',
            mode='r',
        ) as f:
            about_cfg = safe_load(f)

        sorted2analyze = about_cfg.get(TAG_TOC, None)

    if sorted2analyze is None:
        sorted2analyze = natsorted(
            p
            for p in allfiles
            if p.suffix[1:] in [TAG_STY,TAG_TEX]
            and not p.suffix[1:] in [TAG_CFG_STY,TAG_CFG_TEX]
        )

    else:
        for i, p in enumerate(sorted2analyze):
            fp = onedir / p

            if not fp.is_file():
                TODO_PB

            sorted2analyze[i] = fp

    resources = [
        p
        for p in allfiles
        if not p in sorted2analyze
           and p.name != TAG_ABOUT_FILE
    ]

    # print([p.name for p in sorting])

    return sorted2analyze, resources


def emptydir(folder):
    if folder.is_dir():
        print(f'+ Cleaning src/{folder.name}')

        rmtree(folder)

    else:
        print(f'+ Creation of {folder.name}')

    folder.mkdir(parents = True)


def prepare(ext, srcfile, ):
    ...



def build_project(
    source  ,
    treeview
):
    projectname = source.parent.name

    projectfolder      = source.parent / projectname
    projectfolder_TEMP = source.parent / f".{projectname}"

    sorteddirs = dirs2analyze(
        source  = source,
        alldirs = list(treeview[TAG_DIR].keys())
    )

    extradeco = "-"*(2 + len(projectname))

    print(f"""
--------------{extradeco}
FINAL PRODUCT "{projectname}"
--------------{extradeco}
    """)

    emptydir(projectfolder_TEMP)

    for onedir in sorteddirs:
        print(f'+ Working in src/{onedir.relative_to(source)}')

        contentdir = treeview[TAG_DIR][onedir]

        sorted2analyze, resources = files2analyze(
            onedir   = onedir,
            allfiles = list(contentdir[TAG_FILE])
        )

        for srcfile in sorted2analyze:
            ext = srcfile.suffix[1:]

            print(
                f'   * [{ext.upper()}] Analyzing {srcfile.name}'
            )

        for srcfile in resources:
            print(
                f'   * [RES] Copying {srcfile.name}'
            )

    TODO

    src2dest = {
        'sty': (
            "code",
            projectfolder / f"{projectname}.sty",
        ),
        'tex': (
            "doc",
            tmpdocfolder / f"{projectname}-doc.tex",
        ),
        'cfg': (
            "config",
            None,
        ),
    }

    filesadded = defaultdict(list)

    for onedir in sorteddirs:
        print(f'+ Working in {onedir}')

        contentdir = treeview[TAG_DIR][onedir]

        sorted2analyze = files2analyze(
            onedir   = onedir,
            allfiles = list(contentdir[TAG_FILE])
        )

        for srcfile in sorted2analyze:
            ext = srcfile.suffix[1:]
            kind, destfile = src2dest[ext]

            print(
                f'   * [{ext.upper()}] '
                f'kind.title() file {srcfile.name}'
            )

            with srcfile.open(
                encoding = "utf-8",
                mode = "r"
            ) as f:
                content = f.read()

            with destfile.open(
                encoding = "utf-8",
                mode = "a"
            ) as f:
                f.write('\n')
                f.write(content)


        for srcfile in contentdir[TAG_FILE]:
            if srcfile.suffix[1:] == TAG_CFG_EXT:
                destfile = projectfolder / srcfile.name

                print(
                    f'   * [{TAG_CFG_EXT.upper()}] '
                    f'Config file {srcfile.name}'
                )

                destfile.write_text(
                    encoding = "utf-8",
                    data = srcfile.read_text()
                )
