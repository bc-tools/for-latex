from pathlib import Path
from yaml   import safe_load

from semver.version import Version

from .constants import *


# --------------------- #
# -- BUILD METADATAS -- #
# --------------------- #

def build_metadata(project_dir):
    metadata = {}

    proj_about = project_dir / "about.yaml"

    if not proj_about.is_file():
        raise IOError("missing an ''about.yaml'' for the project")


    with proj_about.open(
        encoding='utf8',
        mode='r',
    ) as f:
        about_cfg = safe_load(f)

    gene_cfg = about_cfg["general"]

    metadata = {
        TAG_AUTHOR  : gene_cfg["author"],
        TAG_DOC_LANG: gene_cfg["lang"]["doc"],
    }

    metadata[TAG_PROJ_DIR]  = project_dir
    metadata[TAG_MANUALS]   = project_dir / "contrib" / "doc" / "manual"
    metadata[TAG_PROJ_NAME] = project_dir.name
    metadata[TAG_ROLLOUT]   = project_dir / "rollout"
    metadata[TAG_SRC]       = project_dir / "src"
    metadata[TAG_TEMP]      = project_dir / f".{metadata[TAG_PROJ_NAME]}"

    metadata[TAG_ALL_VERSIONS] = about_stable_version(project_dir)
    metadata[TAG_LAST_VERSION] = last_version(metadata[TAG_ALL_VERSIONS])

    metadata[TAG_CREATION] = creation(metadata[TAG_ALL_VERSIONS])

    return metadata



def about_stable_version(project_dir):
    stable_chges_dir = project_dir / 'changes' / 'stable'

    stable_versions = {}

    for month_file in stable_chges_dir.glob("*/*.txt"):
        year  = month_file.parent.name
        month = month_file.stem

        content = month_file.read_text()

        match = re.search(DATE_PATTERN, content)

        if match:
            day     = match.group(1)
            version = match.group(2)

            stable_versions[version] = {
                TAG_DAY  : day,
                TAG_MONTH: month,
                TAG_YEAR : year,
            }

    stable_versions_revsorted = []

    all_nb_versions = [
        Version.parse(v)
        for v in stable_versions
    ]

    all_nb_versions.sort(reverse = True)

    for v in all_nb_versions:
        v = str(v)

        stable_versions_revsorted.append(
            {v: stable_versions[v]}
        )

    return stable_versions_revsorted



def version_n_date(dict_vd):
    for v, d in dict_vd.items():
        return {
            TAG_VERSION: v,
            TAG_DATE   : d,
        }


def last_version(stable_versions):
    for vd in stable_versions:
        break

    return version_n_date(vd)


def creation(stable_versions):
    for vd in stable_versions:
        ...

    return version_n_date(vd)
