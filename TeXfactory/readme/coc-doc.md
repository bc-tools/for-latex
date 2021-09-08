### Typing the documentation

The documentation of a small part of the final code must be typed inside the same folder using one or several `TEX` files with a name finishing by either `-FR` or `-EN`. Those suffixes indicate French and English languages which are the only ones supported at this moment.


How to use packages, macros, or environments just for the documentation? To acheive that, you can complete or use an `about.peuf` file in the source folder with the block `extra` to give the path of a file with lines of codes that will be simply imported just before `\begin{document}`.

~~~
extra::
    doc-header = relative/path/to/doc-settings.tex
~~~
