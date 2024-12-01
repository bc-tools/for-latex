from .lazy_extract import *


class CleanedDep(LazyExtract):
    def __call__(
        self,
        content: str
    ):
        super().__call__(content)

        self._finalize()

        return self._data

    def _finalize(self):
# Standard imports.
        self._data = {
            k: []
            for k in self._raw_data[TAG_IMPORTS]
        }

        for kind, tools in self._raw_data[TAG_IMPORTS].items():
            for name, infos in tools.items():
                settings = self._final_options_n_version(infos)

                if settings:
                    self._data[kind].append({
                        name: settings
                    })

                else:
                    self._data[kind].append(name)

# Pass options to classes.
        for clsname, clsopts in self._raw_data[TAG_SETUP][TAG_CLS_PASS_OPTS].items():
            self._add_to(
                clsname,
                {TAG_OPTIONS: clsopts},
                self._data[TAG_CLS],
            )

# Extra option settings.
        for cmd in self._raw_data[TAG_SETUP]:
            if cmd == TAG_CLS_PASS_OPTS:
                continue

            kind, _, parent_cmd = TEX_SETUP_CMDS[cmd].partition(':')
            kind = TAG_CMD_SET_ABREVS[kind]
            print(f"{cmd=} ; {parent_cmd}[{kind}]",)

        # from pprint import pprint;pprint(self._raw_data[TAG_SETUP]);exit()

    def _final_options_n_version(
        self,
        infos
    ):
        settings = {}
        options  = {}
        version  = None

        for oneinfo in infos:
            if (
                TAG_VERSION in oneinfo
                and
                oneinfo[TAG_VERSION]
            ):
                if (
                    len(oneinfo[TAG_VERSION]) > 1
                    or
                    not version is None
                ):
                    TODO_PB

                version = oneinfo[TAG_VERSION][0]


            if TAG_OPTIONS in oneinfo:
                for someopts in oneinfo[TAG_OPTIONS]:
                    for opt, val in someopts.items():
                        if opt in options:
                            TODO_PB

                        options[opt] = val

        if version:
            settings[TAG_VERSION] = version

        if options:
            final_options = []

            for k, v in options.items():
                if v is None:
                    final_options.append(k)

                else:
                    final_options.append(f"{k} = {v}")

            settings[TAG_OPTIONS] = final_options

        if not settings:
            settings = None

        return settings

    def _add_to(
        self,
        name,
        what,
        data,
    ):
        for i, iname in enumerate(data):
            if iname == name:
                data[i] = {
                    name: self._final_options_n_version([what])
                }

                break

            else:
                TODO
