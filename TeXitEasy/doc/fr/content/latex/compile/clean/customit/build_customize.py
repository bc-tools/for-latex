#! /usr/bin/env python3

from mistool.os_use import PPath

from mistool.latex_use import EXTS_TO_CLEAN, TEMP_EXTS

thisdir = PPath(__file__).parent


# ----------- #
# -- TEXTS -- #
# ----------- #

onetab = ' '*4

texts = {
    'extstoclean': ['EXTS_TO_CLEAN = ['],
    'tempexts': ['TEMP_EXTS = {']
}

for kind, ext in TEMP_EXTS.items():
    texts['extstoclean'] += [
        "# " + kind,
        onetab + str(ext)[1:-1] + ","
    ]

    texts['tempexts'] += [
        onetab + "'" + kind + "': " +str(ext) + ","
    ]

# No final coma...
texts['extstoclean'][-1] = texts['extstoclean'][-1][:-1]
texts['tempexts'][-1] = texts['tempexts'][-1][:-1]

# Let's finish the work.
texts['extstoclean'].append(']')
texts['tempexts'].append('}')

texts['tempexts'] = '\n'.join(texts['tempexts'])
texts['extstoclean'] = '\n'.join(texts['extstoclean'])


# ------------------------ #
# -- UPDATING THE FILES -- #
# ------------------------ #

for onekind, onetext in texts.items():
    ppath = thisdir / '{0}.py'.format(onekind)

    with ppath.open(encoding = "utf-8", mode = "w") as file:
        file.write(onetext)
