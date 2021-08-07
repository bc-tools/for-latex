#! /usr/bin/env python3

from collections import defaultdict

from mistool.os_use     import DIR_TAG, FILE_TAG, PPath
from mistool.string_use import between
from orpyste.data       import ReadBlock


# -------------------------------- #
# -- ONLY TOOLS FOR THE SOURCES -- #
# -------------------------------- #

# Esay-to-update configuration.

THIS_FILE = PPath(__file__)
FILE_PY   = THIS_FILE.parent / THIS_FILE.name.replace('tool_', '')
FILE_PEUF = THIS_FILE.parent / 'tool_config' / FILE_PY.with_ext('peuf').name


# Let's contruct.

TAB = " "*4*2

COMMENT_TAG       = f'ESCAPE - AUTO CODE'
COMMENT_START_TAG = f'# -- {COMMENT_TAG} - START -- #'
COMMENT_END_TAG   = f'# -- {COMMENT_TAG} - END -- #'

ASCII = 'ascii'
TEXT  = 'text'
MATH  = 'math'

MODES = ['text', 'math']

CHARS_TO_ESCAPE   = {}
CHARS_TO_LATEXIFY = defaultdict(dict)


with ReadBlock(
    content = FILE_PEUF,
    mode    = {
        "keyval:: =": ':default:',
        "verbatim"  : 'math-n-text',
    }
) as datas: 
    config = {}
    
    for kind, infos in datas.mydict("std nosep nonb").items():
# Chars to escape.
        if kind == 'math-n-text':
            infos = ' '.join(infos)

            chars = ''.join(
                onechar.strip()
                for onechar in infos.split()
            )

            for m in MODES:
                CHARS_TO_ESCAPE[m] = chars

# Special macros for chars to escape.
        else:
            asciichar = infos[ASCII]
            asciichar = asciichar.replace('\\', '\\'*2)

            for m in MODES: 
                if m in infos:
                    latexcode = infos[m].replace('\\', '\\'*2)

                    CHARS_TO_LATEXIFY[m][asciichar] = latexcode


# Let's update the FILE_PY.

code_latexify = {}

for m in MODES:
    code_latexify[m] = f'\n{TAB}'.join([
        f'"{k}": "{v}"'
        for k, v in CHARS_TO_LATEXIFY[m].items()
    ])

code = f'''
CHARS_TO_ESCAPE = {{
    '{TEXT}': "{CHARS_TO_ESCAPE[TEXT]}",
    '{MATH}': "{CHARS_TO_ESCAPE[MATH]}" 
}}

CHARS_TO_LATEXIFY = {{
    '{TEXT}': {{
        {code_latexify[TEXT]}
    }},
    '{MATH}': {{
        {code_latexify[MATH]}
    }}
}}
'''

with FILE_PY.open(
    encoding = "utf-8",
    mode     = "r"
) as file:
    content = file.read()


before, _ , after = between(
    text = content, 
    seps = [
        COMMENT_START_TAG,
        COMMENT_END_TAG
    ],
    keepseps = True
)

content = f'{before}\n{code}\n{after}'


with FILE_PY.open(
    encoding = "utf-8",
    mode     = "w"
) as file:
    file.write(content)
