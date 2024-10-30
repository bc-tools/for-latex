The `Python` module `TeXfacto`
==============================

This document is a *not so short* tutorial showing the most useful features without being exhaustive.


About `TeXfacto`
----------------

This module proposes `Python` tools to automate the production of a `TeX` project from a `STY` source directory using a standardized workflow (the idea is to code using small parts of the project rather than big `STY` files).

> [!CAUTION]
> *For the moment, `TeXfacto` is focused on `LaTeX` projects using `STY` files on the coding side with written documentation management via `TEX` files, resource files being possible.. The case of classes will be implemented later, as the author does not use this kind of stuff yet.*


Code of coding
--------------

Let's start by looking at the development cycle needed before calling `TeXfacto` to the rescue. To do this, we will work with a fictitious example.


### The fictive source folder

In the following sections, we will consider a project named `MockProject` with the following source folder where one `Lua` file is used by the final package, and some translations are defined inside one folder `locale`.

~~~
+ MockProject
    * about.yaml
    * versions.yaml
    + src
        * about.yaml
        + init-tools
            * 01-mandatory.tex
            * 02-optional.tex
            * some.sty
            * utils.lua
            + locale
                * EN.sty
                * FR.sty
        + intro
            * intro.tex
    + ...
~~~


> ***NOTE.*** *The file `MockProject/about.yaml` has a special use that will be explained later.*


> ***WARNING.*** *You cannot use the `changelog` subfolder for your code because it is a very special subfolder: see the documentation for more information.*


### Coding style

#### Chunks of code and documentation

The `src` directory in our example shows that the final code is developped using "small" `STY` files together with `TEX` files used to build the "tutorial" documentation and another exposing the public API (the latter gives the "signature" of macros and environments).


> ***NOTE 1.*** *It is possible to target the files and folders analyzed by `TeXfacto`: see the documentation for more information.*


> ***NOTE 2.*** *The `PDF` files associated to a `TEX` chunk of the documentation won't be imported in the final product.*


#### Resources

`TeXfacto` should, normally, find alone the ressources used by the `STY` source files and the `TEX` ones.


#### What `TeXfacto` will do for us?

The goal is to obtain automaticcaly the following `mockproject` folder.

~~~
+ MockProject
    + src [...]
    + mockproject
        * LICENSE.txt
        * mockproject.sty
        * mockproject-DOC-FR.tex
        * mockproject-DOC-FR.pdf
        * mockproject-API.pdf
        * utils.lua
        + locale
            * EN.sty
            * FR.sty
    + ...
~~~


### The `about.yaml` file of the project

Thanks to the `MockProject/about.yaml` file, we can give important informations about the project. The content below is very expressive, except perhaps for the key `require` which simply indicates the coding languages required to make the package works (this file uses the `YAML` syntax).

~~~yaml
general:
  name   : mockproject
  desc   : This package proposes fictive tools.
  author : Christophe BAL
  licence: gnu 3
  lang   :
    - doc: fr
  require:
    - latex
    - lualatex
~~~


> ***NOTE.*** *The `name` key can be omitted if you just want to use a lowercase package name like in our fictitious example.*


Sometimes a pure `LaTeX` package proposes optional extra features based on additional languages. In this case, the key `optional` allows to indicate that additional languages.

~~~yaml
general:
  # ...
  # Same starting lines as before.
  #
  # Only LaTeX is required.
  require:
    - latex
  # Some extra features available if Python,
  # and/or LuaLaTeX can be used.
  optional:
    - lualatex
    - python
~~~


### Optional `about.yaml` file for the source folder

To change the default behavior of `TeXfacto` on the source folder, you can add an `about.yaml` file. Let's give again the general structure of our source code.

~~~
+ src
    * about.yaml
    + init-tools
    + intro
~~~

Without the use of `src/about.yaml`, all folders will be processed in "natural" order. If we want to change this, we have to use an `about.yaml` file like the one below where the value of the `toc` key indicates the ordered list of folders to be treated. **Don't forget in that case to indicate all the subfolders concerned!**

~~~yaml
toc:
  - intro
  - init-tools
~~~


> ***NOTE.*** *It is also possible to use `about.yaml` files in any folder analyzed by `TeXfacto`. In our example, we don't need them in `init-tools` as following the "natural" sorting is fine.*
