#!/usr/bin/env python3

from src2prod import *


PROJECT_DIR = Path("/Users/projetmbc/Google Drive/git[NEW]/coding/tools/for-latex") / 'bdoc'

project = Project(
    project = PROJECT_DIR,
    source  = PROJECT_DIR / 'src',
    target  = '',
    ignore  = '''
        tool_*/
        tool_*.*

        test_*/
        test_*.*
    ''',
    usegit = True
)

project.build()

print('---')

for f in project.lof:
    print(f)
