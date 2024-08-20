# Define file paths
$distFolderPath = "D:\Dev\projects\html_label_inspect\dist"
$frontendPath = "D:\Dev\projects\html_label_inspect_backend\frontend"
$mainPyPath = "D:\Dev\projects\html_label_inspect_backend\main.py"
$getLabelInfosPyPath = "D:\Dev\projects\html_label_inspect_backend\get_label_infos.py"
$saveLabelInfoPyPath = "D:\Dev\projects\html_label_inspect_backend\save_label_info.py"

# Backup files before modifying
$mainPyBackup = "$mainPyPath.bak"
Copy-Item -Path $mainPyPath -Destination $mainPyBackup -Force

$getLabelInfosPyBackup = "$getLabelInfosPyPath.bak"
Copy-Item -Path $getLabelInfosPyPath -Destination $getLabelInfosPyBackup -Force

$saveLabelInfoPyBackup = "$saveLabelInfoPyPath.bak"
Copy-Item -Path $saveLabelInfoPyPath -Destination $saveLabelInfoPyBackup -Force

try {
    # Step 1: Copy dist folder to the backend's frontend directory
    Copy-Item -Path $distFolderPath -Destination $frontendPath -Recurse -Force

    # Step 2: Modify "frontend/dist/assets" in main.py
    $mainPyContent = Get-Content -Path $mainPyPath
    $mainPyContent = $mainPyContent -replace "frontend/dist/assets", "/code/frontend/dist/assets"
    $mainPyContent | Set-Content -Path $mainPyPath

    # Step 3: Modify paths in get_label_infos.py
    $getLabelInfosContent = Get-Content -Path $getLabelInfosPyPath
    $getLabelInfosContent = $getLabelInfosContent -replace "root_path = 'test'", "root_path = '/data/aisvc_data/intern2024_2/NLP_paper/label_data'"
    $getLabelInfosContent = $getLabelInfosContent -replace "test.db", "/data/aisvc_data/intern2024_2/NLP_paper/label_data/label_info.db"
    # $getLabelInfosContent = $getLabelInfosContent -replace "test/saved_img", "/data/aisvc_data/intern2024_2/NLP_paper/label_data/saved_img"
    $getLabelInfosContent | Set-Content -Path $getLabelInfosPyPath

    # Step 4: Modify paths in save_label_info.py
    $saveLabelInfoContent = Get-Content -Path $saveLabelInfoPyPath
    $saveLabelInfoContent = $saveLabelInfoContent -replace "root_path = 'test'", "root_path = '/data/aisvc_data/intern2024_2/NLP_paper/label_data'"
    $saveLabelInfoContent = $saveLabelInfoContent -replace "test.db", "/data/aisvc_data/intern2024_2/NLP_paper/label_data/label_info.db"
    # $saveLabelInfoContent = $saveLabelInfoContent -replace "test/saved_img", "/data/aisvc_data/intern2024_2/NLP_paper/label_data/saved_img"
    $saveLabelInfoContent | Set-Content -Path $saveLabelInfoPyPath

    # Step 5: Build Docker image with user-defined tag
    $imageTag = Read-Host "Enter Docker image tag (e.g., hli:1.0.0)"
    docker build -t $imageTag .

    if ($LASTEXITCODE -eq 0) {
        Write-Output "Docker build succeeded."
    } else {
        Write-Error "Docker build failed. Not reverting changes."
        exit 1
    }

    # Step 6: Restore original files
    Copy-Item -Path $mainPyBackup -Destination $mainPyPath -Force
    Copy-Item -Path $getLabelInfosPyBackup -Destination $getLabelInfosPyPath -Force
    Copy-Item -Path $saveLabelInfoPyBackup -Destination $saveLabelInfoPyPath -Force

    Write-Output "All modifications have been reverted successfully."

    # Step 7: docker save
    Write-Output "Save Start!"
    docker save $imageTag -o hli.tar
    Write-Output "saved successfully."

} catch {
    Write-Error "An error occurred: $_"
    Write-Error "Reverting to original files."

    # Restore original files on error
    Copy-Item -Path $mainPyBackup -Destination $mainPyPath -Force
    Copy-Item -Path $getLabelInfosPyBackup -Destination $getLabelInfosPyPath -Force
    Copy-Item -Path $saveLabelInfoPyBackup -Destination $saveLabelInfoPyPath -Force
} finally {
    # Cleanup: Remove backup files
    Remove-Item -Path $mainPyBackup, $getLabelInfosPyBackup, $saveLabelInfoPyBackup -Force
}
