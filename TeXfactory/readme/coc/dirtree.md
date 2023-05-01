### The fictive source folder

In the following sections, we will consider a project named `FictivePack` with the following source folder where some `Python` and `Lua` files are used by the final package, and some images are needed to document the package.

~~~
+ FictivePack
    * about.yaml
    * versions.yaml
    + src
        * about.yaml
        * doc-header.tex
        + changelog [...]
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


> ***WARNING 1.*** *The `FictivePack` project folder cannot use in its development cycle a folder named `fictivepack` because it is overwritten every time `TeXfactory` is called.*


> ***WARNING 2.*** *The subfolder `changelog` has a special meaning that we will explain later.*
