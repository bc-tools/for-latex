### One `about.yaml` file for the source folder

One optional `about.yaml` file can be added to change the default behavior of `TeXfactory`. Let's give again the general structure of our source code.

~~~
+ src
    * about.yaml
    * doc-header.tex
    + changelog
    + intro
    + other-tools
    + some-tools
~~~

Without the use of `src/about.yaml`, all folders will be processed in alphabetical order, except for the very special subfolder `changelog` which will be used to produce the change log for the user (we will explain this later). If we want to choose the order of analysis, we have to use an `about.yaml` file like the one below where the value of the `toc` key indicates the ordered list of folders to be treated.

~~~yaml
doc:
  header: doc-header.tex

toc:
  - intro
  - some-tools
  - other-tools
~~~


What is the purpose of the `doc` key? It is used to specify specific parameters to the `TEX` file used to produce the user documentation. Here, we give a file containing the header part of the file, i.e. the lines before `\begin{document}`, more precisely those in the header placed before the instructions automatically built by `TeXfactory` from the source code.
