from yaml import (
    Dumper,
    dump as yaml_dump
)

from .check import *

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
        yaml_file.touch()

        with yaml_file.open('w') as f:
            yaml_dump(
                self.build(),
                f,
                # indent = 2,
                Dumper=IndentDumper,
                sort_keys=False,
            )
