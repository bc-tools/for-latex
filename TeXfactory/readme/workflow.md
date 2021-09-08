Standardized workflow
---------------------

The project [`bdoc`](https://github.com/projetmbc/tools-for-latex/tree/master/bdoc) is developped using the workflow imposed by `TeXfactory`. The structure of the source code of [`bdoc`](https://github.com/projetmbc/tools-for-latex/tree/master/bdoc) was more or less the following one on September 8, 2021.

~~~
+ src
    * about.peuf
    * LICENSE.txt
    + intro
        * intro-FR.tex
        * intro-FR.pdf
    + main
        * main.sty
        * 01-lang-FR.tex
        * 01-lang-FR.pdf
        * 02-formatting-FR.tex
        * 02-formatting-FR.pdf
        + locale
            * EN.sty
            * FR.sty
            * tech-EN.sty
            * tech-FR.sty
            * tool_update_translate.py
            + tool_config_translate
                * EN.peuf
                * FR.peuf
    + version-n-change
        * version-n-change.sty
        * version-n-change-FR.tex
        * version-n-change-FR.pdf
        + examples
            + version-n-change
                * new.tex
                * topic.tex
                * version.tex
~~~

Thanks to `TeXfactory`, the following final product is obtained automatically.

~~~
+ bdoc
    * bdoc.sty
    * bdoc-FR.tex
    * bdoc-FR.pdf
    + examples
        + version-n-change
            * new.tex
            * topic.tex
            * version.tex
    + locale
        * EN.sty
        * FR.sty
        * tech-EN.sty
        * tech-FR.sty
    * LICENSE.txt
~~~


Here is what `TeXfactory` does for us.

  1. The file `bdoc.sty` gathers all the codes developped in `main.sty` and `version-n-change.sty` (see the last point below about the order used to build the final file). The source files must be directly inside a subfolder of the directory `src`.

  1. The file `bdoc-FR.tex` gathers the files `...-FR.tex` inside a subfolder of the directory `src` (see the last point below about the order used to build this file). The `PDF` file `bdoc-FR.pdf` is automatically compiled via `LaTeX`.

  1. Extra files are copied except the `PDFs` `...-FR.pdf` associated to small parts of the documentation and the ones having a name starting by `tool_` (you can choose which folders and files have to be ignored regarding some patterns about their names).

  1. In the folder `src`, there is a special file `about.peuf` which gives the order to follow to produce the final `bdoc.sty` and `bdoc-FR.tex` files. The content of `about.peuf` is given below. You can also use such a file inside subfolders of the directory `src`. If you don't do that, as it is the case inside the folder `main`, the construction will use a natural order.

~~~
toc::
    + intro
    + main
    + version-n-change
~~~
