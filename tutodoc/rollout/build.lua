-- Sources.
--     * https://www.latex-project.org/news/2019/04/16/l3build-upload/
--     * https://ctan.org/help/submit
--     * https://ctan.org/license
--     * https://ctan.org/topics/highscore
--     * https://ctan.org/incoming

module = "tutodoc"

sourcefiledir = "code"
sourcefiles   = {"*.cls", "*.cls.sty", "DEPENDS.yaml"}

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
    version      = "1.7.0 [2024-12-04]",
    announcement = "More robust environments for the changes indicated.",
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


---------------
-- DIFF TOOL --
---------------

DIFF_OPTION_SIDE_BY_SIDE  = "-y"
DIFF_OPTION_FULL_ONE_PAGE = "-u"


function diff_files(
    initial_name, initial_content,
    final_name  , final_content,
    options
)
    local initial_file = io.open(initial_name, "w")

    if initial_file == nil
    then
        return raiseFileNotCreated(initial_name)
    end

    local final_file = io.open(final_name, "w")

    if final_file == nil
    then
        os.remove(initial_file)

        return raiseFileNotCreated(final_name)
    end

    initial_file:write(initial_content)
    final_file:write(final_content)

    local iostream = assert(
        io.popen(
            "diff "
            -- .. DIFF_OPTION_SIDE_BY_SIDE ..
            .. DIFF_OPTION_FULL_ONE_PAGE ..
            " "
            .. initial_name ..
            " "
            .. final_name,
            'r'
        )
    )

    local infos = assert(iostream:read('a'))

    iostream:close()

    infos = string.gsub(infos, '^%s+', '')
    infos = string.gsub(infos, '%s+$', '')

    print("`diff -u test check` gives:")
    print("")

    print(infos)

    os.remove(initial_name)
    os.remove(final_name)

    return false
end


--------------------
-- RAISING ERRORS --
--------------------

function raise(kind, message)
    print("")
    print(kind .. ".ERROR! " .. message)

    return 1
end

function raiseFileNotCreated(file_name)
    return raise(
        "IO",
        "File ''" .. file_name .. "'' can't be created."
    )
end


-------------------
-- CMD UTILITIES --
-------------------

function helper(
    xtra_args,
    text_helper
)
    if (
        #xtra_args == 1
        and
        (
            xtra_args[1] == "@"
            or
            xtra_args[1] == "@@bout"
        )
    )
    then
        print(text_helper)
        return 0
    end

    return nil
end


--------------------------------
-- L3BUILD EXTRA CMD "sbunit" --
--------------------------------

----
-- This extra unit-testing command validates [s]how[b]ox comparisons?
--
-- Source.
--    + l3build use of \showbox: https://tex.stackexchange.com/a/729463/6880
----

SBUNIT_HELPER = [[
l3build extra command "sbunit"

    GGGG
]]

cmd_option = "sbunit"

TAG_CHECK  = "check"
TAG_IGNORE = "standard"
TAG_TEST   = "test"

TAG_L3BUILD_BOX_START = "> \\box"
TAG_L3BUILD_BOX_END   = "! OK."

function checkSBUNIT(xtra_args)
    if (
        xtra_args == nil
        or (
            #xtra_args == 0
            or
            #xtra_args > 1
        )
    )
    then
        return raise(
            "IO",
            "One single test file name needed!"
        )
    end

    -- local help =

    if helper(
        xtra_args,
        SBUNIT_HELPER
    ) ~= nil
    then
        return 0
    end

    print("SHOWBOX COMPARISON CHECKING\n")

    local testfilename = xtra_args[1]
    local logfile      = testfilename .. ".log"

    local file  = io.open(testdir .. "/" .. logfile)
    local lines = file:lines()

    local nbline = 0

    local nbtests = 0
    local kind    = TAG_IGNORE

    local line_test = -1
    local log_test  = ""

    local line_check = -1
    local log_check  = ""

    for line in lines
    do
        nbline    = nbline + 1
        startline = string.sub(line, 1, 9)

        if startline == "SB-TESTED"
        then
            line_test = nbline
            kind      = TAG_TEST
            catego    = string.sub(line, 11, -1)

        elseif startline == "SB-WANTED"
        then
            if catego ~= string.sub(line, 11, -1)
            then
                return raise(
                    "FORMAT",
                    "Showbox checker without a showbox tested: see line "
                    .. nbline ..
                    " in the log file. Tested? Same category"
                )
            end


            line_check = nbline
            kind       = TAG_CHECK

        elseif line == TAG_L3BUILD_BOX_END
        then
            if kind == TAG_CHECK
            then
                error_code = _compareSBUNIT(
                    catego,
                    line_test , log_test,
                    line_check, log_check
                )

                if error_code == 1
                then
                    return error_code
                end

                if error_code == false
                then
                    return raise(
                        "TEST",
                        "Validation has failed!"
                    )
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

    print("\nSHOWBOX COMPARISON FINISHED.")

    return 0
end


target_list[cmd_option] = {
    func = checkSBUNIT,
    desc = "Check showbox comparison unit test",
--   pre = function(xtra_args)
--   end
}


function _compareSBUNIT(
    catego,
    line_test , log_test,
    line_check, log_check
)
    local what   = "Showbox " .. catego

-- Happy day!
    if log_test == log_check
    then
        result = true

        print("    + [OK] " .. what)

        return true
    end

-- Chaos day...
    print("    + [KO] " .. what)

    print("LOG FILE. Test starts at line " .. line_test .. ".")
    print("          Check starts at line " .. line_check .. ".")

    diff_files(
        "build/test/" .. "@_@test_@_l3build@_@",
        log_test,
        "build/test/" .."@_@check_@_l3build@_@",
        log_check,
        nil
    )
end


------------------------------
-- L3BUILD EXTRA CMD "view" --
------------------------------

----
-- This extra command allow to quickly view one PDF associated to one test.
----
cmd_option = "view"

function viewPDF(xtra_args)
    if xtra_args == nil or #xtra_args ~= 1
    then
        return raise(
            "IO",
            "One single test file name needed!"
        )
    end

    local testfilename = xtra_args[1]

    -- cfr: use the variable in case builddir isn't this directory
    local pdffile = testfilename .. ".pdf"

    if fileexists(testdir .. "/" .. pdffile) == false
    then
        return raise(
            "IO",
            "No PDF file found.\nSee: " .. pdffile
        )
    end

-- Works on Linux, but not MacOS
    local trycmd = run(testdir, "xdg-open " .. '"' .. pdffile .. '"')

    if trycmd ~= 0 then
-- Works on MacOS, but not on Linux.
      trycmd = run(testdir, "open " .. '"' .. pdffile .. '"')

      if trycmd ~= 0
      then
          return raise(
              "OS",
              "No command to open PDF files.\nSee: " .. pdffile
          )
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


-------------------------------
-- L3BUILD EXTRA CMD "cplog" --
-------------------------------

----
-- This extra command simply copy luatex and xetex log files as tlg ones.
----
cmd_option = "cplog"

function cplog(xtra_args)
    if xtra_args == nil or #xtra_args ~= 1
    then
        return raise(
            "IO",
            "One single test file name needed!"
        )
    end

    local testfilename = xtra_args[1]

    local allexts = {"luatex", "xetex"}

    for _ , ext in ipairs(allexts) do
        local srclog_path = testdir .. "/" .. testfilename .. "." .. ext .. ".log"

        if fileexists(srclog_path) == false
        then
            return raise(
                "IO",
                "No xetex LOG file found.\nSee: " .. srclog_path
            )
        end

        local desttlg_path = testfiledir .. "/" .. testfilename .. "." .. ext .. ".tlg"

        local srcfile = io.open(srclog_path, "r")
        srcfile_content = srcfile:read("*a")
        srcfile:close()

        local destfile = io.open(desttlg_path, "w")
        destfile:write(srcfile_content)
        destfile:close()
    end

    return 0
end


target_list[cmd_option] = {
    func = cplog,
    desc = "Copy luatex and xetex lof files as tlg ones",
--   pre = function(xtra_args)
--   end
}
