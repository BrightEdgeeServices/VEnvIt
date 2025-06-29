# Install-Conclude.psm1

if (Get-Module -Name "Conclude-UpgradePrep") { Remove-Module -Name "Conclude-UpgradePrep" }
Import-Module $PSScriptRoot\..\src\Conclude-UpgradePrep.psm1
if ((Get-Module -Name "Utils") -and $Pester ) {
    if (Test-Path ) { Copy-Item -Path function:prompt -Destination function:bakupPrompt }
    if (Test-Path function:_OLD_VIRTUAL_PROMPT) { Copy-Item function:_OLD_VIRTUAL_PROMPT -Destination function:backup_OLD_VIRTUAL_PROMPT }
    Remove-Module -Name "Utils"
    if (Test-Path function:function:bakupPrompt) { Copy-Item -Path function:bakupPrompt -Destination function:prompt }
    if (Test-Path function:backup_OLD_VIRTUAL_PROMPT) { Copy-Item -Path function:backup_OLD_VIRTUAL_PROMPT -Destination function:_OLD_VIRTUAL_PROMPT }
}
Import-Module $PSScriptRoot\Utils.psm1
$separator = "-" * 80

function Clear-InstallationFiles {
    param (
        [string]$upgradeScriptDir
    )
    Remove-Item -Path $upgradeScriptDir -Force -Recurse
    Write-Host "Installation files has been deleted." -ForegroundColor Green
}

function Invoke-ConcludeInstall {
    param (
        [string]$UpgradeScriptDir
    )
    if (Get-Module -Name "Utils") { Remove-Module -Name "Utils" }
    Import-Module $PSScriptRoot\Utils.psm1

    # Check for administrative privileges
    if (-not (Test-Admin)) {
        Write-Host "This script needs to be run as an administrator. Please run it in an elevated PowerShell session." -ForegroundColor Red
        Invoke-CleanUp
        exit
    }

    Update-PackagePrep $UpgradeScriptDir
    Write-Host $separator -ForegroundColor Cyan
    Get-ReadAndSetEnvironmentVariables -EnvVarSet $defEnvVarSet_7_0_0
    Set-Path
    Write-Host "Environment variables have been set successfully." -ForegroundColor Green
    Install-PythonRepository -Major "3" -Minor "13" -Patch "3"
    $venvPythonPath = Install-PythonVirtualEnv -Major "3" -Minor "13" -Patch "3"
    New-Directories -EnvVarSet $defEnvVarSet_7_0_0
    Publish-LatestVersion -UpgradeSourceDir $UpgradeScriptDir
    Publish-Secrets -UpgradeScriptDir $UpgradeScriptDir
    Write-Host $separator -ForegroundColor Cyan
    Get-Item "$env:VENVIT_DIR\*.ps1" | ForEach-Object { Unblock-File $_.FullName }
    Get-Item "$env:VENV_SECRETS_DEFAULT_DIR\secrets.ps1" | ForEach-Object { Unblock-File $_.FullName }
    Get-Item "$env:VENV_SECRETS_USER_DIR\secrets.ps1" | ForEach-Object { Unblock-File $_.FullName }
    Clear-InstallationFiles -UpgradeScriptDir $UpgradeScriptDir
    Write-Host "Installation and configuration are complete." -ForegroundColor Green
}

function Invoke-IsInRole {
    param (
        [Security.Principal.WindowsPrincipal]$Principal,
        [Security.Principal.WindowsBuiltInRole]$Role
    )
    return $Principal.IsInRole($Role)
}

function New-Directories {
    # Ensure the directories exist
    param(
        $EnvVarSet
    )
    foreach ($envVar in $envVarSet.Keys) {
        if ( $envVarSet[$envVar]["IsDir"]) {
            $dirName = [System.Environment]::GetEnvironmentVariable($envVar, [System.EnvironmentVariableTarget]::Machine)
            if (-not (Test-Path -Path $dirName)) {
                New-Item -ItemType Directory -Path $dirName | Out-Null
            }
        }
    }
}

function Publish-LatestVersion {
    param (
        $UpgradeSourceDir
    )
    if (Get-Module -Name "Utils") { Remove-Module -Name "Utils" }
    Import-Module $PSScriptRoot\Utils.psm1

    foreach ($filename in $sourceFileCompleteList) {
        $barefilename = Split-Path -Path $filename -Leaf
        Copy-Item -Path (Join-Path -Path $UpgradeSourceDir -ChildPath $filename) -Destination ("$env:VENVIT_DIR\$barefilename") | Out-Null
    }
}

function Publish-Secrets {
    param(
        [string]$UpgradeScriptDir
    )
    # Move the secrets.ps1 file from VENVIT_DIR to VENV_SECRETS_DIR if it does not already exist in VENV_SECRETS_DIR
    $copiedFiles = @()
    $directories = @( $env:VENV_SECRETS_DEFAULT_DIR, $env:VENV_SECRETS_USER_DIR )
    $sourcePath = Join-Path -Path ("$UpgradeScriptDir\src") -ChildPath (Get-SecretsFileName)
    foreach ($directory in $directories) {
        $destinationPath = Join-Path -Path $directory -ChildPath (Get-SecretsFileName)
        if ( -not(Test-Path -Path $destinationPath)) {
            Copy-Item -Path $sourcePath -Destination $destinationPath -Force
            $copiedFiles += $destinationPath
        }
    }
    return $copiedFiles
}

function Set-Path {
    # Add VENVIT_DIR to the System Path variable
    $path = [System.Environment]::GetEnvironmentVariable("Path", [System.EnvironmentVariableTarget]::Machine)
    if ($path -notlike "*$env:VENVIT_DIR*") {
        $newPath = "$path;$env:VENVIT_DIR"
        [System.Environment]::SetEnvironmentVariable("Path", $newPath, [System.EnvironmentVariableTarget]::Machine)
        Write-Host "VENVIT_DIR has been added to the System Path." -ForegroundColor Yellow
    }
    else {
        Write-Host "VENVIT_DIR is already in the System Path." -ForegroundColor Yellow
    }
}

function Test-Admin {

    $currentUser = [Security.Principal.WindowsIdentity]::GetCurrent()
    $Principal = New-Object Security.Principal.WindowsPrincipal($currentUser)
    $adminRole = [Security.Principal.WindowsBuiltInRole]::Administrator
    return Invoke-IsInRole -Principal $Principal -Role $adminRole
}

Export-ModuleMember -Function Clear-InstallationFiles, Install-PythonVirtualEnv , Invoke-ConcludeInstall, Invoke-IsInRole
Export-ModuleMember -Function New-Directories, Publish-LatestVersion, Publish-Secrets, Set-Path, Test-Admin
