from src2prod import *


project = Project(
    project = Path(__file__).parent,
    source  = Path('src'),
    target  = Path('bdoc'),
    usegit  = True,
    readme  = Path('README.md'),
    # ignore = '',
)

project.build()

for f in project.lof:
    if f.suffix == ".yaml":
        print(f)
