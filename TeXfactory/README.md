The `Python` module `TeXfactory`
================================


> **I beg your pardon for my english...**
>
> English is not my native language, so be nice if you notice misunderstandings, misspellings, or grammatical errors in my documents and codes.


About `TeXfactory`
------------------

This module proposes `Python` tools to automate the production of a `TeX` project from a source directory using a standardized workflow (the idea is to code easily small parts of the project).


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


Code of coding
--------------

Let's see now all the rules to follow such as to help `TeXfactory` to make the final product.


### Organize the source files

Let's imagine a project named `MyProject` having the following source folder where some `Python` and `Lua` files are used by the project.

~~~
+ MyProject
    + src
        * LICENSE.txt
        + intro
            * intro-FR.tex
            * intro-FR.pdf
        + other-tools
            * other.sty
            * other_utils.py
            * other-FR.tex
            * other-FR.pdf
        + some-tools
            * some.sty
            * some_utils.lua
            * 01-some-inter-FR.tex
            * 01-some-inter-FR.pdf
            * 02-some-medium-FR.tex
            * 02-some-medium-FR.pdf
            + config
                * EN.sty
                * FR.sty
~~~

What are the hidden rules used in this source folder?

  1. The final product, its documentation and its main `STY` file will be named using the lower case version of the project.

  1. Only the `STY` files inside a subfolder of the directory `src` are considered as parts of the single final `STY` file. Other `STY` files can be used, like the ones inside the folder `config`, but there will be only copied.

  1. Each file `...-FR.tex` inside a subfolder of the directory `src` is considered as a piece of the documentation of the final product. This implies that the corresponding `PDF` files `...-FR.pdf` won't be imported in the final product.

  1. Except for the files to be ignored, we will talk about that later, all the other files will be copied in the final product by following a similar structure as shown just below. If some duplicated files are found during the copy stage, an error is emitted.


~~~
+ MyProject
    + src
        * ...

    + myproject
        * LICENSE.txt
        * myproject.sty
        * myproject-FR.tex
        * myproject-FR.pdf
        * other_utils.py
        * some_utils.lua
        + config
            * EN.sty
            * FR.sty
~~~


### Choosing the order of the analyse

By default, a source folder is analyzed using a natural order which is `intro`, `other-tools` and `some-tools` for the following project.

~~~
+ OneProject
    + src
        * ...
        + intro
            * ...
        + other-tools
            * ...
        + some-tools
            * ...
~~~

You can impose a different order `intro`, `some-tools` and `other-tools` by adding a file `about.peuf` directly inside the directory `src`, this file having the following content. **In this case, the folders indicated in the `about.peuf` file are the only ones analyzed.**

~~~
toc::
    + intro
    + some-tools
    + other-tools
~~~

You can also use `about.peuf` files inside the subfolders used to code small parts of the final `STY` file such as to indicate `STY` and `TEX` files to be analyzed. **Don't forget in that case to indicate all the files concerned with their extension!**


### Some rules for pure coding

The `STY` parts of the final product are directly inside a subfolder of the source directory. They must use the following template with some magic comments.

~~~latex
% == PACKAGES == %

% ...

% == OPTIONS == %

% ...

% == TOOLS == %

% ...
~~~


Here is how to use those magic comments.

  1. The order above must be respected even if you don't use all the magic comments.

  1. The comment `% == PACKAGES == %` indicates lines importing packages via `\RequirePackage` or `\usepackage`, but also via `\tcbuselibrary` for example.

  1. The comment `% == OPTIONS == %` is dedicated to the management of the package options.

  1. The comment `% == TOOLS == %` is for definitions of environments and macros, and also for settings using macros.


### Typing the documentation

The documentation of a small part of the final code must be typed inside the same folder using one or several `TEX` files with a name finishing by either `-FR` or `-EN`. Those suffixes indicate French and English languages which are the only ones supported at this moment.


How to use packages, macros, or environments just for the documentation? To acheive that, you can complete or use an `about.peuf` file in the source folder with the block `extra` to give the path of a file with lines of codes that will be simply imported just before `\begin{document}`.

~~~
extra::
    doc-header = relative/path/to/doc-settings.tex
~~~


### Use of other files

The only important things to do with extra files needed by the final project is to use them via relative paths.


Build the final product
-----------------------

TODO...