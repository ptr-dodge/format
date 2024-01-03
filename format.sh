#!/bin/bash

tmp=".tmptext"
file="$1"

# Array of comment indicators
comments=( '#' '\/\/' "'" '\"\"\"' "'''" 'rem\s' )

# Copy the file content to the temporary file
cp "$file" "$tmp"

# Loop through each comment indicator and filter lines
for c in "${comments[@]}"; do
    grep -Ev "^\s*$c" "$tmp" > "$tmp.tmp"
    mv "$tmp.tmp" "$tmp"
done

# Remove leading and trailing spaces on each line
sed -i 's/^[[:space:]]*//; s/[[:space:]]*$//' "$tmp"

# Remove trailing newlines
sed -i -e :a -e '/^\n*$/{$d;N;ba' -e '}' -e '/^\n*$/d' "$tmp"

# Remove multiple consecutive newlines
sed -i '/^$/N;/^\n$/D' "$tmp"

mv "$tmp" "$file"
