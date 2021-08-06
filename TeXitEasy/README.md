About `TeXitEasy`
=================


I beg your pardon for my english...
===================================

English is not my native language, so be nice if you notice misunderstandings, misspellings, or grammatical errors in my documents and codes.


About
=====

This project proposes `Python` tools to ease the use of `LaTeX`.


Escaping the special LaTeX characters
=====================================

The function ``latex_use.escape`` will escape all special characters for you regarding the text or math mode.

```python
>>> from mistool.latex_use import escape
>>> onetext = "\OH/ & ..."
>>> print(escape(onetext))
\textbackslash{}OH/ \& ...
>>> print(escape(text = onetext, mode = "math"))
\backslash{}OH/ \& ...
```


Easy LaTeX compilation(s)
=========================

The class ``latex_use.Build`` compiles a LaTeX file for you *(for the moment only the PDF compilation is implemented)*. Let's consider the
following LaTeX file with the absolute path ``/Users/projetmbc/latex/file.tex``.

```latex
\documentclass[11pt, oneside]{article}

\begin{document}

\section{One little test}

One basic formula : $E = mc^2$.

\end{document}
```

In the following code, we call to the class ``term_use.DirView`` so as to show the new files made by LaTeX *(the ellipsis ``[...]``
indicates some lines not reproduced here)*.

```python
>>> from mistool.latex_use import Build, PPath
>>> from mistool.term_use import DirView
>>> latexdir = PPath("/Users/projetmbc/latex/file.tex")
>>> print(DirView(latexdir.parent).ascii)
+ latex
    * file.tex
>>> builder   = Build(latexdir)
>>> builder.pdf()
# == Start of compilation Nb.1 == #

This is pdfTeX, Version 3.14159265-2.6-1.40.15 (TeX Live 2014) (preloaded
format=pdflatex)
 restricted \write18 enabled.
entering extended mode

[...]

Output written on file.pdf (1 page, 36666 bytes).
Transcript written on file.log.

# == End of compilation Nb.1 == #
>>> print(DirView(latexdir.parent).ascii)
+ latex
    * file.aux
    * file.log
    * file.pdf
    * file.tex
```

The PDF file has been build by LaTeX but there are also temporary ones. If you need several compilations, so as to build a table of content for example, just use the attribut-argument ``repeat``, and if you don't want to see the LaTeX ouput, just set the attribut-argument ``showinfos`` to ``False``.


Removing the temporary files produced by LaTeX
==============================================

We keep the same LaTeX example file. The function ``latex_use.clean`` cleans all unuseful temporary files when the compilation has been done.

```python
>>> from mistool.latex_use import clean, PPath
>>> from mistool.term_use import DirView
>>> latexdir = PPath("/Users/projetmbc/latex")
>>> print(DirView(latexdir.parent).ascii)
+ latex
    * file.aux
    * file.log
    * file.pdf
    * file.synctex.gz
    * file.tex
>>> clean(ppath = latexdir, showinfos = True)
* Cleaning for "/Users/projetmbc/latex/file.tex"
>>> print(DirView(latexdir.parent).ascii)
+ latex
    * file.pdf
    * file.tex
```


Automatic installation of personal LaTeX packages
=================================================

Let's suppose that we have package named ``lyxam`` stored in a folder having the absolute path ``/Users/projetmbc/latex/lyxam`` and whose structure is the following one.

```
+ lyxam
    + change_log
        + 2012
            * 02.txt
            * 03.txt
            * 04.txt
            * 10.txt
        * todo.txt
    * lyxam.sty
    + config
        * settings.tex
        + lang
            * en.tex
            * fr.tex
            + special
                * fr.config
            + standard
                * en.config
                * fr.config
        + style
            * apmep.tex
            * default.tex
```

To install this package locally in your LaTeX distribution, just do like in the code above.

```python
>>> from mistool.latex_use import install, PPath
>>> package = PPath("/Users/projetmbc/latex/lyxam")
>>> install(package)
Starting installation of the package locally.
    * Deletion of the old << lyxam >> package in the local LaTeX directory.
    * Creation of a new << lyxam >> package in the local LaTeX directory.
        + Adding the new file << lyxam.sty >>
        + Adding the new file << change_log/todo.txt >>
        + Adding the new file << change_log/2012/02.txt >>
        + Adding the new file << change_log/2012/03.txt >>
        + Adding the new file << change_log/2012/04.txt >>
        + Adding the new file << change_log/2012/10.txt >>
        + Adding the new file << config/settings.tex >>
        + Adding the new file << config/lang/en.tex >>
        + Adding the new file << config/lang/fr.tex >>
        + Adding the new file << config/lang/special/fr.config >>
        + Adding the new file << config/lang/standard/en.config >>
        + Adding the new file << config/lang/standard/fr.config >>
        + Adding the new file << config/style/apmep.tex >>
        + Adding the new file << config/style/default.tex >>
    * Refreshing the list of LaTeX packages.
```


Using the concept of "regpath" of the module ``os_use``, you can for example choose to not install all the ``TXT`` files.

```python
>>> from mistool.latex_use import install, PPath
>>> package = PPath("/Users/projetmbc/latex/lyxam")
>>> install(ppath = package, regpath = "file not::**.txt")
Starting installation of the package locally.
    * Deletion of the old << lyxam >> package in the local LaTeX directory.
    * Creation of a new << lyxam >> package in the local LaTeX directory.
        + Adding the new file << lyxam.sty >>
        + Adding the new file << config/settings.tex >>
        + Adding the new file << config/lang/en.tex >>
        + Adding the new file << config/lang/fr.tex >>
        + Adding the new file << config/lang/special/fr.config >>
        + Adding the new file << config/lang/standard/en.config >>
        + Adding the new file << config/lang/standard/fr.config >>
        + Adding the new file << config/style/apmep.tex >>
        + Adding the new file << config/style/default.tex >>
    * Refreshing the list of LaTeX packages.
```


Remove a personal LaTeX packages
================================

Just use ``remove(name)`` where ``name`` is the name of a local LaTeX package.




<!-- :version-START: -->
<!-- :version-END: -->
