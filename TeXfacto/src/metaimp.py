# all pacjkges installed

# tlmgr list --only-installed > installed_texlive_packages.txt

from collections import defaultdict
from copy        import deepcopy
from pathlib     import Path
from yaml        import dump

import re

PATH_FILE = Path(__file__).parent.parent.parent / "tutodoc" / "src" / "main" / "main.cls"
YAML_FILE = Path(__file__).parent.parent.parent / "tutodoc" / "src" / "DEPENDS.yaml"

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

pack_require_like_pattern = re.compile(
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

cls_pass_option_pattern = re.compile(
    r"""
        \\(?:PassOptionsToClass) #
        (?:[^{]*)                #
        {(?P<options>[^{}]*)}    #
        (?:[^{]*)                #
        {(?P<name>[^{}]*)}       #
    """.strip(),
    re.VERBOSE
)

if not PATH_FILE is None:
    test_str = PATH_FILE.read_text()


content = []

for line in test_str.split("\n"):
    line = line.strip()

    if not line or line.startswith("%"):
        continue

    content.append(line)

content = "\n".join(content)

matches = pack_require_like_pattern.finditer(content)

metaimports      = defaultdict(dict)
specific_actions = {
    "tcbuselibrary": set(),
    "geometry": set(),
}

for m in matches:
    kind = m["kind"].strip()

# Library import.
    if kind in specific_actions:
        specific_actions[kind] = specific_actions[kind].union(
            set(
                x.strip()
                for x in m["name"].split(',')
            )
        )

        continue

# Standard import.
    metakind = metaimports[kind]

    name = m["name"].strip()

# We keep the last import!
    if name in metakind:
        thismeta = deepcopy(metakind[name])
        del metakind[names]

    else:
        thismeta = {
            "options": set(),
            "date": set(),
        }

    for i in ["options", "date"]:
        if not m[i] is None:
            thismeta[i].add(m[i])

    metaimports[kind][name] = deepcopy(thismeta)





matches = cls_pass_option_pattern.finditer(content)

for m in matches:
    name = m["name"].strip()

    if not name in metaimports["LoadClass"]:
        raise ValueError(f"the class '{name}' has not been loaded!")

    options = m["options"].strip()

    metaimports["LoadClass"][name]["options"].add(options)


alltexnames = {
    "cls"  : ["LoadClass"],
    "packs": [
        "RequirePackage",
        "usepackage",
    ],
}

yaml_storing = {}

for kind, texnames in alltexnames.items():
    thiskind = []

    print(f"-- {kind}")

    for tname in texnames:
        for what, metawhat in metaimports[tname].items():
            if not(
                metawhat["options"]
                or
                metawhat["date"]
            ):
                thiskind.append(what)

            else:
                about = {}

                for x in [
                    "options",
                    "date"
                ]:
                  if metawhat[x]:
                      about[x] = metawhat[x]

                thiskind.append({
                  what: deepcopy(about)
                })



    yaml_storing[kind] = deepcopy(thiskind)


print(yaml_storing)


print(f"\n{specific_actions=}")

exit()

print("\nmetaimports")

# from pprint import pprint;pprint(metaimports)

print(metaimports)


exit()

yaml_storing = {}



YAML_FILE.touch()

with YAML_FILE.open(
    mode = 'w',
) as f:
    dump(metaimports, f)
