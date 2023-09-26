from yaml import safe_load

from src2prod import *

PROJECT_DIR = Path(__file__).parent
SOURCE_DIR  = PROJECT_DIR / Path('src')
TARGET_DIR  = PROJECT_DIR.parent / PROJECT_DIR.name.lower()

# Fichires souhaités
project = Project(
    project = PROJECT_DIR,
    source  = Path('src'),
    target  = TARGET_DIR,
    usegit  = True,
    readme  = Path('README.md'),
    # ignore = '',
)

project.build()

allfiles = [f for f in project.lof]

# Gestion de l'ordre


def buildtoc(aboutfile):
    with aboutfile.open(
        encoding='utf8',
        mode='r',
    ) as f:
        about_cfg = safe_load(f)

    print(about_cfg['toc'])

src_about = SOURCE_DIR / "about.yaml"

if src_about in allfiles:
    toc = buildtoc(src_about)

# Gestion des sty


for f in allfiles:
    if f.suffix == ".sty":
        print(f.name)
