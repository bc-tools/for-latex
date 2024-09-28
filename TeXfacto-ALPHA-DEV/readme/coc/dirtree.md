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
