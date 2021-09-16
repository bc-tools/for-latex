#!/usr/bin/env python3

# TODO  NELLE ORGA !!!!

# TODO gestion about vs auto


###
# This module implements all the logic needed to manage (La)TeX projects
# developped using a simple standardized workflow: for more informations,
# see the README at the following web adress.
# https://github.com/projetmbc/tools-for-latex/tree/master/TeXfactory
###


from src2prod import *


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

class BuildProj(Project):
    TAG_ASIT = "to copy verbatim"

    TAG_ABOUT    = "about.peuf"
    TAG_STY      = "sty (for the final STY)"
    TAG_TEX      = "tex (for the final doc)"
    TAG_XTRA_PDF = "PDF to ignore (dev doc)"

    TAG_CHANGES   = "changes (for the final doc)"
    SRC_DIR_CHGES = "changes"


###
# This method resets everything with a personalized main title.
###
    def reset(self) -> None:
        super().reset(
            kind = 'SOURCE --[[ TeXfactory ]]--> FINAL PRODUCT'
        )


###
# prototype::
#     opensession  : ``True`` is to reset eveything and open the communication
#                    and ``False`` starts directly the work.
#     closesession : ``True`` is to close the communication and
#                    ``False`` otherwise.
#
#
# This method is the great bandleader building the lists of files to use to update
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
            self.TAG_ABOUT   : [],
            self.TAG_STY     : [],
            self.TAG_TEX     : [],
            self.TAG_XTRA_PDF: [],
            self.TAG_ASIT    : [],
            self.TAG_CHANGES : [],
        }

        self._maxlentag = max(len(k) for k in self._lof_catego)

        self._src_dirs: Set(Path) = set()

# Do we open the session?
        if opensession:
            self._start_one_session(
                timer_title = 'build',
                title       = f'"{self.project.name}": LISTS OF FILES',
            )

# Let's work.
        for name in [
            'build_lof_catego',
            'sort_spe_lofs',
        ]:
            getattr(self, name)()

            if not self.success:
                break

# Do we close the session?
        if closesession:
            self._close_one_session(timer_title = 'build')

###
# This method build four lists stored in the dictionary ``self._lof_catego`` and
# also the set ``self._src_dirs``.
#
#     1) A list of about.peuf fiiles found inside the source dir or a direct
#        subfolder of the source dir.
#
#     1) A list of the ``STY`` files to use to make the main single ``STY`` file
#        of the final product.
#
#     1) A list of the ``TEX`` files to use to make the doc of the final product.
#
#     1) A list of the ``PDF`` files to ignore because they are just the result
#        of the (La)TeX compilation of ``TEX`` files write to documentate the
#        project during its development (see the preceding item).
#
#     1) A list of the files to copy "directly" in the folder of the final product.
#
#     1) An additional set ``self._src_dirs`` contains the direct subfolders
#        containing the ``STY`` and ``TEX`` files needed to build the final product
#        and its docu.
###
    def build_lof_catego(self) -> None:
# Let ``src2prod.Project`` do the main work.
        super().build(
            opensession  = False,
            closesession = False,
        )

        if not self.success:
            return

# Let's gather files by category and also find the direct useful subfolders.
        nb_pdfs_ignored = 0

        for p in self.lof:
            relpath    = p.relative_to(self.source)
            reldepth   = len(relpath.parents) - 1

            if self.is_info_change(relpath):
                self._lof_catego[self.TAG_CHANGES].append(p)
                continue

            elif (
                relpath.name == 'about.peuf'
                and
                reldepth <= 1
            ):
                self._lof_catego[self.TAG_ABOUT].append(p)
                continue

            elif reldepth == 1:
                suffix = relpath.suffix

                if suffix == '.sty':
                    self._lof_catego[self.TAG_STY].append(p)
                    self._src_dirs.add(p.parent)
                    continue

                elif suffix == '.tex':
                    self._lof_catego[self.TAG_TEX].append(p)
                    self._src_dirs.add(p.parent)
                    continue

                elif self.pdf_to_ignore(p):
                    self._lof_catego[self.TAG_XTRA_PDF].append(p)
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
            plurial  = ""   if nbpaths <= 1 else "s"

            xspace = " "*(self._maxlentag - len(kind))

            self.recipe(
                {VAR_STEP_INFO:
                    f'"{kind}"{xspace}: '
                    f'{nb_or_no} file{plurial} found.',
                 VAR_LEVEL: 1}
            )

            if kind == self.TAG_ASIT and nb_pdfs_ignored != 0:
                if nb_pdfs_ignored == 1:
                    plurial = ""
                    verb    = "has"

                else:
                    plurial = "s"
                    verb    = "have"

###
# prototype::
#     path : just a path
#
#     :return: ``True`` if the path points to a ¨tex file used to indicate a change
#              about a new version, and ``False`` otherwise.
###
    def is_info_change(self, path: Path) -> bool:
        parents = list(path.parents)

        return (
            len(parents) == 4
            and
            str(parents[-2]) == self.SRC_DIR_CHGES
        )

###
# prototype::
#     path : just a path
#
#     :return: ``True`` if the path points to a ¨pdf file used in the source
#              dir to write a part of the final ¨docu, and ``False`` otherwise.
###
    def pdf_to_ignore(self, path: Path) -> bool:
        pathname = path.name

        for onelang in ALL_LANGS:
            if pathname.endswith(f'-{onelang}.pdf'):
                return True

        return False

###
# This method sorts the lists of changes, of ``STY`` files and ``TEX`` files
# such as to obtain easily the good docu and final main ``STY`` file.
###
    def sort_spe_lofs(self) -> None:
# Let's talk a little...
        self.recipe(
            {VAR_STEP_INFO:
                'Sorting specific lists used for '
                'the final STY file and the doc.'}
        )

# Sort the list of changes.
        if self._lof_catego[self.TAG_CHANGES]:
            self._lof_catego[self.TAG_CHANGES].sort(reverse = True)
            print(self._lof_catego[self.TAG_CHANGES])

            self.recipe(
                {VAR_STEP_INFO:
                    f'Changes: files sorted (antichronologic order).',
                VAR_LEVEL: 1}
            )

# Sort the list of ``STY`` and ``TEX`` files.
#
# We just have to take care of ``about.peuf`` files.
        print(self.source)
        exit()



###
# prototype::
#     folder : the path of a folder to "sort" by taking care of a possible
#              ``about.peuf`` file.
#
#     :return:
###
    def recsort_sty_tex_lofs(self, folder: Path) -> List[Path]:
        ...
