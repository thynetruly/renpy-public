$projectRoot = "C:\Users\thyne\rerenpy\renpy"
$outputFile = "directory_structure.md"

function Get-DirectoryTree {
    param (
        [string]$path,
        [string]$prefix = "",
        [bool]$isLast = $true
    )

    $name = Split-Path $path -Leaf
    
    if ($prefix -eq "") {
        $treeLine = $name
    } else {
        $treeLine = "$prefix$(if ($isLast) { '└── ' } else { '├── ' })$name"
    }
    
    $treeLine

    $items = Get-ChildItem -Path $path -Directory | Sort-Object Name
    $count = $items.Count

    for ($i = 0; $i -lt $count; $i++) {
        $item = $items[$i]
        $newPrefix = $prefix + $(if ($isLast) { "    " } else { "│   " })
        $isLastChild = ($i -eq $count - 1)
        Get-DirectoryTree -path $item.FullName -prefix $newPrefix -isLast $isLastChild
    }
}

# Create the Markdown content
$markdownContent = @"
``````
$(Get-DirectoryTree -path $projectRoot)
``````
"@

# Write the content to the file
$markdownContent | Out-File -FilePath $outputFile -Encoding utf8

Write-Host "Markdown file created: $outputFile"
