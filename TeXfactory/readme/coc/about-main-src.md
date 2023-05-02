### One `about.yaml` file for the source folder

One optional `about.yaml` file can be added to change the default behavior of `TeXfactory`. Let's give again the general structure of our source code.

~~~
+ src
    * about.yaml
    + changelog
    + init-tools
    + intro
~~~

Without the use of `src/about.yaml`, all folders will be processed in alphabetical order, except for the very special subfolder `changelog` which will be used to produce the change log for the user (we will explain this later). If we want to choose the order of analysis, we have to use an `about.yaml` file like the one below where the value of the `toc` key indicates the ordered list of folders to be treated.

~~~yaml
toc:
  - intro
  - init-tools
~~~
