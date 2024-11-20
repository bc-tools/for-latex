from collections import defaultdict
from copy        import deepcopy

import re

test_str = r"""
% ********************************************************* %
% ** This is file `tutodoc.cls' generated automatically. ** %
% **                                                     ** %
% ** Copyright (C) 2023-2024 by Christophe, BAL          ** %
% **                                                     ** %
% ** This file may be distributed and/or modified under  ** %
% ** the conditions of the GNU 3 License.                ** %
% ********************************************************* %

\ProvidesExplClass
  {tutodoc}
  {2024-10-30}  % Creation: 2023-11-29
  {1.6.2}
  {This package proposes tools for writing "human friendly" documentations of LaTeX packages.}


% =================== %
% == PACKAGES USED == %
% =================== %

% ------------- %
% -- OPTIONS -- %
% ------------- %

\ExplSyntaxOn

\tl_new:N \l__tutodoc_other_cls_options_tl

\newcommand{ \tutodoc@theme } { color }

\keys_define:nn { tutodoc / main / class / options } {
  theme .choices:nn = {
    bw,
    color,
    dark,
    draft
  } {
    \renewcommand{ \tutodoc@theme } {
      \tl_use:N \l_keys_choice_tl
    }
  },
  unknown .code:n = {
    \tl_set:Nn \l__tutodoc_other_cls_options_tl { #1 }
  }
}

\ProcessKeyOptions[tutodoc / main / class / options]

\exp_last_unbraced:NNV \LoadClass[ \l__tutodoc_other_cls_options_tl ]%
          { article }%
          [ 2022-06-01 ]

\ExplSyntaxOff


% ------------- %
% -- IMPORTS -- %
% ------------- %

\RequirePackage[svgnames]%
               {xcolor}%
               [2023/11/15]

\RequirePackage[
  top            = 2.5cm,
  bottom         = 2.5cm,
  left           = 2.5cm,
  right          = 2.5cm,
  marginparwidth = 2cm,
  marginparsep   = 2mm,
  heightrounded
]{geometry}%
 [2020-01-02]

\RequirePackage[raggedright]%
               {titlesec}%
               [2023/10/27]

\RequirePackage{tocbasic}

\RequirePackage{xcolor}%
               [2022/06/12]

\RequirePackage{hyperref}% To load after titlesec!
               [2023-02-07]


% We delegate the management of quoting to the ''csquotes'' package,
% which takes care of the locale settings.
\RequirePackage{csquotes}%
               [2022-09-14]


\RequirePackage{fontawesome5}%
               [2022-05-02]

\RequirePackage{keytheorems}%
               [2024/09/19]

\RequirePackage[svgnames]%
               {xcolor}%
               [2023/11/15]

\RequirePackage{tcolorbox}%
               [2024/07/10]

\tcbuselibrary{breakable,
               skins}


\RequirePackage{clrstrip}%
               [2021-08-28]


\RequirePackage[highlightmode = immediate]%
               {minted}%
               [2024/09/22]

\RequirePackage{tcolorbox}%
               [2024/07/10]

\tcbuselibrary{minted,
               breakable,
               skins}


\RequirePackage{fontawesome5}%
               [2022-05-02]

\RequirePackage{marginnote}%
               [2018/08/09]


    """

pattern = re.compile(
    r"""
        \\(?P<kind>RequirePackage|LoadClass|tcbuselibrary) #
        (\[(?P<options>[^][]*)\])?              #
        (?P<xtra_1>[^{]*)                      #
        {(?P<name>[^{}]*)}                   #
        (?P<xtra_2>.*)                           #
        (?:\n\s*\[(?P<date>[^][]*)])?        #
    """.strip(),
    re.VERBOSE
)

matches = pattern.finditer(test_str)

metaimports     = defaultdict(dict)
specificimports = {
    "tcbuselibrary": set(),
}

for m in matches:
    kind = m["kind"]

# Library import.
    if kind in specificimports:
        specificimports[kind] = specificimports[kind].union(
            set(
                x.strip()
                for x in m["name"].split(',')
            )
        )

        continue

# Standard import.
    metakind = metaimports[kind]

# We keep the last import!
    if m["name"] in metakind:
        thismeta = deepcopy(metakind[m["name"]])
        del metakind[m["name"]]

    else:
        thismeta = defaultdict(list)

    for i in ["options", "date"]:
        if not m[i] is None:
            thismeta[i].append(m[i])

    metaimports[kind][m["name"]] = deepcopy(thismeta)



print(f"\n{specificimports=}")

print("\nmetaimports")

from pprint import pprint
pprint(metaimports)
