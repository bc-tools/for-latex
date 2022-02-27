Escaping
--------

### For `LaTeX`...

The function `texiteasy.escape.escape` "escapes" special `LaTeX` characters. Here is an example of use.

~~~python
from texiteasy.escape import escape, MODE_MATH

txt = "\OH/ & ..."

print("Default mode (MODE_TEXT):")
print(escape(txt))
print()
print("Math mode (MODE_MATH):")
print(escape(text = txt, mode = MODE_MATH))
~~~

Launched in a terminal, the preceding script prints the following output.

~~~
Default mode (MODE_TEXT):
\textbackslash{}OH/ \& ...

Math mode:
\backslash{}OH/ \& ...
~~~


### For `Python`...

Working together with `LaTeX` templates for `f-strings` is very boring because of the curly braces. The function `texiteasy.escape.fstringit` simplifies this as you can see in the following code. Note that `<:PYVAR_FOR_F_STRING:>` is used instead of ``{PYVAR_FOR_F_STRING}`` as this must normally be done in `f-strings`.

~~~python
from texiteasy.escape import fstringit

texcode = r'''
\NewDocumentCommand{ \fictivenv }
                   { O{abc}m }{
    \onemacro{<:PYVAR_FOR_F_STRING:>}{#2}
}
'''.strip()

readytouse = fstringit(texcode)

print(readytouse.format(PYVAR_FOR_F_STRING = 'TEST'))
~~~

Launched in a terminal, the preceding script prints the following output.

~~~
\NewDocumentCommand{ \fictivenv }
                   { O{abc}m }{
    \onemacro{TEST}{#2}
}
~~~
