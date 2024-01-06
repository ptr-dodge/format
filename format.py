import re
import sys

# Define the comment patterns
comment_patterns = [
    r'^\s*#.*$',           # Python-style comment
    r'^\s*//.*$',          # Double-slash comment
    r'^\s*--.*$',          # Double-dash comment
    r'/\*.*?\*/',          # C-style block comments
    r"'''.*?'''",          # Triple single quotes for a comment (Start)
    r".*'''\s*$",          # Triple single quotes for a comment (End)
    r'^\s*;.*$',           # Semicolon style comment
    r'^\s*rem\s.*$',       # Windows 'rem' comment
    r'^\s*<!--.*?-->$',    # HTML comment
    r'^\s*//\s*Comment.*$',# JavaDoc-style comments
    r'^\s*\(%*.*%*\)$',    # Pascal-style comments
]

# Read text from the specified file (sys.argv[1])
file_name = sys.argv[1]
with open(file_name, "r+") as file:
    content = file.read()
    file.seek(0)  # Move cursor to the beginning of the file

    lines = content.split('\n')
    modified_content = []
    in_multiline_comment = False

    for line in lines:
        skip_line = False

        if re.match(r'/\*.*', line):  # C-style block comment start
            in_multiline_comment = True
            skip_line = True

        if re.match(r'.*\*/\s*$', line):  # C-style block comment end
            in_multiline_comment = False
            skip_line = True

        if re.match(r"'''.*", line):  # Triple single quotes for a comment (Start)
            in_multiline_comment = not in_multiline_comment
            skip_line = True

        if re.match(r".*'''\s*$", line):  # Triple single quotes for a comment (End)
            in_multiline_comment = not in_multiline_comment
            skip_line = True

        if in_multiline_comment:
            skip_line = True
        else:
            for pattern in comment_patterns:
                if re.match(pattern, line):
                    skip_line = True
                    break

        if not skip_line:
            modified_content.append(line)

    file.write('\n'.join(modified_content))
    file.truncate()
