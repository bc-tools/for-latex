from functools import cmp_to_key

from yaml import (
    Dumper,
    dump as yaml_dump
)

from .check import *

def _special_compare(v1, v2):
    if isinstance(v1, dict):
        v1 = list(v1)[0]

    if isinstance(v2, dict):
        v2 = list(v2)[0]

    if v1 > v2:
        return 1

    if v1 < v2:
        return -1

    return 0


# Source: https://reorx.com/blog/python-yaml-tips/
class IndentDumper(Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(IndentDumper, self).increase_indent(flow, False)


class ExtractDep():
    CLEANED_DEP = CleanedDep()

    def __init__(self, content):
        self.content = content

    def build(self):
        return self.CLEANED_DEP(self.content)

    def save(self, yaml_file):
        data = self.build()

        report = {
            k: self._sort_this(data[k])
            for k in [TAG_CLS, TAG_PACK]
        }

        yaml_file.touch()

        with yaml_file.open('w') as f:
            yaml_dump(
                report,
                f,
                # indent = 2,
                Dumper=IndentDumper,
                sort_keys=False,
            )

        raw_content = yaml_file.read_text()

        raw_content = raw_content.replace(
            "\npackages:\n",
            "\n\npackages:\n",
        )

        content = f"""
# ------------------------------------------------- #
# -- File generated automatically by TeXoptidep. -- #
# --                                             -- #
# -- The classes, the packages, and the option   -- #
# -- settings are sorted alphabetically.         -- #
# ------------------------------------------------- #

{raw_content}
        """.strip() + "\n"

        yaml_file.write_text(content)



    def _sort_this(self, data):
        for i, val in enumerate(data):
            if isinstance(val, dict):
                name = list(val)[0]

                val[name][TAG_OPTIONS].sort()

        data = sorted(
            data,
            key = cmp_to_key(_special_compare)
        )

        return data
