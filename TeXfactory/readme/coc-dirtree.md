### Organize the source files

Let's imagine a project named `MyProject` having the following source folder where some `Python` and `Lua` files are used by the project.

~~~
+ MyProject
    + src
        * LICENSE.txt
        + intro
            * intro.tex
            * intro.pdf
        + other-tools
            * other.sty
            * other_utils.py
            * other.tex
            * other.pdf
        + some-tools
            * some.sty
            * some_utils.lua
            * 01-some-inter.tex
            * 01-some-inter.pdf
            * 02-some-medium.tex
            * 02-some-medium.pdf
            + config
                * EN.sty
                * FR.sty
~~~

What are the hidden rules used in this source folder?

  1. The final product, its documentation and its main `STY` file will be named using the lower case version of the project.

  1. Only the `STY` files inside a subfolder of the directory `src` are considered as parts of the single final `STY` file. Other `STY` files can be used, like the ones inside the folder `config`, but there will be only copied.

  1. Each `tex` file inside a subfolder of the directory `src` is considered as a piece of the documentation of the final product. This implies that the corresponding `PDF` files won't be imported in the final product.

  1. Except for the files to be ignored, we will talk about that later, all the other files will be copied in the final product by following a similar structure as shown just below. If some duplicated files are found during the copy stage, an error is emitted.


~~~
+ MyProject
    + src
        * ...

    + myproject
        * LICENSE.txt
        * myproject.sty
        * myproject.tex
        * myproject.pdf
        * other_utils.py
        * some_utils.lua
        + config
            * EN.sty
            * FR.sty
~~~
