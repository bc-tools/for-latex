Standardized workflow
---------------------

Let's consider the project [`bdoc`](https://github.com/projetmbc/tools-for-latex/tree/master/bdoc) which is developped using the workflow imposed by `TeXfactory`. The structure of the source code of [`bdoc`](https://github.com/projetmbc/tools-for-latex/tree/master/bdoc) was partially the following one on April 29, 2023.

~~~
+ src
    * about.yaml
    * LICENSE.txt
    + intro
        * intro.tex
        * intro.pdf
    + main
        * about.yaml
        * main.sty
        * lang.tex
        * lang.pdf
        * formatting-geo.tex
        * formatting-geo.pdf
        * formatting-title-n-toc.tex
        * formatting-title-n-toc.pdf
        * formatting-link.tex
        * formatting-link.pdf
        + locale
            * FR.sty
            + fr
                * macros.txt
                * sentences.txt
    + version-n-change
        * version-n-change.sty
        * version-n-change.tex
        * version-n-change.pdf
        + examples
            + version-n-change
                * new.tex
                * topic.tex
                * version.tex
    + ...
~~~


Thanks to `TeXfactory`, the following final product is obtained automatically.

~~~
+ bdoc
    * bdoc.sty
    * bdoc.tex
    * bdoc.pdf
    + examples
        + version-n-change
            * new.tex
            * topic.tex
            * version.tex
    + locale
        * FR.sty
    * LICENSE.txt
~~~


Here is what `TeXfactory` does for us.

  1. The file `bdoc.sty` gathers all the codes developped in `main.sty` and `version-n-change.sty` (see the last point below about the order used to build the final file). The source files must be directly inside a subfolder of the directory `src`.

  1. The file `bdoc.tex` gathers the files `....tex` inside a subfolder of the directory `src` (see the last point below about the order used to build this file). The `PDF` file `bdoc.pdf` is automatically compiled via `LaTeX`, or `LuaTeX` as needed.

  1. Extra files are copied except the `PDFs` associated to small parts of the documentation (you can choose which folders and files have to be ignored regarding some patterns about their names).

  1. In the folder `src`, there is a special file `about.yaml` which gives the order to follow to produce the final `bdoc.sty` and `bdoc.tex` files. The content of `about.yaml` could be the one given below. You can also use such a file inside subfolders of the directory `src`, as it is the case inside the folder `main`. If you don't do that, the construction will use a natural order.

~~~yaml
toc:
  - intro
  - main
  - version-n-change
~~~
