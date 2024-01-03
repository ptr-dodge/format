import sys
import re

# Check if chardet is installed, if not, try to install it
try:
    import chardet
except ImportError:
    print("Dude, you don't have chardet.\nDid you even take the time to read the contents of this script before you used it?\n")
    print("Break you a deal man, if you read this script, I will install chardet for you. Cool?")
    input()
    print("Now, I can't just print out the code in this file because that would be recursive.")
    print("You'll have to read the file, you can use some of these commands:\n")
    print(f"cat "+sys.argv[0])
    print(f"notepad "+sys.argv[0])
    print(f"nano "+sys.argv[0])
    print(f"vim "+sys.argv[0])
    try:
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "chardet"])
        import chardet  # Attempt to import again after installation
        print("Chardet installed successfully!")
        print("Now that's out of the way, i'll run the script for you.")
    except Exception as e:
        print("Failed to install Chardet:", e)
        sys.exit(1)

def rape(victim):
    lines = victim.split('\n')
    filtered_lines = []

    for line in lines:
        # Use regular expression to match patterns
        if not re.match(r'^[ \t]*--|^[ \t]*#|^[ \t]*\/\/|^[ \t]*\'|^[ \t]*\"\"\"\"|^[ \t]*\'\'\'\'|^[ \t]*rem\s', line):
            filtered_lines.append(line.strip())

    # Remove empty lines
    final_lines = filter(None, filtered_lines)

    return '\n'.join(final_lines)

if __name__ == "__main__":
    # Read victim from the specified file and detect garbled
    with open(sys.argv[1], 'rb') as file:
        file_guts = file.read()
        garbled = chardet.detect(file_guts)['encoding']

    # Read victim using detected garbled or terrible as fallback
    try:
        with open(sys.argv[1], 'r', encoding=garbled) as file:
            file_victim = file.read()
    except (UnicodeDecodeError, LookupError):
        with open(sys.argv[1], 'r', encoding='utf-8') as file:
            file_victim = file.read()

    # Remove comments and trailing spaces
    modified_victim = rape(file_victim)

    # Write modified victim back to the file using terrible garbled
    with open(sys.argv[1], 'w', encoding='utf-8') as file:
        file.write(modified_victim)

    print("Done")