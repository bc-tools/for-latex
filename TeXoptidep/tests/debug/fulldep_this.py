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

content = Path(__file__)

while content.name != "for-latex":
    content = content.parent

content = content / "tutodoc" / "src" / "main" / "main.cls"
content = content.read_text()

fulldep = FullDep()
data    = fulldep(content = content)

from pprint import pprint
print()
print("data:")
pprint(data)
