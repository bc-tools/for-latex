from pathlib import Path
import              re

from semver.version import Version

THIS_DIR              = Path(__file__).parent
STABLE_CHGES_DIR      = THIS_DIR.parent / 'changes' / 'stable'
PRE_AUTO_VERSION_FILE = THIS_DIR / 'pre-auto' / 'stable-versions.yaml'

DATE_PATTERN = re.compile(r"==\n(\d+)\s+\((.+)\)\n==")

stable_versions = {}

for month_file in STABLE_CHGES_DIR.glob("*/*.txt"):
    year  = month_file.parent.name
    month = month_file.stem
    # print(f"{year} / {month}")

    content = month_file.read_text()

    # print(content)

    match = re.search(DATE_PATTERN, content)
    if match:
        day     = match.group(1)
        version = match.group(2)

        stable_versions[version] = [year, month, day]


yaml_stable_versions_sorted = []

all_nb_versions = [
    Version.parse(v)
    for v in stable_versions
]

all_nb_versions.sort(reverse = True)

for v in all_nb_versions:
    v = str(v)

    yaml_stable_versions_sorted.append(
        f"'{v}': {stable_versions[v]}"
    )

yaml_stable_versions_sorted = '\n'.join(yaml_stable_versions_sorted)

PRE_AUTO_VERSION_FILE.write_text(yaml_stable_versions_sorted)
