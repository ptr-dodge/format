-- Function to remove comment lines and trailing whitespace from a file
function rape(file_name)
    local file = io.open(file_name, "r")  -- Open the file for reading
    if not file then
        print("File not found or could not be opened.")
        return
    end

    local lines = {}  -- Store lines without comments or trailing whitespace

    -- Process each line in the file
    for line in file:lines() do
        -- Remove comment lines and trailing whitespace
        local cleaned_line = line:gsub("^%s*#.*", "")  -- Remove lines starting with #
        cleaned_line = cleaned_line:gsub("^%s*//.*", "")  -- Remove lines starting with //
        cleaned_line = cleaned_line:gsub("^%s*'''.*", "")  -- Remove lines starting with '''
        cleaned_line = cleaned_line:gsub("^%s*\"\"\".*", "")  -- Remove lines starting with """
        cleaned_line = cleaned_line:gsub("^%s*'.*", "")  -- Remove lines starting with '
        cleaned_line = cleaned_line:gsub("^%s*rem%s+.*", "")  -- Remove lines starting with rem
        cleaned_line = cleaned_line:gsub("%s+$", "")  -- Remove trailing whitespace

        if #cleaned_line > 0 then
            table.insert(lines, cleaned_line)  -- Add cleaned line to the list
        end
    end

    file:close()  -- Close the file

    -- Write modified content back to the file
    local output_file = io.open(file_name, "w")
    if not output_file then
        print("Failed to open the output file.")
        return
    end

    -- Write the modified content (without comments or trailing whitespace) to the file
    output_file:write(table.concat(lines, "\n"))
    output_file:close()

    print("Comments and trailing whitespace removed successfully.")
end

-- Usage: Pass the file name as an argument when running the script
local file_to_modify = arg[1]
if not file_to_modify then
    print("Please provide the file name as an argument.")
    return
end

rape(file_to_modify)
