---------------------------
-- REOP. COMMON SETTINGS --
---------------------------

module = "l3build-xtras"

sourcefiledir = "code"
sourcefiles   = {"*.cls", "*.sty"}

docfiledir   = "doc"
typesetfiles = {"*.tex"}

testfiledir = "tests"

checkopts   = "-interaction=nonstopmode --shell-escape"
typesetopts = checkopts


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
