### Coding style

#### Chunks of code and documentation

The `src` directory in our example shows that the final code is developped using "small" `STY` files together with `TEX` files used to build the "tutorial" documentation and another exposing the public API (the latter gives the "signature" of macros and environments).


> ***NOTE 1.*** *It is possible to target the files and folders analyzed by `TeXfactory`: see the documentation for more information.*


> ***NOTE 2.*** *The `PDF` files associated to a `TEX` chunk of the documentation won't be imported in the final product.*


#### Resources

`TeXfactory` should, normally, find alone the ressources used by the `STY` source files and the `TEX` ones.


#### What `TeXfactory` will do for us?

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
