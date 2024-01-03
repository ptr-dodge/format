import sys
import re

# Check if chardet is installed, if not, try to install it
try:
    import chardet
except ImportError:
    print("Chardet library not found. Attempting to install...")
    try:
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "chardet"])
        import chardet  # Attempt to import again after installation
        print("Chardet installed successfully!")
    except Exception as e:
        print("Failed to install Chardet:", e)
        sys.exit(1)

def remove_comments_and_trailing_spaces(content):
    lines = content.split('\n')
    filtered_lines = []

    for line in lines:
        # Use regular expression to match patterns
        if not re.match(r'^[ \t]*#|^[ \t]*\/\/|^[ \t]*\'|^[ \t]*\"\"\"\"|^[ \t]*\'\'\'\'|^[ \t]*rem\s', line):
            filtered_lines.append(line.strip())

    # Remove empty lines
    final_lines = filter(None, filtered_lines)

    return '\n'.join(final_lines)

if __name__ == "__main__":
    # Read content from the specified file and detect encoding
    with open(sys.argv[1], 'rb') as file:
        raw_data = file.read()
        encoding = chardet.detect(raw_data)['encoding']

    # Read content using detected encoding or utf-8 as fallback
    try:
        with open(sys.argv[1], 'r', encoding=encoding) as file:
            file_content = file.read()
    except (UnicodeDecodeError, LookupError):
        with open(sys.argv[1], 'r', encoding='utf-8') as file:
            file_content = file.read()

    # Remove comments and trailing spaces
    modified_content = remove_comments_and_trailing_spaces(file_content)

    # Write modified content back to the file using UTF-8 encoding
    with open(sys.argv[1], 'w', encoding='utf-8') as file:
        file.write(modified_content)
