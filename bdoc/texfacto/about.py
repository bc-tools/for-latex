from yaml import safe_load

def buildtoc(
    source,
    allfiles
):
    src_about = source / "about.yaml"

    if not src_about in allfiles:
        return allfiles[:]

    with src_about.open(
        encoding='utf8',
        mode='r',
    ) as f:
        about_cfg = safe_load(f)

    print(about_cfg['toc'])

    exit()
