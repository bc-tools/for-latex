# un fichier + une classe juste pour BUILD
# buildproj.BuildProj


#!/usr/bin/env python3

# TODO gestion about vs auto


###
# This module implements all the logic needed to manage (La)TeX projects
# developped using a simple standardized workflow: for more informations,
# see the README at the following web adress.
# https://github.com/projetmbc/tools-for-latex/tree/master/TeXfactory
###


from .buildproj import *


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
# This class specializes the class ``Project`` from the package ``src2prod``
# such as to transform a TeXfactory source project into a standard (La)TeX
# project to distribute.
###

class TeXProject(BuildProj):

###
# prototype::
#     opensession  : ``True`` is to reset eveything and open the communication
#                    and ``False`` starts directly the work.
#     closesession : ``True`` is to close the communication and
#                    ``False`` otherwise.
#     safemode     : ``True`` asks to never remove a none empty target folder
#                    contrary to ``False``.
#
# note::
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
