\NeedsTeXFormat{LaTeX2e}

\ProvidesClass{mylang}[2014/08/16 Example LaTeX class]

\LoadClassWithOptions{article}[2022-06-01]

\AtBeginDocument{
  \newcommand\tdoclang{\BCPdata{language}}
}
