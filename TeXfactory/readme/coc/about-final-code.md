### The `about.yaml` files to organize the final code

????

Some `about.yaml` files can be added to change the default behavior of `TeXfactory`. Let's give again the general structure of our source code during development.

~~~
+ src
    * about.yaml
    * doc-header.tex
    + changelog
    + intro
    + other-tools
    + some-tools
~~~

Without the use of `src/about.yaml` all the folder will be senn


special sub-folder `changelog`


The `STY` parts of the final product are directly inside a subfolder of the source directory.



~~~
+ some-tools
    * about.yaml
    * optional.tex
    * mandatory.tex
    * some.sty
    + utils
    + locale
~~~

`src/about.yaml`

~~~yaml
doc:
  header: doc-header.tex

toc:
  - intro
  - some-tools
  - other-tools
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
