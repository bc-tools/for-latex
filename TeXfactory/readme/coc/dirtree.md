### The fictive source folder

In the following sections, we will consider a project named `FictivePack` with the following source folder where one `Lua` file is used by the final package, and some translations are defined inside one folder `locale`.

~~~
+ FictivePack
    * about.yaml
    * versions.yaml
    + src
        * about.yaml
        + changelog [...]
        + init-tools
            * about.yaml
            * optional.tex
            * mandatory.tex
            * some.sty
            * utils.lua
            + locale
                * EN.sty
                * FR.sty
        + intro
            * intro.tex
    + ...
~~~


> ***WARNING 1.*** *The `FictivePack` project folder cannot use in its development cycle a folder named `fictivepack` because it is overwritten every time `TeXfactory` is called.*


> ***WARNING 2.*** *The files `FictivePack/about.yaml` and `FictivePack/versions.yaml`, and the subfolder `changelog` have a special meaning that we will explain later.*
