-- Sources.
--     * https://www.latex-project.org/news/2019/04/16/l3build-upload/
--     * https://ctan.org/help/submit
--     * https://ctan.org/license
--     * https://ctan.org/topics/highscore
--     * https://ctan.org/incoming

module = "tutodoc"

sourcefiledir = "code"
sourcefiles   = {"*.sty"}

flatten    = false
flattentds = false

docfiledir   = "doc"
typesetfiles = {"*.tex"}
-- typesetsourcefiles = {"**/*"}

testfiledir = "tests"

checkopts   = "-interaction=nonstopmode --shell-escape"
-- checkopts   = "-interaction=batchmode --shell-escape"
typesetopts = checkopts

uploadconfig = {
    version      = "1.4.0 [2024-09-28]",
    announcement = "New macros \\tdocstartproj and \\tdocicon + Breaking changes for \\tdoccaution, \\tdocexa and \\tdocrem.",
    author       = "Christophe BAL",
    uploader     = "Christophe BAL",
    email        = "projetmbc@gmail.com",
    license      = "gpl3",
    pkg          = "tutodoc",
    -- update       = false,
    summary      = 'This package proposes tools for writing "human friendly" documentations of LaTeX packages.',
    topic        = {"doc-tool"},
    ctanPath     = "/macros/latex/contrib/tutodoc",
    repository   = "https://github.com/bc-tools/for-latex",
    bugtracker   = "https://github.com/bc-tools/for-latex/issues",
    note         = [[Uploaded automatically by l3build...]]
}


------------------------------
-- New command line options --
------------------------------

VIEW_TAG = "view"

function viewPDF(xtra_args)
  if xtra_args == nil or #xtra_args ~= 1
  then
    print("One single tesfile name needed!")
    return 1
  end

  testfilename = xtra_args[1]
  pdffile = "build/test/" .. testfilename .. ".pdf"

  if fileexists(pdffile) == false
  then
    print("No PDF file found.\nSee: " .. pdffile)
    return 1
  end

  trycmd = run(".", "open " .. '"' .. pdffile .. '"')

  if trycmd ~= 0
  then
    print("No command to open PDF files.\nSee: " .. pdffile)
  end

  return 0
end

target_list[VIEW_TAG] = {
  func = viewPDF,
  desc = "Open a PDF of tested files",
--   pre = function(xtra_args)
--   end
}
