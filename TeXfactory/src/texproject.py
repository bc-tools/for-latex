#!/usr/bin/env python3

###
# This module ...
###


from typing import Union

from src2prod import *

# TODO gestion about vs auto


# --------------- #
# -- CONSTANTS -- #
# --------------- #

ALL_LANGS = [
    "EN",
    "FR",
]


# ------------------------ #
# -- PROJECT MANAGEMENT -- #
# ------------------------ #

###
# prototype::
#     :see: src2prod.Project
#
# This class ...
###

class TeXProject(Project):
    TAG_ASIT  = "asit"
    TAG_STY   = "sty"
    TAG_TEX   = "tex"
    TAG_ABOUT = "about"

###
# prototype::
#     opensession  : ``True`` is to reset eveything and open the communication
#                    and ``False`` starts directly the work.
#     closesession : ``True`` is to close the communication and
#                    ``False`` otherwise.
#     safemode     : ``True`` asks to never remove a none empty target folder
#                    contrary to ``False``.
#
# info::
#     The argument ``safemode`` is here to leave the responsability of
#     removing a none empty folder to the user (my lawyers forced me to
#     add this feature).
###
    def update(
        self,
        opensession : bool = True,
        closesession: bool = True,
        safemode    : bool = True
    ) -> None:
        TODO


###
# prototype::
#     opensession  : ``True`` is to reset eveything and open the communication
#                    and ``False`` starts directly the work.
#     closesession : ``True`` is to close the communication and
#                    ``False`` otherwise.
#
#
# This method is the great bandleader building the list of files to be copied to
# the target dir.
###
    def build(
        self,
        opensession : bool = True,
        closesession: bool = True,
    ) -> None:
# Our specific attributes.
        self._lof_catego: Dict(str, List(Path)) = {
# The order of the keys is useful for the printings...
            self.TAG_ABOUT: [],
            self.TAG_STY  : [],
            self.TAG_TEX  : [],
            self.TAG_ASIT : [],
        }

        self._maxlentag = max(len(k) for k in self._lof_catego)

# Do we open the session?
        if opensession:
            self.recipe(
                {VAR_TITLE:
                    f'"{self.project.name}": SOURCE '
                    ' --[[ TeXfactory ]]--> '
                    'FINAL PRODUCT'},
            )

            self.timestamp('start')

            self.recipe(
                FORTERM,
                    ('The log file used will be :'
                    '\n'
                    f'"{self.logfile}".'),
                    NL,
            )

# Let's work.
        for name in [
            'build_all_lofs',
            # 'sort_sty_n_doc_lofs',
            # 'build_final_sty',
            # 'build_final_doc',
        ]:
            getattr(self, name)()

            if not self.success:
                break

# Do we close the session?
        if closesession:
            self._close_one_session(timer_title = 'build')

###
# ????
###
    def build_all_lofs(self) -> None:
# Let's talk.
        self.recipe(
            {VAR_TITLE: f'SEARCHING FOR SOURCE FILES'},
        )

# Let ``src2prod.Project`` do the main work.
        super().build(
            opensession  = False,
            closesession = False,
        )

        if not self.success:
            return

        for p in self.lof:
            relpath  = p.relative_to(self.source)
            reldepth = len(relpath.parents) - 1

            if (
                relpath.name == 'about.peuf'
                and
                reldepth <= 1
            ):
                self._lof_catego[self.TAG_ABOUT].append(p)
                continue

            elif reldepth == 1:
                if relpath.suffix == '.sty':
                    self._lof_catego[self.TAG_STY].append(p)
                    continue

                elif relpath.suffix == '.tex':
                    self._lof_catego[self.TAG_TEX].append(p)
                    continue

                elif self.pdf_to_ignore(p):
                    continue

            self._lof_catego[self.TAG_ASIT].append(p)

# We indicate the number of files found by category.
        self.recipe(
            {VAR_STEP_INFO:
                "Number of files found by category."}
        )

        for kind, paths in self._lof_catego.items():
            nbpaths = len(paths)

            nb_or_no = "no" if nbpaths == 0 else nbpaths
            plurial  = "" if nbpaths <= 1 else "s"

            xspace = " "*(self._maxlentag - len(kind))

            xtra = (
                " (PDF parts of the doc are ignored)"
                if kind == self.TAG_ASIT else
                ""
            )

            self.recipe(
                {VAR_STEP_INFO:
                    f'"{kind}"{xspace}: '
                    f'{nb_or_no} file{plurial} found{xtra}.',
                 VAR_LEVEL: 1}
            )


###
# prototype::
#     path : just a path
#
#     :return: ``True`` if the path points to a ¨pdf file used in source
#              to write a part of the final ¨docu and ``False`` otherwise.
###
    def pdf_to_ignore(self, path: Path) -> bool:
        pathname = path.name

        for onelang in ALL_LANGS:
            if pathname.endswith(f'-{onelang}.pdf'):
                return True

        return False
