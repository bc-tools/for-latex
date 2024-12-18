from .lazyextract import *


class FullDep(LazyExtract):
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
            k: {}
            for k in self._raw_data[TAG_IMPORT]
        }

        for kind, tools in self._raw_data[TAG_IMPORT].items():
            for name, infos in tools.items():
                settings = self._final_options_n_co(infos)

                self._data[kind][name] = settings

# Pass options to classes.
        for clsname, clsopts in self._raw_data[TAG_SETUP][TAG_CLS_PASS_OPT].items():
            self._add_to(
                clsname,
                {
                    TAG_OPTION: clsopts
                },
                self._data[TAG_CLS],
            )

# Extra option settings.
        for cmd, settings in self._raw_data[TAG_SETUP].items():
            if cmd == TAG_CLS_PASS_OPT:
                continue

            kind, _, parent_cmd = TEX_SETUP_CMDS[cmd].partition(':')
            kind = TAG_CMD_SET_ABREVS[kind]

            self._add_to(
                parent_cmd,
                {kind: settings},
                self._data[TAG_PACK],
            )

    def _final_options_n_co(
        self,
        infos
    ):
        settings = {}

        for oneinfo in infos:
# Version.
            version = oneinfo.get(TAG_VERSION, [])

            if version:
                if (
                    TAG_VERSION in settings
                    or
                    len(version) > 1
                ):
                    raise ValueError(
                        f"illegal version. See below:\n{version}"
                    )

                settings[TAG_VERSION] = version

# Options or libraries.
            for tag in [TAG_OPTION, TAG_LIBRARY]:
                tag_set = oneinfo.get(tag, [])

                if not tag_set:
                    continue

                if not tag in settings:
                    settings[tag] = {}

                for some_settings in tag_set:
                    for k, v in some_settings.items():
                        if k in settings[tag]:
                            raise ValueError(
                                f"{tag} used at least twice"
                                f"See below:\n{opt}"
                            )

                        settings[tag][k] = v

        return settings


    def _add_to(
        self,
        name,
        what,
        data,
    ):
        if not name in data:
            raise ValueError(
                f"settings for unknown '{name}'."
            )

        data[name] = self._final_options_n_co([what])
