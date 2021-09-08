### Choosing the order of the analyse

By default, a source folder is analyzed using a natural order which is `intro`, `other-tools` and `some-tools` for the following project.

~~~
+ OneProject
    + src
        * ...
        + intro
            * ...
        + other-tools
            * ...
        + some-tools
            * ...
~~~

You can impose a different order `intro`, `some-tools` and `other-tools` by adding a file `about.peuf` directly inside the directory `src`, this file having the following content. **In this case, the folders indicated in the `about.peuf` file are the only ones analyzed.**

~~~
toc::
    + intro
    + some-tools
    + other-tools
~~~

You can also use `about.peuf` files inside the subfolders used to code small parts of the final `STY` file such as to indicate `STY` and `TEX` files to be analyzed. **Don't forget in that case to indicate all the files concerned with their extension!**
