from collections import defaultdict

from .constants import *
from .finalize  import prettify_all_titles
from .misc      import *


# --------------------------- #
# -- END IS COMING SOON... -- #
# --------------------------- #

def minicss(
    metadata,
):
    projname = metadata[TAG_PROJ_NAME]

    code_dir = metadata[TAG_ROLLOUT] / "code"
    csspaths = defaultdict(dict)

    for p in code_dir.glob("*.css.*"):
        name, _ , longext    = p.name.partition(".css.")
        name                 = name[len(projname)+1:]
        cssname, _ , srcname = name.partition("-")

        csspaths[cssname][srcname] = p

    main_contents = defaultdict(list)

    for cssname, srcinfos in csspaths.items():
        for srcname in sorted(srcinfos):
            main_contents[cssname].append(
                srcinfos[srcname].read_text()
            )

    for cssname, contents in main_contents.items():
        contents = "\n\n\n".join(contents)
        contents = prettify_all_titles(contents)

        cssmainfile = code_dir / f"{projname}-{cssname}.css.cls"
        cssmainfile.write_text(contents)

    for cssname, srcinfos in csspaths.items():
        for srcname in sorted(srcinfos):
            srcinfos[srcname].unlink()

    projfile = code_dir / f"{projname}.cls"

    cleaned_content = []

    all_cssnames = list(csspaths)

    keep = True
    for line in projfile.read_text().split('\n'):
        short_line = line.strip()

        if not keep and not short_line:
            keep = True
            continue

        keep = True

        for cssname in all_cssnames:
            if short_line.startswith(
                 f"\\input{{{projname}-\\{projname}@theme-main"
            ):
                line = f"\\input{{{projname}-\\{projname}@theme.css.cls}}"

            elif short_line.startswith(
               f"\\input{{{projname}-\\{projname}@theme-"
            ):
                keep = False
                break

        if keep:
            cleaned_content.append(line)

    cleaned_content = "\n".join(cleaned_content)

    projfile.write_text(cleaned_content)
