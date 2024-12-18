from copy   import deepcopy
from typing import *

from .config.texcmds import *
from .config.tags    import *


class LazyExtract:
    def __call__(
        self,
        content: str
    ):
        self.content   = content
        self._raw_data = {}

        self._build_short_content()
        self._extract_cmd_actions()
        self._extract_cls_pass_opts()

        return self._raw_data


    def _build_short_content(self):
        self._useful_content = []

        for line in self.content.split("\n"):
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

        setup_cmds  = {}
        std_imports = {
            k: {}
            for k in TEX_IMPORT_CMDS.values()
        }

        for m in matches:
            kind = m["kind"].strip()

# Library import / Setup options lately.
            if kind in TEX_SETUP_CMDS:
                last_settings = setup_cmds.get(kind, [])
                last_settings.append(self.get_keyval_options(m["name"]))

                setup_cmds[kind] = last_settings

                continue

# Standard import.
            kind = TEX_IMPORT_CMDS[kind]

            this_name = m["name"].strip()

            this_meta = {
                TAG_OPTION: [],
                TAG_VERSION   : [],
            }

            for x in [TAG_OPTION, TAG_VERSION]:
                if not m[x] is None:
                    this_meta[x].append(
                        m[x].strip()
                        if x == TAG_VERSION else
                        self.get_keyval_options(m[x])
                    )

            if this_name in std_imports[kind]:
                std_imports[kind][this_name].append(this_meta)

            else:
                std_imports[kind][this_name] = [this_meta]

# Job done!
        self._raw_data[TAG_IMPORT] = std_imports
        self._raw_data[TAG_SETUP]   = setup_cmds


    def _extract_cls_pass_opts(self):
        setup_cls_opts = {}

# Loading options for classes.
        matches = CLASS_OPTS_PASSED_PATTERN.finditer(self._useful_content)

        for m in matches:
            name = m["name"].strip()

            if not name in self._raw_data[TAG_IMPORT][TAG_CLS]:
                raise ValueError(f"class '{name}' not loaded!")

            last_settings = setup_cls_opts.get(name, [])
            this_settings = self.get_keyval_options(m[TAG_OPTION])

            last_settings.append(this_settings)

            setup_cls_opts[name] = last_settings

# Job done!
        self._raw_data[TAG_SETUP][TAG_CLS_PASS_OPT] = setup_cls_opts
