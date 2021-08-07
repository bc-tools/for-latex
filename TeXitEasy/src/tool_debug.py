#! /usr/bin/env python3

from escape import fstringit

texcode = r'''
\NewDocumentCommand{ \fictivenv }
                   { O{abc}m }{
    \onemacro{<:PYVAR_FOR_FSTRING:>}{#2}
}
'''

print(fstringit(texcode))