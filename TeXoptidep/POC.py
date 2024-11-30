# all pacjkges installed

# tlmgr list --only-installed > installed_texlive_packages.txt

from collections import defaultdict
from copy        import deepcopy
from pathlib     import Path
from yaml        import dump

import re

PATH_FILE = Path(__file__).parent.parent.parent / "tutodoc" / "src" / "main" / "main.cls"
YAML_FILE = Path(__file__).parent.parent.parent / "tutodoc" / "src" / "DEPENDS.yaml"


pack_require_like_pattern = re.compile(
    r"""
        \\(?P<kind>RequirePackage|LoadClass|tcbuselibrary|geometry) #
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


def clean_options(option):
    option = option.split("=")
    option = [x.strip() for x in option]
    option = " = ".join(option)
    return option


for m in matches:
    kind = m["kind"].strip()

# Library import.
    if kind in specific_actions:
        specific_actions[kind] = specific_actions[kind].union(
            set(
                clean_options(x)
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
            thismeta[i].add(
                m[i]
                if i == "options" else
                clean_options(m[i])
            )

    metaimports[kind][name] = deepcopy(thismeta)





matches = cls_pass_option_pattern.finditer(content)

for m in matches:
    name = m["name"].strip()

    if not name in metaimports["LoadClass"]:
        raise ValueError(f"the class '{name}' has not been loaded!")

    options = clean_options(m["options"])

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



YAML_FILE.touch()

with YAML_FILE.open(
    mode = 'w',
) as f:
    dump(yaml_storing, f)




print(f"\n{specific_actions=}")

exit()

print("\nmetaimports")

# from pprint import pprint;pprint(metaimports)

print(metaimports)


exit()

yaml_storing = {}
