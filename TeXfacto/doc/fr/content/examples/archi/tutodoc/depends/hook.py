# Deux modules pour nous aider à gérer le format des dates pour
# la langue de la documentation.
from datetime    import date
from babel.dates import format_date

# La fonction codée est nommée en utilisant le préfixe ''tex_''
# suivi de la version minuscule du nom de la variable de
# substitution, sans les chevrons bien entendu.
#
# IMPORTANT ! Les fonctions de la famille ''tex_...'' doit toujours
# utiliser les deux variables ''lang'' et ''infos'', et renvoyer
# un code TeX valide.
def tex_depends(lang, infos):
# On souhaite un format adapté à l'anglais ou au français, les
# deux seules langues de la documentation.
    if lang == "en":
        fdate = "yyyy-MM-dd"
    else:
        fdate = "dd/MM/yyyy"

# Nous créons d'abord le contenu "intérieur" ligne par la ligne.
    texcode = []

# La documentation du système d'interception nous permet de savoir
# que pour ''<<DEPENDS>>'', la variable ''infos'', qui est fournie
# par TeXfacto, est une liste de couples ''(n, d)'' du type suivant.
#
#     + ''n'' est le nom d'une classe ou d'un package LaTeX avec
#       son extension ''cls'' ou ''sty''.
#
#     + ''d'' est une date au format ''(année, mois, jour)'' un
#       triplet de trois naturels.
    for n, d in infos:
        d = format_date(
            date   = date(*d),
            format = fdate
        )

        texcode.append(
            fr"    \task \texttt{{{n}}}"
              "\n"
            fr"    \hfill {{\small ({d})}}\kern10pt"
        )

# On colle les lignes ensemble avec des retours à la ligne.
    texcode = "\n\n".join(texcode)

# Le code intérieur est inséré dans le corps de l'environnement
# LaTeX souhaité.
    texcode = fr"""
%
\begin{{tasks}}[style=itemize](2)"
{texcode}
\end{{tasks}}
    """.strip()

# Nous renvoyons le code TeX final qu'utilisera TeXfacto lors de
# la fabrication de chaque documentation.
    return texcode
