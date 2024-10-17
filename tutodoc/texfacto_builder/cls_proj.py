from .constants import *
from .misc      import *


# --------------------------- #
# -- BUILD SINGLE STY FILE -- #
# --------------------------- #

def prebuild_single_cls(
    source,
    temp_dir,
    sorted_useful_files,
    dev_lang,
    other_lang,
    versions
):
    for onedir, srcfile, kind in iter_sorted_useful_files(
        source              = source,
        sorted_useful_files = sorted_useful_files,
        ext_wanted          = TAG_CLS
    ):
        if kind == TAG_FILE:
            print(f"   * Analyzing ''{srcfile.name}''")

            pieces = extract_from_DEV_CLS(srcfile)
            prepare_CLS(onedir, temp_dir, *pieces)

        else:
            print(f"   * [RES-CLS] Copying ''{srcfile.name}'")

            copyfromto(
                srcfile  = srcfile,
                destfile = temp_dir / srcfile.name
            )

    print()
    print(
        f"+ ''{temp_dir.parent.name}/{temp_dir.name}'' "
         "folder OK for the ''CLS'' file."
    )


def extract_from_DEV_CLS(srcfile):
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

        if shortline == TAG_MC_PACKAGES:
            store_in = store_import
            continue

        if shortline == TAG_MC_OPTIONS:
            store_in = store_options
            continue

        if shortline == TAG_MC_TOOLS:
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


def prepare_CLS(
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
            destfile = tmpdir / TAG_TMP_CLS_IMPORT
        )

    if pack_options:
        pack_options += '\n'*3

        addcontentto(
            content  = pack_options,
            destfile = tmpdir / TAG_TMP_CLS_OPTIONS
        )

    if pack_src:
        pack_src = pack_src.replace(
            f"\\input{{../{curdir.name}/",
             "\\input{"
        )

        pack_src += '\n'*3

        addcontentto(
            content  = pack_src,
            destfile = tmpdir / TAG_TMP_CLS_SRC
        )
