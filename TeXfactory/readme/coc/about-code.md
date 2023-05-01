### Some `about.yaml` files in each sub-folder

?????

Here is the part of the implementations in our source code.

~~~
+ src
    + intro
        * intro.tex
    + other-tools
        * config.sty
        * config.tex
        * other.sty
        * other.tex
        * utils.py
        + images
            * screenshot.png
    + some-tools
        * about.yaml
        * optional.tex
        * mandatory.tex
        * some.sty
        + utils
            * config.lua
            * analyzer.lua
        + locale
            * EN.sty
            * FR.sty
    + ...
~~~






`src/some-tools/about.yaml`


~~~yaml
toc:
  - some.sty
  - optional.tex
  - mandatory.tex
~~~


pour  -tools sty et tex auto si indiqué via toc

~~~
+ other-tools
    * config.sty
    * config.tex
    * other.sty
    * other.tex
    * utils.py
    + images
~~~
`src/other-tools/about.yaml`

~~~yaml
toc:
  - config.*
  - other.*
~~~
