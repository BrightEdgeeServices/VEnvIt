# vi.ps1

param (
    [Parameter(Mandatory = $false, Position = 0)]
    [string]$ProjectName,

    [Parameter(Mandatory = $false)]
    [Switch]$Help,

    # Used to indicate that the code is called by Pester to avoid unwanted code execution during Pester testing.
    [Parameter(Mandatory = $false)]
    [Switch]$Pester
)

function Invoke-VirtualEnvironment {
    param (
        [string]$ProjectName
    )

    if ((Get-Module -Name "Utils") -and $Pester ) {
        Remove-Module -Name "Utils"
    }
    Import-Module $PSScriptRoot\Utils.psm1

    Invoke-Script -ScriptPath ("$env:VENVIT_DIR\Config\" + (Get-ConfigFileName -ProjectName $ProjectName -Postfix "EnvVar")) | Out-Null
    Invoke-Script -ScriptPath ("~\VenvIt\Config\" + (Get-ConfigFileName -ProjectName $ProjectName -Postfix "EnvVar")) | Out-Null

    if ($env:VIRTUAL_ENV) {
        "Deactivate VEnv $env:VIRTUAL_ENV."
        Invoke-Script -ScriptPath "deactivate" | Out-Null
    }
    Invoke-Script -ScriptPath ($env:VENV_BASE_DIR + "\" + $env:PROJECT_NAME + "_env\Scripts\activate.ps1") | Out-Null

    # $env:PROJECT_NAME = $_project_name
    if ($env:VENV_ENVIRONMENT -eq "loc_dev") {
        Invoke-Script -ScriptPath ("$env:VENVIT_DIR\Secrets\secrets.ps1") | Out-Null
        Invoke-Script -ScriptPath ("~\VenvIt\Secrets\secrets.ps1") | Out-Null
    }

    # Remove temporary directories from previous sessions
    # TODO
    # https://github.com/BrightEdgeeServices/venvit/issues/21
    # Exclude the current temp directory if there is one.
    # Possibly move this to some clean up procedsure.
    Get-ChildItem -Path $env:TEMP -Directory -Filter "$env:PROJECT_NAME*" | Remove-Item -Recurse -Force

    if (Test-Path $env:PROJECT_DIR) {
        Set-Location -Path (Split-Path $env:PROJECT_DIR -Qualifier)
        Set-Location -Path $env:PROJECT_DIR
    }
    else {
        Set-Location -Path (Split-Path $env:PROJECTS_BASE_DIR -Qualifier)
        Set-Location -Path $env:PROJECTS_BASE_DIR
    }

    Invoke-Script -ScriptPath ("$env:VENVIT_DIR\Config\" + (Get-ConfigFileName -ProjectName $ProjectName -Postfix "CustomSetup")) | Out-Null
    Invoke-Script -ScriptPath ("~\VenvIt\Config\" + (Get-ConfigFileName -ProjectName $ProjectName -Postfix "CustomSetup")) | Out-Null
}

# function ShowEnvVarHelp {
#     Write-Host "Make sure the following system environment variables are set. See the help for more detail." -ForegroundColor Cyan
#
#     $_env_vars = @(
#         @("VENV_ENVIRONMENT", $env:VENV_ENVIRONMENT),
#         @("PROJECTS_BASE_DIR", "$env:PROJECTS_BASE_DIR"),
#         @("VENVIT_DIR", "$env:VENVIT_DIR"),
#         @("VENV_SECRETS_DIR", "$env:VENV_SECRETS_DIR"),
#         @("VENV_BASE_DIR", "$env:VENV_BASE_DIR")
#     )
#
#     foreach ($var in $_env_vars) {
#         if ([string]::IsNullOrEmpty($var[1])) {
#             Write-Host $var[0] -ForegroundColor Red -NoNewline
#             Write-Host " - Not Set"
#         }
#         else {
#             Write-Host $var[0] -ForegroundColor Green -NoNewline
#             $s = " - Set to: " + $var[1]
#             Write-Host $s
#         }
#     }
# }

function Show-Help {
    Write-Host $separator -ForegroundColor Cyan

    # Introduction
    @"
This script, 'vi.ps1', initializes a Python virtual environment. This include running the
VEnv${_project_name}CustomSetup .ps1 script.
"@ | Write-Host

    Write-Host $separator -ForegroundColor Cyan
    @"
Usage:
------
vi.ps1 ProjectName
vi.ps1 -Help

Parameters:
1. ProjectName: The name of the project.
2. -Help:       Display this help

Environment Variables:
----------------------
Prior to starting the PowerShell script, ensure these environment variables are set.

1. PROJECTS_BASE_DIR:        The directory for all projects (e.g., d:\Dropbox\Projects).
2. VENV_BASE_DIR:            Directory for virtual environments (e.g., c:\venv).
3. VENV_ENVIRONMENT:         Sets the development environment amrker. Possible values: loc_dev, github_dev, prod, etc.
4. VENVIT_DIR:               Directory where this script resides.
"@ | Write-Host
}

# Script execution starts here
# Pester parameter is to ensure that the script does not execute when called from
# pester BeforeAll.  Any better ideas would be welcome.
if (-not $Pester) {
    Write-Host ''
    Write-Host ''
    $dateTime = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "=[ START $dateTime ]=================================================[ vi.ps1 ]=" -ForegroundColor Blue
    Write-Host "Initialize the $project_name virtual environment" -ForegroundColor Blue
    if ($ProjectName -eq "" -or $Help) {
        Show-Help
    }
    else {
        Invoke-VirtualEnvironment -ProjectName $ProjectName
        Show-EnvironmentVariables
    }
    Write-Host '-[ END ]------------------------------------------------------------------------' -ForegroundColor Cyan
}
