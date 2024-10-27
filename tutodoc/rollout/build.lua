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

-- Source for l3build use of \showbox: https://tex.stackexchange.com/a/729463/6880

cmd_option = "sbunit"

TAG_CHECK  = "check"
TAG_IGNORE = "standard"
TAG_TEST   = "test"

TAG_L3BUILD_BOX_START = "> \\box"
TAG_L3BUILD_BOX_END   = "! OK."


function checkSBUNIT(xtra_args)
    if xtra_args == nil or #xtra_args ~= 1
    then
        print(
            "IO.ERROR!"
            ..
            "One single test file name needed!"
        )

        return 1
    end

    print("Starting validation of SHOWBOX COMPARISON unit tests.")

    local testfilename = xtra_args[1]
    local logfile      = testfilename .. ".log"

    local file  = io.open(testdir .. "/" .. logfile)
    local lines = file:lines()

    local nbline = 0

    local nbtests = 0
    local kind    = TAG_IGNORE

    local log_test  = ""
    local log_check = ""

    for line in lines
    do
        nbline    = nbline + 1
        startline = string.sub(line, 1, 9)

        if startline == "SB-TESTED"
        then
            kind   = TAG_TEST
            catego = string.sub(line, 11, -1)

        elseif startline == "SB-WANTED"
        then
            if catego ~= string.sub(line, 11, -1)
            then
                print(
                    "Showbox checker without a showbox tested: see line "
                    .. nbline ..
                    " in the log file. Tested? Same category"
                )

                return 1
            end

            kind = TAG_CHECK

        elseif line == TAG_L3BUILD_BOX_END
        then
            if kind == TAG_CHECK
            then
                if _compareSBUNIT(catego, log_test, log_check) == false
                then
                    print("\nValidation has failed!")
                    return 1
                end
            end

            kind = TAG_IGNORE

        elseif string.sub(line, 0, 6) ~= TAG_L3BUILD_BOX_START
        then
            if kind == TAG_TEST
            then
                log_test = log_test .. "\n" .. line

            elseif kind == TAG_CHECK
            then
                log_check = log_check .. "\n" .. line
            end
        end
    end

    print("\nSuccessful validation.")
    return 0
end


target_list[cmd_option] = {
    func = checkSBUNIT,
    desc = "Check showbox comparison unit test",
--   pre = function(xtra_args)
--   end
}


function _compareSBUNIT(catego, log_test, log_check)
    local what   = "Showbox " .. catego
    local result = false

    if log_test == log_check
    then
        result = true

        print("    + " .. what .. " [OK]")

      else
        print("    + " .. what .. " [KO]")
    end

    return result
end


-- VIEW PDF FROM ONE TEST --

cmd_option = "view"

function viewPDF(xtra_args)
    if xtra_args == nil or #xtra_args ~= 1
    then
        print(
            "IO.ERROR!"
            ..
            "One single test file name needed!"
        )

        return 1
    end

    local testfilename = xtra_args[1]

    -- cfr: use the variable in case builddir isn't this directory
    local pdffile = testfilename .. ".pdf"

    if fileexists(testdir .. "/" .. pdffile) == false
    then
        print(
            "IO.ERROR!"
            ..
            "No PDF file found.\nSee: " .. pdffile
        )

        return 1
    end

-- Works on Linux, but not MacOS
    local trycmd = run(testdir, "xdg-open " .. '"' .. pdffile .. '"')

    if trycmd ~= 0 then
-- Works on MacOS, but not on Linux.
      trycmd = run(testdir, "open " .. '"' .. pdffile .. '"')

      if trycmd ~= 0
      then
          print(
              "OS.ERROR!"
              ..
              "No command to open PDF files.\nSee: " .. pdffile
          )

          return 1
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
