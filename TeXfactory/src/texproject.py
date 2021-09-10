#!/usr/bin/env python3

from typing import Union

from src2prod import *


class TeXProject(Project):

# TODO gestion about vs auto
    def build(self):
        self.recipe(
                {VAR_TITLE: 'TeX Factory'},
            FORTERM,
                {VAR_STEP_INFO:
                     'The log file used will be :'
                     '\n'
                    f'"{self.logfile}".'},
        )
# Let's work.
        for name in [
            'build_all_lofs'
        ]:
            getattr(self, name)()

            if not self.success:
                break


    def build_all_lofs(self):
        super().build(
            opensession  = False,
            closesession = False,
        )

        if not self.success:
            return

        self.lof_sty_src = []
        self.lof_tex_src = []
        self.lof_about   = []

        for p in self.lof:
            relpath = p.relative_to(self.source)

            if relpath.name == 'about.peuf':
                self.lof_about.append(p)

            elif len(relpath.parents) - 1 == 1:
                if relpath.suffix == '.sty':
                    self.lof_sty_src.append(p)

                elif relpath.suffix == '.tex':
                    self.lof_tex_src.append(p)


        self.reset()

        self.recipe(
                {VAR_TITLE: 'XXXX'},
            FORTERM,
                {VAR_STEP_INFO:
                     'OOO.'},
        )
