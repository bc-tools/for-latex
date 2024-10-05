#!/usr/bin/env python3

###
# This file proposes two escaping functions.
#     1) The 1st one escape a text to be used in a \latex content.
#     2) The 2nd one prepare a \latex source code to be used in a f-string.
###


# --------------- #
# -- CONSTANTS -- #
# --------------- #

MODE_MATH = "math"
MODE_TEXT = "text"


# -- ESCAPE - AUTO CODE - START -- #

CHARS_TO_ESCAPE = {
    MODE_TEXT: "{}_$&%#",
    MODE_MATH: "{}_$&%#"
}

CHARS_TO_LATEXIFY = {
    MODE_TEXT: {
        "\\": "\\textbackslash{}"
    },
    MODE_MATH: {
        "\\": "\\backslash{}"
    }
}

# -- ESCAPE - AUTO CODE - END -- #

PLACEHOLDERS_F_STRING = {
    '<:': '{',
    ':>': '}',
}


# -------------------------- #
# -- ESCAPING LATEX CHARS -- #
# -------------------------- #

###
# prototype::
#     text : the text to be escaped.
#     mode : the \latex mode where the text will be used.
#          @ mode in [MODE_MATH, MODE_TEXT]
#
#     :return: the text with all specific \latex characters escaped so as
#              to be used verbatim in either a math formula or a text
#              regarding to the value of ''mode''.
###
def escape(
    text: str,
    mode: str = MODE_TEXT
) -> str:
    assert mode in CHARS_TO_ESCAPE, "unknown mode."

    tolatexify = CHARS_TO_LATEXIFY[mode].items()
    toescape   = CHARS_TO_ESCAPE[mode]

    escaped_text = ''

    imax = len(text)
    i    = 0

    while(i < imax):
        if text[i] in toescape:
            escaped_text += '\\' + text[i]
            i            += 1
            continue

        nothingfound = True

        for onechar, latexcode in tolatexify:
            if text[i:].startswith(onechar):
                escaped_text += latexcode
                i            += len(onechar)
                nothingfound  = False
                break

        if nothingfound:
            escaped_text += text[i]
            i            += 1

    return escaped_text


# ------------------------------------ #
# -- USING LATEX CODES IN F-STRINGS -- #
# ------------------------------------ #

###
# prototype::
#     code : the \latex source to transform into a f-string template.
#
#     :return: the source with all specific \latex characters escaped so as
#              to be used verbatim in either a math formula or a text
#              regarding to the value of ''mode''.
###
def fstringit(code: str) -> str:
    for brace in '{}':
        code = code.replace(brace, brace*2)

    for old, new in PLACEHOLDERS_F_STRING.items():
        code = code.replace(old, new)

    return code
