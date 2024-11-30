from copy   import deepcopy
from typing import *

from .config.texcmds import *
from .config.tags    import *


class LazyExtractDep:
    def __init__(self):
        self._content        = None
        self._useful_content = None
        self._data           = None

    def __call__(
        self,
        content: str
    ):
        self._content = content
        self._data    = {}

        self._build_short_content()
        self._extract_cmd_actions()
        self._extract_cls_pass_opts()

        return self._data


    def _build_short_content(self):
        self._useful_content = []

        for line in self._content.split("\n"):
            short_line = line.strip()

            if not short_line or short_line.startswith("%"):
                continue

            self._useful_content.append(line)

        self._useful_content = "\n".join(self._useful_content)


    def get_keyval_options(
        self,
        options: str
    ) -> List[str]:
        dict_options = {}

        for oneopt in options.split(","):
            oneopt = oneopt.strip()

            if "=" in oneopt:
                key, _, val = oneopt.partition("=")

                key = key.strip()
                val = val.strip()

            else:
                key, val = oneopt, None

            dict_options[key] = val

        return dict_options


    def _extract_cmd_actions(self):
        matches = IMPORT_PATTERN.finditer(self._useful_content)

        setup_libs_or_opts = {}
        std_imports        = {
            k: {}
            for k in TEX_IMPORT_CMDS.values()
        }

        for m in matches:
            kind = m["kind"].strip()

    # Library import / Setup options lately.
            if kind in TEX_SETUP_LIBS_OR_OPTS_CMDS:
                last_settings = setup_libs_or_opts.get(kind, {})
                this_settings = self.get_keyval_options(m["name"])

                for k, v in this_settings.items():
                    if k in last_settings:
                        last_settings[k].append(v)

                    elif not v is None:
                        last_settings[k] = [v]

                    else:
                        last_settings[k] = []


                setup_libs_or_opts[kind] = last_settings

                continue

    # Standard import.
            kind = TEX_IMPORT_CMDS[kind]

            thisname = m["name"].strip()
            thismeta = {
                TAG_OPTIONS: [],
                TAG_DATE   : [],
            }

            for x in [TAG_OPTIONS, TAG_DATE]:

                if x == TAG_DATE:
                    print(f"{ m[0]=}")

                if not m[x] is None:
                    thismeta[x].append(
                        m[x].strip()
                        if x == TAG_DATE else
                        self.get_keyval_options(m[x])
                    )

            if thisname in std_imports[kind]:
                std_imports[kind][thisname].append(thismeta)

            else:
                std_imports[kind][thisname] = [thismeta]

    # Job done!
        self._data[TAG_IMPORTS]     = std_imports
        self._data[TAG_SETUP] = setup_libs_or_opts


    def _extract_cls_pass_opts(self):
        setup_cls_opts = {}

# Loding options for classes.
        matches = CLASS_OPTS_PASSED_PATTERN.finditer(self._useful_content)

        for m in matches:
            name = m["name"].strip()

            if not name in self._data[TAG_IMPORTS][TAG_CLS]:
                raise ValueError(f"class '{name}' not loaded!")

            last_settings = setup_cls_opts.get(name, [])
            this_settings = self.get_keyval_options(m["options"])

            last_settings.append(this_settings)

            setup_cls_opts[name] = last_settings

    # Job done!
        self._data[TAG_SETUP][TAG_CLS_PASS_OPTS] = setup_cls_opts
