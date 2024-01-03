param (
    [string]$file
)

$content = Get-Content $file
$filteredContent = foreach ($line in $content) {
    if (-not ($line -match '^[ 	]*#|^[ 	]*\/\/|^[ 	]*''|^[ 	]*""""|^[ 	]*''''|^[ 	]*rem\s')) {
        $line.Trim()
    }
}

$finalContent = $filteredContent -ne ''
Set-Content -Path $file -Value $finalContent
