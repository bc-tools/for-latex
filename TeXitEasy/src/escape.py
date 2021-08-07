#!/usr/bin/env python3

###
# This file proposes two escaping functions. 
#     1) The 1st one escape a text to be used in a ¨latex content.
#     2) The 2nd one prepare a ¨latex source code to be used in a f-string. 
###


# --------------- #
# -- CONSTANTS -- #
# --------------- #

MODE_MATH = "math"
MODE_TEXT = "text"


# -- ESCAPE - AUTO CODE - START -- #

CHARS_TO_ESCAPE = {
    'text': "{}_$&%#",
    'math': "{}_$&%#" 
}

CHARS_TO_LATEXIFY = {
    'text': {
        "\\": "\\textbackslash{}"
    },
    'math': {
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
#     arg = ; // See Python typing...
#           the text to be escaped.
#     arg = _ in ["text" , "math"] ( MODE_TEXT ) ; // See Python typing...
#           the ¨latex mode where the text will be used.
#
#     :return: = ; // See Python typing...
#                the text with all specific ¨latex characters escaped so as
#                to be used verbatim in either a math formula or a text 
#                regarding to the value of ``mode``.
#
# Here are two examples of use.
#
# term-python::
#     >>> from texiteasy.escape import escape, MODE_MATH
#     >>> txt = "\OH/ & ..."
#     >>> print(escape(txt))
#     \textbackslash{}OH/ \& ...
#     >>> print(escape(text = txt, mode = MODE_MATH))
#     \backslash{}OH/ \& ...
###

def escape(
    text: str,
    mode: str = MODE_TEXT
):
    if not mode in CHARS_TO_ESCAPE:
        raise ValueError("unknown mode.")

    tolatexify = CHARS_TO_LATEXIFY[mode].items()
    toescape   = CHARS_TO_ESCAPE[mode]

    escaped_text = ''

    imax = len(text)
    i    = 0

    while(i < imax):
        nothingfound = True

        for onechar in toescape:
            if text[i] == onechar:
                escaped_text += '\\' + onechar
                i            += 1
                nothingfound  = False
                break

        if nothingfound:
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
#     arg = ; // See Python typing...
#           the ¨latex source to transform to a f-string.
#
#     :return: = ; // See Python typing...
#                the source with all specific ¨latex characters escaped so as
#                to be used verbatim in either a math formula or a text 
#                regarding to the value of ``mode``.
#
# Here is an example of use where latex::``<:PYVAR_FOR_FSTRING:>`` is used instead 
# of ``{PYVAR_FOR_FSTRING}`` as this must be done for f-strings.
#
# term-python::
#     >>> from escape import fstringit
#     >>> texcode = r'''
#     \NewDocumentCommand{ \fictivenv }
#                     { O{abc}m }{
#         \onemacro{<:PYVAR_FOR_FSTRING:>}{#2}
#     }
#     '''.strip()
#     >>> print(fstringit(texcode))
#     \NewDocumentCommand{{ \fictivenv }}
#                     {{ O{{abc}}m }}{{
#         \onemacro{{{PYVAR_FOR_FSTRING}}}{{#2}}
#     }}
###

def fstringit(code: str):
    for brace in '{}':
        code = code.replace(brace, brace*2)

    for old, new in PLACEHOLDERS_F_STRING.items():
        code = code.replace(old, new)

    return code
