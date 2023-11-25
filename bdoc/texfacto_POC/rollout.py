def build_rollout_proj(patterns, tmpdir, rolloutdir):
    for texfile in tmpdir.glob("*.tex"):
        if texfile.name[0] == '.':
            continue

        destfile = rolloutdir / "doc" / texfile.name

        if destfile.is_file():
            destfile.unlink()

        destfile.touch()

        print(f"+ Analyzing {destfile.name}.")

        resources = {}

        with (
            destfile.open("w") as f_out,
            texfile.open("r") as f_in
        ):
            for line in f_in:
                newline = line

                for p in patterns:
                    match = p.findall(line)

                    if not match:
                        continue

                    start, comment, macroname, options, input_file, end = match[0]

                    if comment:
                        continue

                    for old in "./":
                        input_file_cleaned = input_file.replace(old, '-')


                    newline = f"{start}{macroname}{options}{{{input_file_cleaned}}}{end}\n"

                    if not input_file in resources:
                        resources[input_file] = input_file_cleaned

                    break

                f_out.write(newline)

        headcontents = []

        for rfile, rname in resources.items():
            with (tmpdir / rfile).open("r") as f:
                headcontents.append(
f"""
\\begin{{filecontents*}}{{{rname}}}
{f.read().lstrip()}
\\end{{filecontents*}}
"""
                )

        headcontents = "\n".join(headcontents)

        finaltex = headcontents + '\n'*2 + destfile.read_text()

        destfile.write_text(data = finaltex)
