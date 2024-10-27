-- Sources.
--     * https://www.latex-project.org/news/2019/04/16/l3build-upload/
--     * https://ctan.org/help/submit
--     * https://ctan.org/license
--     * https://ctan.org/topics/highscore
--     * https://ctan.org/incoming

module = "tutodoc"

sourcefiledir = "code"
sourcefiles   = {"*.cls", "*.cls.sty"}

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
    version      = "1.6.0 [2024-10-26]",
    announcement = "The main change is the ability to choose a layout from 4 themes.",
    author       = "Christophe BAL",
    uploader     = "Christophe BAL",
    email        = "projetmbc@gmail.com",
    license      = "gpl3",
    pkg          = "tutodoc",
    -- update       = false,
    summary      = 'This class proposes tools for writing "human friendly" documentations of LaTeX packages.',
    topic        = {"doc-tool"},
    ctanPath     = "/macros/latex/contrib/tutodoc",
    repository   = "https://github.com/bc-tools/for-latex",
    bugtracker   = "https://github.com/bc-tools/for-latex/issues",
    note         = [[Uploaded automatically by l3build...]]
}


-----------------
-- CMD OPTIONS --
-----------------

-- UNIT TESTS: AUTO VALIDATIONS OF [S]HOW[B]OX COMPARISONS --

cmd_option = "sbunit"

function checkSBUNIT(xtra_args)
    if xtra_args == nil or #xtra_args ~= 1
    then
        print("Showbox comparison unit test: one single test file name needed!")
        return 1
    end

    print("Starting validation of SHOWBOX COMPARISON unit tests.")

    local testfilename = xtra_args[1]
    local logfile      = testfilename .. ".log"

    file  = io.open(testdir .. "/" .. logfile)
    lines = file:lines()

    local nbline = 0

    TAG_CHECK = "check"
    TAG_STD   = "standard"
    TAG_TEST  = "test"

    TAG_L3BUILD_BOX = "> \\box"
    local nbtests = 0
    local kind    = "std"


    for line in lines
    do
        nbline = nbline + 1

        startline = string.sub(line, 1, 9)

        if startline == "SB-TESTED"
        then
            kind   = TAG_TEST
            catego = string.sub(line, 11, -1)

        elseif startline == "SB-WANTED"
        then
            if kind ~=  TAG_TEST
            then
                print("No showbox tested before: see line " .. nbline .. " in the log file.")
                return 1
            end

            if catego ~= string.sub(line, 11, -1)
            then
                print("Showbox checker without the same category: see line " .. nbline .. " in the log file.")
                return 1
            end

            kind = TAG_CHECK
        elseif line == "! OK."
        then
            kind = TAG_STD
            print("--- LET'S WORK! --")
        elseif kind == TAG_TEST or kind == TAG_CHECK
        then
            if string.sub(line, 0, 6) ~= TAG_L3BUILD_BOX
            then
                print("\t[" .. nbline .. "-" .. kind .. "]" .. line)
            end
        end
    end


  return 0
end


target_list[cmd_option] = {
    func = checkSBUNIT,
    desc = "Check showbox comparison unit test",
--   pre = function(xtra_args)
--   end
}


-- VIEW PDF FROM ONE TEST --

cmd_option = "view"

function viewPDF(xtra_args)
    if xtra_args == nil or #xtra_args ~= 1
    then
        print("View PDF from one test: one single test file name needed!")
        return 1
    end

    local testfilename = xtra_args[1]

    -- cfr: use the variable in case builddir isn't this directory
    local pdffile = testfilename .. ".pdf"

    if fileexists(testdir .. "/" .. pdffile) == false
    then
        print("No PDF file found.\nSee: " .. pdffile)
        return 1
    end

-- Works on Linux, but not MacOS
    local trycmd = run(testdir, "xdg-open " .. '"' .. pdffile .. '"')

    if trycmd ~= 0 then
-- Works on MacOS, but not on Linux.
      trycmd = run(testdir, "open " .. '"' .. pdffile .. '"')

      if trycmd ~= 0
      then
          print("No command to open PDF files.\nSee: " .. pdffile)
      end
    end

    return 0
end


target_list[cmd_option] = {
    func = viewPDF,
    desc = "Open a PDF of tested files",
--   pre = function(xtra_args)
--   end
}
