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

    def _final_options_n_version(
        self,
        infos
    ):
        settings = {}
        options  = {}
        version  = None

        for oneinfo in infos:
            if oneinfo[TAG_VERSION]:
                if (
                    len(oneinfo[TAG_VERSION]) > 1
                    or
                    not version is None
                ):
                    TODO_PB

                version = oneinfo[TAG_VERSION][0]

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
