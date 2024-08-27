from .constants import *
from .misc      import *


# --------------------------- #
# -- END IS COMING SOON... -- #
# --------------------------- #

def finalize(metadata):
# Useful.
    proj_name = metadata[TAG_PROJ_NAME]

    temp_dir    = metadata[TAG_TEMP]
    rollout_dir = metadata[TAG_ROLLOUT]

# STY file.
    code_dir  = rollout_dir / "code"

    emptydir(code_dir)

    print("+ Building STY file.")

    code_file = code_dir / f"{proj_name}.sty"

    code = [sty_header(metadata)]

    for kind, temp_file in [
        ("PACKAGES USED"    , TAG_TMP_STY_IMPORT),
        ("AVAILABLE OPTIONS", TAG_TMP_STY_OPTIONS),
        ("MAIN CODE"        , TAG_TMP_STY_SRC),
    ]:
        code.append(
            f"""
% == {kind} == %

{(temp_dir / temp_file).read_text()}
            """.rstrip()
        )

    code = '\n\n'.join(code)
    code = code.strip()

    code = pretty_title(code)

    code_file.write_text(code)

    print("+ Copying STY resources.")

    for resrc in temp_dir.glob("*.sty"):
        if resrc.name[0] == '.':
            continue

        copyfromto(
            srcfile  = resrc,
            destfile = code_dir / resrc.name
        )

# TEX files.
    print()

    doc_dir  = rollout_dir / "doc"

    emptydir(doc_dir)






def sty_header(metadata):
# About
    about = SRC_CODE_HEADER

    for old, new in {
        'PROJ_NAME'    : metadata[TAG_PROJ_NAME],
        'CREATION_YEAR': metadata[TAG_CREATION][TAG_YEAR],
        'LAST_YEAR'    : metadata[TAG_VERSIONS][TAG_LAST][TAG_YEAR],
        'AUTHOR'       : metadata[TAG_AUTHOR],
    }.items():
        about = about.replace(f"<<{old}>>", new)

    about = about.split('\n')

    max_len = max(len(l) for l in about)

    for i, line in enumerate(about):
        line += ' ' * (max_len - len(line))
        line  = f"% -- {line} -- %"

        about[i] = line

    about = '\n'.join(about)

    deco =  '-' * (max_len + 6)
    deco  = f"% {deco} %"

    about = f"""
{deco}
{about}
{deco}
    """.strip()

# Provide package
    provide = SRC_CODE_PROVIDE_PACK

    for old, new in {
        'PROJ_NAME'    : metadata[TAG_PROJ_NAME],
        'CREATION_DATE': nb_date_EN(metadata[TAG_CREATION]),
        'LAST_DATE'    : nb_date_EN(metadata[TAG_VERSIONS][TAG_LAST]),
        'LAST_NB_VER'  : metadata[TAG_VERSIONS][TAG_LAST][TAG_NB],
        'SHORT_DESC'   : metadata[TAG_DESC],
    }.items():
        provide = provide.replace(f"<<{old}>>", new)

    return f"""
{about}

{provide}
    """.strip()


def pretty_title(code):
    new_code   = []
    not_ignore = False

    for line in code.split('\n'):
        if line == r"\ProvidesExplPackage":
            not_ignore = True

        if not_ignore:
            for pattern in TITLE_PATTERNS:
                match = re.search(pattern, line)

                if match:
                    title     = match.group(2)
                    pre_deco  = match.group(1)
                    # post_deco = match.group(3)

                    deco = pre_deco[0] * (len(title) + 6)
                    deco = f"% {deco} %"

                    line = f"""
{deco}
{line}
{deco}
                    """.strip()

                    break

        new_code.append(line)

    new_code = '\n'.join(new_code)

    return new_code
