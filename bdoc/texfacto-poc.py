from src2prod import *

PROJECT_DIR = Path(__file__).parent
TARGET_DIR  = PROJECT_DIR.parent / PROJECT_DIR.name.lower()

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
allfiles.sort()

for f in allfiles:
    print(f.name)

    # if f.suffix == ".yaml":
    #     print(f)
