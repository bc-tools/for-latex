#!/usr/bin/env python3

from typing import Union

from src2prod import (
    Path,
    Project
)

class TeXProject:
###
# prototype::
#     project : the folder project that will be used to communicate during
#               the analysis.
#     source  : the **relative** path of the source dir (regarding the project
#               folder).
#     target  : the **relative** path of the final product dir (regarding the
#               project folder).
#     ignore  : if a string is used then this gives the rules for ignoring
#               files in addition to what ¨git does.
#               If an instance of ``Path`` is used, thent we have a file
#               containing the rules.
#     usegit  : ``True`` asks to use ¨git contrary to ``False``.
#     readme  : ``None`` is if you don't need to import an external
#               path::``README`` file, otherwise give a **relative** path.
#
# warning::
#     The target folder is totally removed and reconstructed at each new
#     update.
#
# info::
#     Additional attributes are created/reseted by the method ``reset``.
###
    def __init__(
        self,
        project: Union[str, Path],
        source : Union[str, Path],
        target : Union[str, Path],
        ignore : Union[str, Path]       = '',
        usegit : bool                   = False,
        readme : Union[None, str, Path] = None,
    ) -> None:
        self.src2prod_project = Project(
            project = project,
            source  = source,
            target  = target,
            ignore  = ignore,
            usegit  = usegit
        )

    def build(self):
        self.src2prod_project.build()

        self.lof_sty_src = []
        self.lof_tex_src = []

        for p in self.src2prod_project.lof:
            relpath = p.relative_to(self.src2prod_project.source)

            if len(relpath.parents) - 1 == 1:
                if relpath.suffix == '.sty':
                    self.lof_sty_src.append(p)

                elif relpath.suffix == '.tex':
                    self.lof_tex_src.append(p)
