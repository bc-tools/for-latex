from .gather import copyfromto, emptydir

def update_contrib(
    projdir,
    toc_doc,
    toc_doc_resrces,
    main_lang = 'fr'
):
    contribdir = projdir / "contrib" / "doc"
    srcdir     = projdir / "src"

    maindoc = contribdir / main_lang

    emptydir(maindoc)

    for docfile in toc_doc:
        copyfromto(
            srcdir / docfile,
            maindoc / docfile
        )
