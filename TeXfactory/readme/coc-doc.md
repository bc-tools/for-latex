### Typing the documentation

The documentation of a small part of the final code must be typed inside the same folder using one or several `TEX` files. The language used is indicated inside the `about.yaml` file of the projet.


How to use packages, macros, or environments just for the documentation? To acheive that, you can complete or use an `about.yaml` file in the source folder with the block `extra` to give the path of a file with lines of code that will be simply imported just before `\begin{document}`.

~~~
extra::
    doc-header = relative/path/to/doc-settings.tex
~~~
