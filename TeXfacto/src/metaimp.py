import re

test_str = r"""
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

\RequirePackage{tocbasic}

\RequirePackage[svgnames]%
               {xcolor}%
               [2023/11/15]

\RequirePackage[raggedright]%  OK?
                {titlesec}

\RequirePackage{xcolor}%
               [2022/06/12]

\RequirePackage{hyperref}% To load after titlesec!
               [2023-02-07]
    """

pattern = re.compile(
    r"""
        \\(RequirePackage|LoadClass) #
        (\[([^][]*)\])?              #
        ([^{]*)                      #
        {([^{}]*)}                   #
        .*                           #
        (?:\n\s*\[([^][]*)])?        #
    """.strip(),
    re.VERBOSE
)

matches = pattern.finditer(test_str)

for m in matches:
    print('---')

    for i in range(len(m.groups()) + 1):
        print(f"m.group({i}):")
        print(m.group(i))
        print()

    input()
