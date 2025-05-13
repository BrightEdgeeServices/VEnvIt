# vi.Tests.ps1

Describe "vi.Tests.ps1: Top level script execution" {
    BeforeAll {
        . $PSScriptRoot\..\src\vi.ps1 -Pester
    }

    BeforeEach {
        if (Get-Module -Name "Utils") { Remove-Module -Name "Utils" }
        Import-Module $PSScriptRoot\..\src\Utils.psm1

        $originalSessionValues = Backup-SessionEnvironmentVariables
        $originalSystemValues = Backup-SystemEnvironmentVariables

        Mock -CommandName "Show-Help" -MockWith { return "Mock: Show-Help called" }
    }

    Context "When Help parameter is passed" {
        It "Should call Show-Help function" {
            & $PSScriptRoot\..\src\vi.ps1 -Help
            Assert-MockCalled -CommandName "Show-Help" -Exactly 1
        }
    }

    Context "When ProjectName is passed and Help is not passed" {
        BeforeEach {
            Mock -CommandName "Invoke-VirtualEnvironment" -MockWith { return "Mock: Invoke-VirtualEnvironment called" }
            Mock -CommandName "Show-EnvironmentVariables" -MockWith { return "Mock: Show-EnvironmentVariables called" }
        }
        It "Should call Invoke-VirtualEnvironment function with ProjectName" {
            & $PSScriptRoot\..\src\vi.ps1 "Tes01"
            Assert-MockCalled -CommandName "Invoke-VirtualEnvironment" -Exactly 1
            Assert-MockCalled -CommandName "Show-EnvironmentVariables" -Exactly 1
        }
    }

    Context "When Var01 is an empty string and Help is not passed" {
        It "Should call Show-Help function" {
            & $PSScriptRoot\..\src\vi.ps1 -ProjectName $null
            Assert-MockCalled -CommandName "Show-Help" -Exactly 1
        }
    }

    Context "When no parameters are passed" {
        It "Should call Show-Help function" {
            & $PSScriptRoot\..\src\vi.ps1
            Assert-MockCalled -CommandName "Show-Help" -Exactly 1
        }
        AfterEach {
            Restore-SessionEnvironmentVariables -OriginalValues $originalValues
        }
    }
    AfterEach {
        Restore-SessionEnvironmentVariables -OriginalValues $originalSessionValues
        Restore-SystemEnvironmentVariables -OriginalValues $originalSystemValues
    }
}

Describe "vi.Tests.ps1: Function Tests" {
    Context "Invoke-VirtualEnvironment" {
        BeforeAll {
        }

        Context "With virtual environment activated" {
            BeforeAll {
                . $PSScriptRoot\..\src\vi.ps1 -Pester

                if (Get-Module -Name "Publish-TestResources") { Remove-Module -Name "Publish-TestResources" }
                Import-Module $PSScriptRoot\..\tests\Publish-TestResources.psm1

            }
            BeforeEach {
                if (Get-Module -Name "Utils") { Remove-Module -Name "Utils" }
                Import-Module $PSScriptRoot\..\src\Utils.psm1

                $originalSessionValues = Backup-SessionEnvironmentVariables
                $originalSystemValues = Backup-SystemEnvironmentVariables

                $mockInstalVal = Set-TestSetup_7_0_0
                $timeStamp = Get-Date -Format "yyyyMMddHHmm"
            }
            It "Should invoke the virtual environment" {
                # . $PSScriptRoot\..\src\vi.ps1 -Pester

                Mock Invoke-Script { return "Mock: Deactivated current VEnv"
                } -ParameterFilter { $ScriptPath -eq "deactivate" }
                Mock Invoke-Script { return "Mock: Activated VEnv"
                } -ParameterFilter { $ScriptPath -eq ($env:VENV_BASE_DIR + "\" + $env:PROJECT_NAME + "_env\Scripts\activate.ps1") }
                Mock Invoke-Script { return "Mock: Default secrets.ps1"
                } -ParameterFilter { $ScriptPath -eq ("$env:VENVIT_DIR\Secrets\secrets.ps1") }
                Mock Invoke-Script { return "Mock: User secrets.ps1"
                } -ParameterFilter { $ScriptPath -eq ("~\VenvIt\Secrets\secrets.ps1") }
                Mock Invoke-Script { return "Mock: Default EnvVar.ps1"
                } -ParameterFilter { $ScriptPath -eq ("$env:VENVIT_DIR\Config\" + (Get-ConfigFileName -ProjectName $ProjectName -Postfix "EnvVar")) }
                Mock Invoke-Script { return "Mock: User EnvVar.ps1"
                } -ParameterFilter { $ScriptPath -eq ("~\VenvIt\Config\" + (Get-ConfigFileName -ProjectName $ProjectName -Postfix "EnvVar")) }
                Mock Invoke-Script { return "Mock: Default CustomSetup.ps1"
                } -ParameterFilter { $ScriptPath -eq ("$env:VENVIT_DIR\Config\" + (Get-ConfigFileName -ProjectName $ProjectName -Postfix "CustomSetup")) }
                Mock Invoke-Script { return "Mock: User CustomSetup.ps1"
                } -ParameterFilter { $ScriptPath -eq ("~\VenvIt\Config\" + (Get-ConfigFileName -ProjectName $ProjectName -Postfix "CustomSetup")) }

                Invoke-VirtualEnvironment -ProjectName "MyProject"

                Assert-MockCalled -CommandName "Invoke-Script" -ParameterFilter { $ScriptPath -eq "deactivate" }
                # (Test-Path $tempDir) | Should -Be $true
            }
            AfterEach {
                Set-Location -Path $env:TEMP
                Remove-Item -Path $mockInstalVal.TempDir -Recurse -Force

                Restore-SessionEnvironmentVariables -OriginalValues $originalSessionValues
                Restore-SystemEnvironmentVariables -OriginalValues $originalSystemValues
            }
        }
        AfterAll {
        }
    }

    Context "Show-Help" {
        # TODO
        # Test to be implemented
    }
}

