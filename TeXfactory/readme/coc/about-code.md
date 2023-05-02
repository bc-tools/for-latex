### Some `about.yaml` files in each sub-folder

In the source folder, there is the following sub-folder.

~~~
+ init-tools
    * about.yaml
    * optional.tex
    * mandatory.tex
    * some.sty
    * utils.lua
    + locale
        * EN.sty
        * FR.sty
~~~


The use of the `about.yaml` with the following content asks to treat the files in a given order.

~~~yaml
toc:
  - some.sty
  - optional.tex
  - mandatory.tex
~~~


> ***NOTE.*** *We will see that the utility file `utils.lua`, as well as those in the `locale` folder, which are all used by `some.sty`, will all be automatically added to the final project by `TeXfactory`.*
