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
