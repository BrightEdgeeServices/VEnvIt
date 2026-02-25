# Install-Conclude.Tests.ps1
BeforeAll {
    if (Get-Module -Name "Publish-TestResources") { Remove-Module -Name "Publish-TestResources" }
    Import-Module $PSScriptRoot\..\tests\Publish-TestResources.psm1

    if (Get-Module -Name "Install-Conclude") { Remove-Module -Name "Install-Conclude" }
    Import-Module $PSScriptRoot\..\src\Install-Conclude.psm1
}

Describe "Install-Conclude.Tests.ps1: Function Tests" {
    BeforeAll {
        # This test must be run with administrator rights.
        if (-not (Test-Admin)) {
            Throw "Tests must be run as an Administrator. Aborting..."
        }
    }

    Context "Clear-InstallationFiles" {
        BeforeAll {
            if (Get-Module -Name "Utils") { Remove-Module -Name "Utils" }
            Import-Module $PSScriptRoot\..\src\Utils.psm1
        }

        BeforeEach {
            $originalSessionValues = Backup-SessionEnvironmentVariables
            $originalSystemValues = Backup-SystemEnvironmentVariables

            $tempDir = New-CustomTempDir -Prefix "VenvIt"
            $upgradeScriptDir = "$tempDir\UpgradeScript"
            New-Item -ItemType Directory -Path $upgradeScriptDir | Out-Null
        }

        It "Ensure installation files removed" {
            Clear-InstallationFiles -upgradeScriptDir $upgradeScriptDir
            (Test-Path -Path $upgradeScriptDir) | Should -Be $false
        }

        AfterEach {
            Remove-Item -Path $TempDir -Recurse -Force
            Restore-SessionEnvironmentVariables -OriginalValues $originalSessionValues
            Restore-SystemEnvironmentVariables -OriginalValues $originalSystemValues
        }
    }

    Context "Invoke-ConcludeInstall (new)" {
        BeforeEach {
            if (Get-Module -Name "Utils") { Remove-Module -Name "Utils" }
            $originalSessionValues = Backup-SessionEnvironmentVariables
            $originalSystemValues = Backup-SystemEnvironmentVariables

            Import-Module $PSScriptRoot\..\src\Utils.psm1

            $upgradeDetail = Set-TestSetup_InstallationFiles
            $TempDir = Join-Path -Path $env:TEMP -ChildPath ("$VEnvIt_" + [Guid]::NewGuid().ToString())
            if (($env:VENV_PYTHON_BASE_DIR) -and (Test-Path -Path $env:VENV_PYTHON_BASE_DIR)) {
                $venv_python_base_dir = $env:VENV_PYTHON_BASE_DIR
            }
            else {
                $venv_python_base_dir = "$TempDir\Python"
            }
            Unpublish-EnvironmentVariables
            $env:APPDATA = (Join-Path -Path $TempDir -ChildPath "$env:USERNAME\AppData")
            New-Item -ItemType Directory -Path $env:APPDATA | Out-Null

            Mock Read-Host { return "" } -ParameterFilter { $Prompt -eq "VENVIT_DIR (C:\Program Files\VenvIt)" }
            Mock -ModuleName Install-Conclude Get-ReadAndSetEnvironmentVariables {
                $env:VENVIT_DIR = "$TempDir\VEnvIt"
                [System.Environment]::SetEnvironmentVariable("VENVIT_DIR", $env:VENVIT_DIR, [System.EnvironmentVariableTarget]::Machine)
                $env:PROJECTS_BASE_DIR = "$TempDir\Projects"
                [System.Environment]::SetEnvironmentVariable("PROJECTS_BASE_DIR", $env:PROJECTS_BASE_DIR, [System.EnvironmentVariableTarget]::Machine)
                $env:VENV_BASE_DIR = "$TempDir\VEnv"
                [System.Environment]::SetEnvironmentVariable("VENV_BASE_DIR", $env:VENV_BASE_DIR, [System.EnvironmentVariableTarget]::Machine)
                # $env:VENV_CONFIG_DEFAULT_DIR = "$env:VENVIT_DIR\Config"
                # [System.Environment]::SetEnvironmentVariable("VENV_CONFIG_DEFAULT_DIR", $env:VENV_CONFIG_DEFAULT_DIR, [System.EnvironmentVariableTarget]::Machine)
                # $env:VENV_CONFIG_USER_DIR = "$TempDir\User\VEnvIt\Config"
                # [System.Environment]::SetEnvironmentVariable("VENV_CONFIG_USER_DIR", $env:VENV_CONFIG_USER_DIR, [System.EnvironmentVariableTarget]::Machine)
                $env:VENV_ENVIRONMENT = "loc_dev"
                [System.Environment]::SetEnvironmentVariable("VENV_ENVIRONMENT", $env:VENV_ENVIRONMENT, [System.EnvironmentVariableTarget]::Machine)
                $env:VENV_PYTHON_BASE_DIR = "$venv_python_base_dir"
                [System.Environment]::SetEnvironmentVariable("VENV_PYTHON_BASE_DIR", $env:VENV_PYTHON_BASE_DIR, [System.EnvironmentVariableTarget]::Machine)
                # $env:VENV_SECRETS_DEFAULT_DIR = "$env:VENVIT_DIR\Secrets"
                # [System.Environment]::SetEnvironmentVariable("VENV_SECRETS_DEFAULT_DIR", $env:VENV_SECRETS_DEFAULT_DIR, [System.EnvironmentVariableTarget]::Machine)
                # $env:VENV_SECRETS_USER_DIR = "$TempDir\User\VEnvIt\Secrets"
                # [System.Environment]::SetEnvironmentVariable("VENV_SECRETS_USER_DIR", $env:VENV_SECRETS_USER_DIR, [System.EnvironmentVariableTarget]::Machine)
            }
        }
        It "Should do new installation" {
            Invoke-ConcludeInstall -UpgradeScriptDir $upgradeDetail.Dir

            Test-Path -Path $env:VENVIT_DIR | Should -Be $true
            Get-Item -Path $env:VENVIT_DIR | Should -Be "$TempDir\VEnvIt"

            $env:ENVIRONMENT | Should -Be $null
            $env:RTE_ENVIRONMENT | Should -Be $null
            $env:SCRIPTS_DIR  | Should -Be $null
            $env:SECRETS_DIR  | Should -Be $null
            $env:VENV_CONFIG_DIR | Should -Be $null
            $env:VENV_SECRETS_DEFAULT_DIR | Should -Be $null
            $env:VENV_SECRETS_DIR | Should -Be $null
            $env:VENV_SECRETS_USER_DIR | Should -Be $null
            $env:VENV_CONFIG_DEFAULT_DIR | Should -Be $null
            $env:VENV_CONFIG_USER_DIR | Should -Be $null

            Test-Path -Path $env:PROJECTS_BASE_DIR | Should -Be $true
            Get-Item -Path $env:PROJECTS_BASE_DIR  | Should -Be "$TempDir\Projects"
            Test-Path -Path $env:VENV_BASE_DIR | Should -Be $true
            Get-Item -Path $env:VENV_BASE_DIR  | Should -Be "$TempDir\VEnv"
            Test-Path -Path $env:VENVIT_DIR | Should -Be $true
            Get-Item -Path $env:VENVIT_DIR  | Should -Be "$TempDir\VEnvIt"

            $env:PROJECT_NAME  | Should -Be $null
            $env:VENV_ENVIRONMENT  | Should -Be "loc_dev"
            $env:VENV_ORGANIZATION_NAME  | Should -Be $null

            [System.Environment]::GetEnvironmentVariable("ENVIRONMENT", [System.EnvironmentVariableTarget]::Machine) | Should -Be $null
            [System.Environment]::GetEnvironmentVariable("RTE_ENVIRONMENT", [System.EnvironmentVariableTarget]::Machine) | Should -Be $null
            [System.Environment]::GetEnvironmentVariable("SCRIPTS_DIR", [System.EnvironmentVariableTarget]::Machine) | Should -Be $null
            [System.Environment]::GetEnvironmentVariable("SECRETS_DIR", [System.EnvironmentVariableTarget]::Machine) | Should -Be $null
            [System.Environment]::GetEnvironmentVariable("VENV_CONFIG_DIR", [System.EnvironmentVariableTarget]::Machine) | Should -Be $null
            [System.Environment]::GetEnvironmentVariable("VENV_SECRETS_DIR", [System.EnvironmentVariableTarget]::Machine) | Should -Be $null
            [System.Environment]::GetEnvironmentVariable("VENV_CONFIG_DEFAULT_DIR", [System.EnvironmentVariableTarget]::Machine) | Should -Be $null
            [System.Environment]::GetEnvironmentVariable("VENV_CONFIG_USER_DIR", [System.EnvironmentVariableTarget]::Machine) | Should -Be $null
            [System.Environment]::GetEnvironmentVariable("VENV_SECRETS_DEFAULT_DIR", [System.EnvironmentVariableTarget]::Machine) | Should -Be $null
            [System.Environment]::GetEnvironmentVariable("VENV_SECRETS_USER_DIR", [System.EnvironmentVariableTarget]::Machine) | Should -Be $null

            [System.Environment]::GetEnvironmentVariable("VENV_BASE_DIR", [System.EnvironmentVariableTarget]::Machine) | Should -Be "$TempDir\VEnv"
            [System.Environment]::GetEnvironmentVariable("VENV_PYTHON_BASE_DIR", [System.EnvironmentVariableTarget]::Machine) | Should -Be "C:\Python"
            [System.Environment]::GetEnvironmentVariable("VIRTUAL_ENV", [System.EnvironmentVariableTarget]::Machine) | Should -Be $null
            [System.Environment]::GetEnvironmentVariable("PROJECTS_BASE_DIR", [System.EnvironmentVariableTarget]::Machine) | Should -Be "$TempDir\Projects"
            [System.Environment]::GetEnvironmentVariable("VENVIT_DIR", [System.EnvironmentVariableTarget]::Machine) | Should -Be "$TempDir\VEnvIt"

        }
        AfterEach {
            Remove-Item -Path $TempDir -Recurse -Force
            Remove-Item -Path ($upgradeDetail.Dir + "\..") -Recurse -Force
            Restore-SessionEnvironmentVariables -OriginalValues $originalSessionValues
            Restore-SystemEnvironmentVariables -OriginalValues $originalSystemValues
        }
    }

    Context "Invoke-ConcludeInstall upgrade 7.2.0 to 7.3.0" {
        BeforeEach {
            if (Get-Module -Name "Utils") { Remove-Module -Name "Utils" }
            $originalSessionValues = Backup-SessionEnvironmentVariables
            $originalSystemValues = Backup-SystemEnvironmentVariables

            Import-Module $PSScriptRoot\..\src\Utils.psm1

            $upgradeDetail = Set-TestSetup_InstallationFiles
            # $TempDir = New-CustomTempDir -Prefix "VenvIt"
            $mockInstalVal = Set-TestSetup_7_2_0
            # if ($env:VENV_PYTHON_BASE_DIR -and (Test-Path -Path $env:VENV_PYTHON_BASE_DIR)) {
            #     $venv_python_base_dir = $env:VENV_PYTHON_BASE_DIR
            # }
            # else {
            #     $venv_python_base_dir = "$TempDir\Python"
            # }
            # # $mockInstalVal = Set-TestSetup_7_2_0
            # $env:APPDATA = (Join-Path -Path $TempDir -ChildPath "$env:USERNAME\AppData")
            # New-Item -ItemType Directory -Path $env:APPDATA | Out-Null

            Mock Read-Host { return "" } -ParameterFilter { $Prompt -eq "VENVIT_DIR (C:\Program Files\VenvIt)" }
            Mock -ModuleName Install-Conclude Get-ReadAndSetEnvironmentVariables {
                [System.Environment]::SetEnvironmentVariable("VENV_ENVIRONMENT", $env:VENV_ENVIRONMENT, [System.EnvironmentVariableTarget]::Machine)
                [System.Environment]::SetEnvironmentVariable("PROJECTS_BASE_DIR", $env:PROJECTS_BASE_DIR, [System.EnvironmentVariableTarget]::Machine)
                [System.Environment]::SetEnvironmentVariable("VENV_BASE_DIR", $env:VENV_BASE_DIR, [System.EnvironmentVariableTarget]::Machine)
                [System.Environment]::SetEnvironmentVariable("VENV_CONFIG_DEFAULT_DIR", $env:VENV_CONFIG_DEFAULT_DIR, [System.EnvironmentVariableTarget]::Machine)
                [System.Environment]::SetEnvironmentVariable("VENV_CONFIG_USER_DIR", $env:VENV_CONFIG_USER_DIR, [System.EnvironmentVariableTarget]::Machine)
                [System.Environment]::SetEnvironmentVariable("VENV_PYTHON_BASE_DIR", $env:VENV_PYTHON_BASE_DIR, [System.EnvironmentVariableTarget]::Machine)
                [System.Environment]::SetEnvironmentVariable("VENV_SECRETS_DEFAULT_DIR", $env:VENV_SECRETS_DEFAULT_DIR, [System.EnvironmentVariableTarget]::Machine)
                [System.Environment]::SetEnvironmentVariable("VENV_SECRETS_USER_DIR", $env:VENV_SECRETS_USER_DIR, [System.EnvironmentVariableTarget]::Machine)
                [System.Environment]::SetEnvironmentVariable("VENVIT_DIR", $env:VENVIT_DIR, [System.EnvironmentVariableTarget]::Machine)
            }
        }
        It "Upgrade from 7.2.0 to 7.3.0" {
            Invoke-ConcludeInstall -UpgradeScriptDir $upgradeDetail.Dir

            Test-Path -Path $env:VENVIT_DIR | Should -Be $true
            Get-Item -Path $env:VENVIT_DIR | Should -Be "$TempDir\VEnvIt"

            $env:ENVIRONMENT = ""
            $env:RTE_ENVIRONMENT = ""
            $env:SCRIPTS_DIR = ""
            $env:SECRETS_DIR = ""
            $env:VENV_CONFIG_DIR = ""
            $env:VENV_SECRETS_DEFAULT_DIR = ""
            $env:VENV_SECRETS_DIR = ""
            $env:VENV_SECRETS_USER_DIR = ""
            $env:VENV_CONFIG_DEFAULT_DIR = ""
            $env:VENV_CONFIG_USER_DIR = ""

            Test-Path -Path $env:PROJECTS_BASE_DIR | Should -Be $true
            Get-Item -Path $env:PROJECTS_BASE_DIR  | Should -Be "$TempDir\Projects"
            Test-Path -Path $env:VENV_BASE_DIR | Should -Be $true
            Get-Item -Path $env:VENV_BASE_DIR  | Should -Be "$TempDir\VEnv"
            Test-Path -Path $env:VENVIT_DIR | Should -Be $true
            Get-Item -Path $env:VENVIT_DIR  | Should -Be "$TempDir\VEnvIt"

            $env:PROJECT_NAME = ""
            $env:VENV_ENVIRONMENT = "loc_dev"
            $env:VENV_ORGANIZATION_NAME = ""

            [System.Environment]::GetEnvironmentVariable("ENVIRONMENT", [System.EnvironmentVariableTarget]::Machine) | Should -Be $null
            [System.Environment]::GetEnvironmentVariable("RTE_ENVIRONMENT", [System.EnvironmentVariableTarget]::Machine) | Should -Be $null
            [System.Environment]::GetEnvironmentVariable("SCRIPTS_DIR", [System.EnvironmentVariableTarget]::Machine) | Should -Be $null
            [System.Environment]::GetEnvironmentVariable("SECRETS_DIR", [System.EnvironmentVariableTarget]::Machine) | Should -Be $null
            [System.Environment]::GetEnvironmentVariable("VENV_CONFIG_DIR", [System.EnvironmentVariableTarget]::Machine) | Should -Be $null
            [System.Environment]::GetEnvironmentVariable("VENV_SECRETS_DIR", [System.EnvironmentVariableTarget]::Machine) | Should -Be $null
            [System.Environment]::GetEnvironmentVariable("VENV_CONFIG_DEFAULT_DIR", [System.EnvironmentVariableTarget]::Machine) | Should -Be $null
            [System.Environment]::GetEnvironmentVariable("VENV_CONFIG_USER_DIR", [System.EnvironmentVariableTarget]::Machine) | Should -Be $null
            [System.Environment]::GetEnvironmentVariable("VENV_SECRETS_DEFAULT_DIR", [System.EnvironmentVariableTarget]::Machine) | Should -Be $null
            [System.Environment]::GetEnvironmentVariable("VENV_SECRETS_USER_DIR", [System.EnvironmentVariableTarget]::Machine) | Should -Be $null

            [System.Environment]::GetEnvironmentVariable("VENV_BASE_DIR", [System.EnvironmentVariableTarget]::Machine) | Should -Be "$TempDir\VEnv"
            [System.Environment]::GetEnvironmentVariable("VENV_PYTHON_BASE_DIR", [System.EnvironmentVariableTarget]::Machine) | Should -Be "C:\Python"
            [System.Environment]::GetEnvironmentVariable("VIRTUAL_ENV", [System.EnvironmentVariableTarget]::Machine) | Should -Be $null
            [System.Environment]::GetEnvironmentVariable("PROJECTS_BASE_DIR", [System.EnvironmentVariableTarget]::Machine) | Should -Be "$TempDir\Projects"
            [System.Environment]::GetEnvironmentVariable("VENVIT_DIR", [System.EnvironmentVariableTarget]::Machine) | Should -Be "$TempDir\VEnvIt"

        }
        AfterEach {
            Remove-Item -Path $TempDir -Recurse -Force
            Remove-Item -Path ($upgradeDetail.Dir + "\..") -Recurse -Force
            Restore-SessionEnvironmentVariables -OriginalValues $originalSessionValues
            Restore-SystemEnvironmentVariables -OriginalValues $originalSystemValues
        }
    }

    Context "Invoke-IsInRole" {
        # TODO
        # Test to be implemented
    }

    Context "New-Directories" {
        BeforeAll {
            if (Get-Module -Name "Utils") { Remove-Module -Name "Utils" }
            Import-Module $PSScriptRoot\..\src\Utils.psm1

            $originalSessionValues = Backup-SessionEnvironmentVariables
            $originalSystemValues = Backup-SystemEnvironmentVariables
        }
        BeforeEach {
            $tempDir = New-CustomTempDir -Prefix "VenvIt"
            $testEnvVarSet = @{
                TEST_VAL = @{
                    DefVal = "Test value"; IsDir = $false; SystemMandatory = $false; ReadOrder = -1; Prefix = $false; Deprecated = $false
                }
                TEST_DIR_100     = @{
                    DefVal = (Join-Path -Path $tempDir -ChildPath ("test_dir_100"))
                    IsDir = $true; SystemMandatory = $true; ReadOrder = -1; Prefix = $false; Deprecated = "1.0.0"
                }
                TEST_DIR_200     = @{
                    DefVal = (Join-Path -Path $tempDir -ChildPath ("test_dir_200"))
                    IsDir = $true; SystemMandatory = $true; ReadOrder = -1; Prefix = $false; Deprecated = "2.0.0"
                }
                TEST_DIR_300     = @{
                    DefVal = (Join-Path -Path $tempDir -ChildPath ("test_dir_300"))
                    IsDir = $true; SystemMandatory = $true; ReadOrder = -1; Prefix = $false; Deprecated = "3.0.0"
                }
                TEST_DIR_CURRENT = @{
                    DefVal = (Join-Path -Path $tempDir -ChildPath ("test_dir_Current"))
                    IsDir = $true; SystemMandatory = $true; ReadOrder = -1; Prefix = $false; Deprecated = $false
                }

            }
            foreach ($envVar in $testEnvVarSet.Keys) {
                [System.Environment]::SetEnvironmentVariable($envVar, $testEnvVarSet[$envVar]["DefVal"], [System.EnvironmentVariableTarget]::Machine)
                # Set-Item -Path "env:$envVar" -Value $testEnvVarSet[$envVar]["DefVal"]
            }
        }

        It "Should create all the current directories" {
            New-Directories -EnvVarSet $testEnvVarSet

            Test-Path -Path ([System.Environment]::GetEnvironmentVariable("TEST_VAL", [System.EnvironmentVariableTarget]::Machine)) | Should -Be $false
            Test-Path -Path ([System.Environment]::GetEnvironmentVariable("TEST_DIR_100", [System.EnvironmentVariableTarget]::Machine)) | Should -Be $false
            Test-Path -Path ([System.Environment]::GetEnvironmentVariable("TEST_DIR_200", [System.EnvironmentVariableTarget]::Machine)) | Should -Be $false
            Test-Path -Path ([System.Environment]::GetEnvironmentVariable("TEST_DIR_300", [System.EnvironmentVariableTarget]::Machine)) | Should -Be $false
            Test-Path -Path ([System.Environment]::GetEnvironmentVariable("TEST_DIR_CURRENT", [System.EnvironmentVariableTarget]::Machine)) | Should -Be $true
        }
        It "Should deprecate v1.0.0 directories" {
            New-Directories -EnvVarSet $testEnvVarSet -Version "1.0.0"

            Test-Path -Path ([System.Environment]::GetEnvironmentVariable("TEST_VAL", [System.EnvironmentVariableTarget]::Machine)) | Should -Be $false
            Test-Path -Path ([System.Environment]::GetEnvironmentVariable("TEST_DIR_100", [System.EnvironmentVariableTarget]::Machine)) | Should -Be $false
            Test-Path -Path ([System.Environment]::GetEnvironmentVariable("TEST_DIR_200", [System.EnvironmentVariableTarget]::Machine)) | Should -Be $true
            Test-Path -Path ([System.Environment]::GetEnvironmentVariable("TEST_DIR_300", [System.EnvironmentVariableTarget]::Machine)) | Should -Be $true
            Test-Path -Path ([System.Environment]::GetEnvironmentVariable("TEST_DIR_CURRENT", [System.EnvironmentVariableTarget]::Machine)) | Should -Be $true
        }

        It "Should deprecate v2.0.0 directories" {
            New-Directories -EnvVarSet $testEnvVarSet -Version "2.0.0"

            Test-Path -Path ([System.Environment]::GetEnvironmentVariable("TEST_VAL", [System.EnvironmentVariableTarget]::Machine)) | Should -Be $false
            Test-Path -Path ([System.Environment]::GetEnvironmentVariable("TEST_DIR_100", [System.EnvironmentVariableTarget]::Machine)) | Should -Be $false
            Test-Path -Path ([System.Environment]::GetEnvironmentVariable("TEST_DIR_200", [System.EnvironmentVariableTarget]::Machine)) | Should -Be $false
            Test-Path -Path ([System.Environment]::GetEnvironmentVariable("TEST_DIR_300", [System.EnvironmentVariableTarget]::Machine)) | Should -Be $true
            Test-Path -Path ([System.Environment]::GetEnvironmentVariable("TEST_DIR_CURRENT", [System.EnvironmentVariableTarget]::Machine)) | Should -Be $true
        }
        AfterEach {
            Unpublish-EnvironmentVariables -EnvVarSet $testEnvVarSet
            Remove-Item -Path $tempDir -Recurse -Force
        }

        AfterAll {
            Restore-SessionEnvironmentVariables -OriginalValues $originalSessionValues
            Restore-SystemEnvironmentVariables -OriginalValues $originalSystemValues
        }
    }

    Context "Publish-LatestVersion" {
        BeforeAll {
            if (Get-Module -Name "Update-Manifest") { Remove-Module -Name "Update-Manifest" }
            Import-Module $PSScriptRoot\..\src\Update-Manifest.psm1

            if (Get-Module -Name "Utils") { Remove-Module -Name "Utils" }
            Import-Module $PSScriptRoot\..\src\Utils.psm1
        }
        BeforeEach {
            $originalSessionValues = Backup-SessionEnvironmentVariables
            $originalSystemValues = Backup-SystemEnvironmentVariables

            $mockInstalVal = Set-TestSetup_6_0_0
            $upgradeDetail = Set-TestSetup_InstallationFiles
        }

        It "Should copy all installation files" {
            Publish-LatestVersion -UpgradeSourceDir $upgradeDetail.Dir

            foreach ($fileName in $upgradeDetail.FileList) {
                $barefilename = Split-Path -Path $filename -Leaf
                # Write-Host $barefilename
                (Test-Path -Path "$env:VENVIT_DIR\$barefilename") | Should -Be $true
            }
        }

        AfterEach {
            Remove-Item -Path ($upgradeDetail.Dir + "\..") -Recurse -Force
            Remove-Item -Path $mockInstalVal.TempDir -Recurse -Force

            Restore-SessionEnvironmentVariables -OriginalValues $originalSessionValues
            Restore-SystemEnvironmentVariables -OriginalValues $originalSystemValues
        }
        AfterAll {
        }
    }

    Context "Publish-Secrets" {
        BeforeAll {
            if (Get-Module -Name "Update-Manifest") { Remove-Module -Name "Update-Manifest" }
            Import-Module $PSScriptRoot\..\src\Update-Manifest.psm1

            if (Get-Module -Name "Utils") { Remove-Module -Name "Utils" }
            Import-Module $PSScriptRoot\..\src\Utils.psm1
        }
        BeforeEach {
            $originalSessionValues = Backup-SessionEnvironmentVariables
            $originalSystemValues = Backup-SystemEnvironmentVariables

            $mockInstalVal = Set-TestSetup_7_0_0
            $upgradeDetail = Set-TestSetup_InstallationFiles
        }

        It "Should copy all secrets files" {
            $secretsPath = Join-Path -Path "$env:VENVIT_DIR\Secrets" -ChildPath (Get-SecretsFileName)
            Remove-Item -Path $secretsPath -Recurse -Force
            $secretsPath = Join-Path -Path "~\VenvIt\Secrets" -ChildPath (Get-SecretsFileName)
            Remove-Item -Path $secretsPath -Recurse -Force
            $secretsDirList = Publish-Secrets -UpgradeScriptDir $upgradeDetail.Dir

            $secretsDirList | Should -Be @("$env:VENVIT_DIR\Secrets\secrets.ps1", "~\VenvIt\Secrets\secrets.ps1")
        }

        It "Should only copy VENVIT_DIR\Secrets secrets files" {
            $secretsPath = Join-Path -Path "$env:VENVIT_DIR\Secrets" -ChildPath (Get-SecretsFileName)
            Remove-Item -Path $secretsPath -Recurse -Force | Out-Null

            $secretsDirList = Publish-Secrets -UpgradeScriptDir $upgradeDetail.Dir

            $secretsDirList | Should -Be @("$env:VENVIT_DIR\Secrets\secrets.ps1")
        }

        AfterEach {
            Remove-Item -Path $upgradeDetail.Dir -Recurse -Force | Out-Null
            Remove-Item -Path $mockInstalVal.TempDir -Recurse -Force | Out-Null
            Restore-SessionEnvironmentVariables -OriginalValues $originalSessionValues
            Restore-SystemEnvironmentVariables -OriginalValues $originalSystemValues
        }
    }

    Context "Set-Path" {
        BeforeEach {
            $originalSessionValues = Backup-SessionEnvironmentVariables
            $originalSystemValues = Backup-SystemEnvironmentVariables
            $orgigPATH = [System.Environment]::GetEnvironmentVariable("Path", [System.EnvironmentVariableTarget]::Machine)
            $env:VENVIT_DIR = ".\my\path"
        }

        It "VenvIt not in path" {
            [System.Environment]::SetEnvironmentVariable("Path", "C:\;D:\", [System.EnvironmentVariableTarget]::Machine)
            Set-Path
            $newPath = [System.Environment]::GetEnvironmentVariable("Path", [System.EnvironmentVariableTarget]::Machine)
            $newPath | Should -Be "C:\;D:\;$env:VENVIT_DIR"
        }

        It "VenvIt already in path" {
            [System.Environment]::SetEnvironmentVariable("Path", "C:\; D:\; $env:VENVIT_DIR", [System.EnvironmentVariableTarget]::Machine)
            Set-Path
            $newPath = [System.Environment]::GetEnvironmentVariable("Path", [System.EnvironmentVariableTarget]::Machine)
            $newPath | Should -Be "C:\; D:\; $env:VENVIT_DIR"
        }

        AfterEach {
            [System.Environment]::SetEnvironmentVariable("Path", $orgigPATH, [System.EnvironmentVariableTarget]::Machine)
            Restore-SessionEnvironmentVariables -OriginalValues $originalSessionValues
            Restore-SystemEnvironmentVariables -OriginalValues $originalSystemValues
        }
    }

    Context "Test-Admin" {
        BeforeAll {
            if (Get-Module -Name "Install-Conclude") { Remove-Module -Name "Install-Conclude" }
            Import-Module $PSScriptRoot\..\src\Install-Conclude.psm1

            $originalSessionValues = Backup-SessionEnvironmentVariables
            $originalSystemValues = Backup-SystemEnvironmentVariables
        }
        It "Returns true if an administrator" {
            Mock -ModuleName Install-Conclude -CommandName Invoke-IsInRole { return $true }

            Test-Admin | Should -Be $true
        }

        It "Returns false if not an administrator" {
            Mock -ModuleName Install-Conclude -CommandName Invoke-IsInRole { return $false }

            Test-Admin | Should -Be $false
        }
        AfterAll {
            Restore-SessionEnvironmentVariables -OriginalValues $originalSessionValues
            Restore-SystemEnvironmentVariables -OriginalValues $originalSystemValues
        }
    }

    AfterAll {
    }

}
