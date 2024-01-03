# format.ps1
# Powershell script to remove comments from files
# also removes extra spaces, tabs, and newlines.
# Comments supported: #, //, ', """, ''', REM, 

# set parameters for this file
param (
    [string]$file
)

# set variable to store the content of input file
$content = Get-Content $file

# loop through each line and search for things we don't want
$filteredContent = foreach ($line in $content) {
    if (-not ($line -match '^[ 	]*#|^[ 	]*\/\/|^[ 	]*''|^[ 	]*""""|^[ 	]*''''|^[ 	]*rem\s')) {
        # If these aren't the case, then we return the line.
        $line.Trim()
    }
}

# more filtering
$finalContent = $filteredContent -ne ''
# write to the same file
Set-Content -Path $file -Value $finalContent
