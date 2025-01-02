this::
    date = 2025-01-02


===============================
Maintenir facilement le \readme
===============================

Il est de bon ton de proposer un fichier \readme pour une présentation efficace et claire du \proj. Ceci peut se faire via la rédaction d'un fichier unique sans aide extérieure.
Pour un contenu court, cela est un bon choix, mais dès que le fichier \readme s'épaissit, la maintenance pour des corrections, ou des \majs, peut devenir cauchemardesque.
Via \thisproj, on peut éclater le contenu en petits fichiers \ext::''md'' placés dans le dossier path::''readme''. Voici un exemple réel d'utilisation.

dirtree::
    ---
    path  = ?/examples/archi/tutodoc/readme/dirtree/small.txt
    title = Le tout petit \readme de \tutodoc
    date  = \tutodoc_date
    ---


Le fichier path::''about.yaml'' nous permet ici d'ordonner l'assemblage dans le fichier \readme.

yaml::
    ---
    path  = ?/examples/archi/tutodoc/readme/about.yaml
    title = Un fichier pour ordonner l'ordre d'assemblage
    date  = \tutodoc_date
    ---
