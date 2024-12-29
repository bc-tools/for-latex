# on fr-ournit de type alias du type TXF_..._Type ce qui permet de faire au passage de l'introspection et sera facile d'mploi
#
#
#  Il vaut mieux employer le typage à la Python. Ici nous devons indiquer un type
# >>> from typing import TypeAlias
# >>> Vector: TypeAlias =List[Tuple[str, Tuple[int, int, int]]]
# >>> print(get_args(Vector))
# (typing.Tuple[str, typing.Tuple[int, int, int]],)
# >>> print(get_origin(Vector))
# <class 'list'>
from typing import List

# TODO
from datetime    import date
from babel.dates import format_date

# TODO
def tex_depends(
    lang : str,
    infos,#: list(tuple(str, tuple(int, int, int)))
) -> str:
    texcode = []

    for n, d in infos:
        d = format_date(
            date   = date(*d),
            format = "dd/MM/yyyy",
            locale = lang
        )

        texcode.append(
            fr"    \task \texttt{{{n}}}"
              "\n"
            fr"    \hfill {{\small ({d})}}\kern10pt"
        )

    texcode = "\n\n".join(texcode)
    texcode = fr"""
%
\begin{{tasks}}[style=itemize](2)"
{texcode}
\end{{tasks}}
    """.strip()

    return texcode


print(
    tex_depends(
        "en",
        [("XXX", (2024, 12, 30)),
        ("XXX", (2024, 12, 30))]
    )
)
