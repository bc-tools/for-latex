from pathlib import Path
import              re
from yaml    import dump as yaml_dump

from natsort import natsorted

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

        stable_versions[version] = f"{year}-{month}-{day}"

# from pprint import pprint;pprint(stable_versions)

PRE_AUTO_VERSION_FILE.write_text(
    yaml_dump(stable_versions)
)
