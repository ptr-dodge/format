-- Define the comment patterns
comment_patterns = {
    "^%s*#.-$",                  -- Python-style comment
    "^%s*//.-$",                 -- Double-slash comment
    "^%s*%-%-.-$",               -- Double-dash comment
    "^%s*/%*.-%*/$",             -- C-style block comments
    "^%s*'''.-$",                -- Triple single quotes for a comment (Start)
    "^.-'''$",                   -- Triple single quotes for a comment (End)
    "^%s*;.-$",                  -- Semicolon style comment
    "^%s*rem%s.-$",              -- Windows 'rem' comment
    "^%s*<!--.- -->$",           -- HTML comment
    "^%s*//%s*Comment.-$",      -- JavaDoc-style comments
    "^%s*%(%*.-%*%)$"           -- Pascal-style comments
}

-- Read text from the specified file (given as the first argument)
file_name = arg[1]
file = io.open(file_name, "r")
if file then
    local lines = file:read("*all")
    file:seek("set")  -- Move cursor to the beginning of the file

    local modified_content = {}
    local in_multiline_comment = false
    for line in lines:gmatch("[^\r\n]+") do
        local skip_line = false

        if line:match("^%s*/%*.-$") then
            in_multiline_comment = true
            skip_line = true
        elseif line:match(".-%*/$") then
            in_multiline_comment = false
            skip_line = true
        end

        if line:match("^%s*'''.-$") then
            in_multiline_comment = not in_multiline_comment
            skip_line = true
        end

        if in_multiline_comment then
            skip_line = true
        else
            for _, pattern in ipairs(comment_patterns) do
                if line:match(pattern) then
                    skip_line = true
                    break
                end
            end
        end

        if not skip_line then
            table.insert(modified_content, line)
        end
    end

    file:write(table.concat(modified_content, "\n"))
    file:close()

    -- Open the file again in write mode and rewrite its content
    file = io.open(file_name, "w")
    file:write(table.concat(modified_content, "\n"))
    file:close()
else
    print("File not found or unable to open.")
end
