### One `about.yaml` file for the project

Let's start with the important `FictivePack/about.yaml` file which gives information about the project. This file uses the `YAML` syntax; the content below is very expressive, except perhaps for the key `require` which simply indicates the coding languages required to make the package works.

~~~yaml
general:
  desc   : This package proposes fictive tools.
  author : Christophe BAL
  licence: gnu 3
  lang   :
    - doc: fr
  require:
    - latex
    - lualatex
    - python
~~~


Sometimes a package may offer optional extra features based on additional languages. In this case, the key `optional` allows to indicate that additional languages.

~~~yaml
general:
  # Same starting lines as before.
  #
  # Only LaTeX is required.
  require:
    - latex
  # By allowing the use of Python, and/or
  # using LuaLaTeX, some extra features
  # will be available.
  optional:
    - lualatex
    - python
~~~
