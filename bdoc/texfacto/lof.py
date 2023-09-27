from src2prod import *

def buildlof(
    project,
    source,
    target,
    readme,
    ignore = '',
):
    project = Project(
        project = project,
        source  = source,
        target  = target,
        usegit  = True,
        readme  = readme,
        ignore  = ignore,
    )

    project.build()

    return [f for f in project.lof]
