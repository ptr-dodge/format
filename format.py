import re
import sys

# Define the comment patterns
comment_patterns = [
    r'^\s*#.*',
    r'^\s*//.*',
    r'^\s*--.*',
    r'^\s*/\*.*?\*/',
    r"^\s*'''.*?'''",
    r'^\s*;.*',
    r'^\s*rem\s.*',
    r'^\s*<!--.*?-->',
    r'^\s*/\*.*?\*/',
    r'^\s*\(\*.*?\*\)',
    r'^\s*//.*',
]

# Read text from the specified file (sys.argv[1])
file_name = sys.argv[1]
with open(file_name, 'r+') as file:
    lines = file.readlines()
    file.seek(0)  # Move cursor to the beginning of the file

    # Remove lines matching comment patterns and rewrite the file
    for line in lines:
        if not any(re.match(pattern, line) for pattern in comment_patterns):
            if line != '\n':
                print(line)
                file.write(line)

    file.truncate()  # Truncate any remaining content after the new written content
