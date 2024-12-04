from functools import cmp_to_key
from pathlib   import Path
import                subprocess
import                os

from yaml import (
    Dumper,
    dump as yaml_dump
)

from .fulldep import *


# Source: https://reorx.com/blog/python-yaml-tips/
class IndentDumper(Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(IndentDumper, self).increase_indent(flow, False)


class ShortDep():
    CLEANED_DEP = FullDep()

    LEGACY = """
# ----------------------------------------------------------- #
# --      File generated automatically by TeXoptidep.      -- #
# --                                                       -- #
# -- WARNING! The alphabetical order used does not reflect -- #
# -- the order used in the source code.                    -- #
# ----------------------------------------------------------- #
    """.strip()

    def __init__(self, content):
        self.content = content
        self.deps    = None

    def build(self, _):
        data = self.CLEANED_DEP(self.content)

        self.deps = {
            k: sorted(list(data[k]))
            for k in [TAG_CLS, TAG_PACK]
        }

        for kind in [TAG_CLS, TAG_PACK]:
            for name, locset in data[kind].items():
                if not TAG_LIBRARY in locset:
                    continue

                if not TAG_LIBRARY in self.deps:
                    self.deps[TAG_LIBRARY] = {}

                self.deps[TAG_LIBRARY][name] = sorted([
                    libname
                    for libname in locset[TAG_LIBRARY]
                ])


    def save(self, yaml_file):
        self.build(yaml_file)

        yaml_file.touch()

        with yaml_file.open('w') as f:
            yaml_dump(
                self.deps,
                f,
                # indent = 2,
                Dumper=IndentDumper,
                sort_keys=False,
            )

        raw_content = yaml_file.read_text()

        for catego in [TAG_PACK, TAG_LIBRARY]:
            raw_content = raw_content.replace(
                f"\n{catego}:\n",
                f"\n\n{catego}:\n",
            )

        content = f"""
{self.LEGACY}

{raw_content}
        """.strip() + "\n"

        yaml_file.write_text(content)



class VersionDep(ShortDep):
    TEMPLATE_LIST_FILE = r"""
{CLASS}

\documentclass{{minimal}}

{PACKAGE}

\listfiles

\begin{{document}}

LIST FILES

\end{{document}}
    """.strip()


    LEGACY = """
# ---------------------------------------------------------------- #
# --         File generated automatically by TeXoptidep.        -- #
# --                                                            -- #
# -- INFO: the dates are the one found when calling TeXoptidep. -- #
# ---------------------------------------------------------------- #
    """.strip()

    def __init__(self, content):
        super().__init__(content)

    def build(self, yaml_file):
        self.deps = {}

        dirused = yaml_file.parent

        import_cmds = {}

        for cmd, kind in TEX_IMPORT_CMDS.items():
            import_cmds[kind] = cmd

        import_txts = {}

        data = self.CLEANED_DEP(self.content)

        for kind, settings in data.items():
            self.deps[kind] = {
                n: None
                for n in sorted(settings)
            }

            import_txts[kind] = "\n".join([
                f"\\{import_cmds[kind]}{{{n}}}"
                for n in settings
            ])

        tex_code = self.TEMPLATE_LIST_FILE.format(
            CLASS   = import_txts[TAG_CLS],
            PACKAGE = import_txts[TAG_PACK] ,
        )

        tmp_texfile = dirused / "TeXoptidep.listfile.tmp.tex"
        tmp_texfile.touch()
        tmp_texfile.write_text(tex_code)

        _ , _ = self.launch_this(
            ['pdflatex', '-interaction=nonstopmode', str(tmp_texfile)],
            dirused
        )

        stdout, _ = self.launch_this(
            ['texlogsieve', f"{tmp_texfile.stem}.log"],
            dirused
        )

        _ , _ , infos = stdout.partition("*File List*")


        for ext in ['aux', 'log', 'out', 'pdf', 'tex']:
            (tmp_texfile.parent / f"{tmp_texfile.stem}.{ext}").unlink()


        matches = TEXLOG_INFOS_PATTERN.finditer(infos)

        for m in matches:
            if not m[TAG_EXT] in TAG_EXT_2_CATEGO:
                continue

            kind = TAG_EXT_2_CATEGO[m[TAG_EXT]]


            name = m[TAG_NAME]

            if not name in self.deps[kind]:
                continue

            self.deps[kind][name] = m[TAG_DATE].replace("-", "/")


    def launch_this(self, actions, dirused):
        original_dir = os.getcwd()

        try:
            os.chdir(dirused)

            result = subprocess.run(
                actions,
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE,
                text   = True
            )

            if result.returncode != 0:
                COMPIL_RATEE

        except FileNotFoundError:
            PasDePDFLATEX

        finally:
            os.chdir(original_dir)

        return result.stdout, result.stderr
