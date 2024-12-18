#! /usr/bin/env python3

from pathlib import Path
import              sys


# ------------------------------------ #
# -- MODULES IMPORTED FROM SOURCES! -- #
# ------------------------------------ #

def addfindsrc(
    file   : str,
    project: str,
) -> Path:
    project_dir = Path(file).parent
    rootdir     = Path('/')

    while(
        project_dir != rootdir
        and
        project_dir.name != project
    ):
        project_dir = project_dir.parent

    assert project_dir.name == project, \
          (
            'call the script from a working directory '
            'containing the project dir.'
          )

    sys.path.append(str(project_dir))

    return project_dir


MODULE_DIR = addfindsrc(
    file    = __file__,
    project = 'TeXoptidep',
)


# -------------- #
# -- LET'S GO -- #
# -------------- #

from src import *

tutodoc_src_dir = Path(__file__)

while tutodoc_src_dir.name != "for-latex":
    tutodoc_src_dir = tutodoc_src_dir.parent

tutodoc_src_dir = tutodoc_src_dir / "tutodoc" / "src"

yaml_file = tutodoc_src_dir / "DEPENDS-VERSIONS.yaml"

content = tutodoc_src_dir / "main" / "main.cls"
content = content.read_text()

extractdep = VersionDep(content = content)
extractdep.save(yaml_file)
