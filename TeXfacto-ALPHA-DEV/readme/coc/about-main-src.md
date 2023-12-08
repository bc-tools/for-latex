### Optional `about.yaml` file for the source folder

To change the default behavior of `TeXfacto` on the source folder, you can add an `about.yaml` file. Let's give again the general structure of our source code.

~~~
+ src
    * about.yaml
    + init-tools
    + intro
~~~

Without the use of `src/about.yaml`, all folders will be processed in "natural" order. If we want to change this, we have to use an `about.yaml` file like the one below where the value of the `toc` key indicates the ordered list of folders to be treated. **Don't forget in that case to indicate all the subfolders concerned!**

~~~yaml
toc:
  - intro
  - init-tools
~~~


> ***NOTE.*** *It is also possible to use `about.yaml` files in any folder analyzed by `TeXfacto`. In our example, we don't need them in `init-tools` as following the "natural" sorting is fine.*
