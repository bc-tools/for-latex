from .constants import *
from .misc      import *


# --------------------------- #
# -- BUILD SINGLE STY FILE -- #
# --------------------------- #

def build_single_sty(
    source,
    temp_dir,
    sorted_useful_files
):
    for onedir, srcfile, kind in iter_sorted_useful_files(
        source              = source,
        sorted_useful_files = sorted_useful_files,
        ext_wanted          = TAG_STY
    ):
        if kind == TAG_FILE:
            print(f"   * Analyzing ''{srcfile.name}''")

            pieces = extractfrom_STY(srcfile)
            prepare_STY(onedir, temp_dir, *pieces)

        else:
            print(f"   * [RES-STY]")
            print(f"       -> Copying ''{srcfile.name}'")

            copyfromto(
                srcfile  = srcfile,
                destfile = temp_dir / srcfile.name
            )

    print()
    print(
        f"+ ''{temp_dir.parent.name}/{temp_dir.name}'' "
         "folder OK for the ''STY'' file."
    )


def extractfrom_STY(srcfile):
    with srcfile.open(
        encoding = "utf-8",
        mode     = "r"
    ) as f:
        content = f.read()

    pack_import  = []
    pack_options = []
    pack_src     = []

    store_import  = "import"
    store_options = "options"
    store_src     = "src"
    store_ignore  = "ignore"
    store_in      = store_ignore

    for oneline in content.split('\n'):
        shortline = oneline.strip()

        if shortline == '% == PACKAGES == %':
            store_in = store_import
            continue

        if shortline == '% == OPTIONS == %':
            store_in = store_options
            continue

        if shortline == '% == TOOLS == %':
            store_in = store_src
            continue

        if store_in == store_import:
            pack_import.append(oneline)

        elif store_in == store_options:
            pack_options.append(oneline)

        elif store_in == store_src:
            pack_src.append(oneline)

    pack_import = '\n'.join(pack_import)
    pack_import = pack_import.strip()

    pack_options = '\n'.join(pack_options)
    pack_options = pack_options.strip()

    pack_src = '\n'.join(pack_src)
    pack_src = pack_src.strip()

    return pack_import, pack_options, pack_src


def prepare_STY(
    curdir,
    tmpdir,
    pack_import,
    pack_options,
    pack_src
):
    if pack_import:
        pack_import += '\n'*3

        addcontentto(
            content  = pack_import,
            destfile = tmpdir / '.tmp_pack_import.sty'
        )

    if pack_options:
        pack_options += '\n'*3

        addcontentto(
            content  = pack_options,
            destfile = tmpdir / '.tmp_pack_options.sty'
        )

    if pack_src:
        pack_src = pack_src.replace(
            f"\\input{{../{curdir.name}/",
             "\\input{"
        )

        pack_src += '\n'*3

        addcontentto(
            content  = pack_src,
            destfile = tmpdir / '.tmp_pack_src.sty'
        )
