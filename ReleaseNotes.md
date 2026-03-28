# Release 8.0.0

2026-03-28 09:58:24 SAST (UTC+02:00)

______________________________________________________________________

## Breaking Changes

- Renamed `vi.ps1` to `vs.ps1` to avoid conflicts with the Linux editor, added `TargetEnvironment` handling, and aligned the related tests and README usage examples.
- Replaced the legacy `VENV_CONFIG_*` and `VENV_SECRETS_*` locations with `VENVIT_DIR\Config`, `VENVIT_DIR\Secrets`, `~\VenvIt\Config`, and `~\VenvIt\Secrets`, and added upgrade cleanup for deprecated environment variables.

## Python Packaging and Upgrade Path

- Migrated the package metadata to the PEP 621 `[project]` table, introduced the `venvit` console entry point, added the Python upgrade modules and models, and expanded Python version targeting to 3.10 through 3.13.
- Updated installation and conclude flows to build and use a dedicated virtual environment under `VENVIT_DIR\venv`, publish the latest packaged files, and keep installation secrets in the new shared and user locations.

## Automation, Tooling and Documentation

- Added reusable publish workflow templates, developer setup scripts, an updated pre-commit configuration, refreshed ignore rules, and the renamed `LICENSE.txt` asset for packaging.
- Expanded the mixed PowerShell and pytest test suites, refreshed the README for the new `vs.ps1` workflow and Python CLI, and retained the existing release history unchanged.

## Summary Statistics

- Branch name: `hendrik/bee-28-main_feature-venvit-rename-vi-to-vs`
- Files changed: `55`
- Insertions: `5602`
- Deletions: `1165`
- Changed files (top-level and workflows): `.flake8`, `.gitattributes`, `.github/CODEOWNERS`, `.github/workflows/py-temp-pr-pub-no_docker-def.yaml`, `.github/workflows/py-temp-publish-pub-build_release_notify_after_merge-def.yaml`, `.gitignore`, `.pre-commit-config.yaml`, `InstallDevEnv.ps1`, `LICENSE.txt`, `Manifest.psd1`, `README.md`, `ReleaseNotes.md`, `SetupDotEnv.ps1`, `SetupGitHubAccess.ps1`, `SetupPrivateRepoAccess.ps1`, `ToDo.md`, `envvar_clear.ps1`, `envvar_reset.ps1`, `install.ps1`, `installpythontools.ps1`, `poetry.lock`, `pyproject.toml`, `testResults.xml`
- Changed files (source): `src/Conclude-UpgradePrep.psm1`, `src/Install-Conclude.psm1`, `src/Uninstall.ps1`, `src/Utils.psm1`, `src/__init__.py`, `src/install.ps1`, `src/secrets.ps1`, `src/venvit/__init__.py`, `src/venvit/main.py`, `src/venvit/models.py`, `src/venvit/setup.py`, `src/venvit/upgrade.py`, `src/vn.ps1`, `src/vr.ps1`, `src/vs.ps1`
- Changed files (tests): `tests/Conclude-UpgradePrep.Tests.ps1`, `tests/Install-Conclude.Tests.ps1`, `tests/Install.Tests.ps1`, `tests/Publish-TestResources.Tests.ps1`, `tests/Publish-TestResources.psm1`, `tests/Uninstall.Tests.ps1`, `tests/Utils.Tests.ps1`, `tests/__init__.py`, `tests/conftest.py`, `tests/test_core.py`, `tests/test_main.py`, `tests/test_setup.py`, `tests/test_upgrade.py`, `tests/testdata/test_data.py`, `tests/vi.Tests.ps1`, `tests/vn.Tests.ps1`, `tests/vr.Tests.ps1`

______________________________________________________________________

# Release 7.2.0

Establish Python as the primary execution environment for VEnvIt to ensure cross-platform compatibility and minimize reliance on PowerShell.

______________________________________________________________________

# Release 7.1.0

Forked version to Universal-Rating-System

______________________________________________________________________

# Release 7.0.0

- Removed reduandant (commented) code in several files.
- Remove coverage from GitHub CI Workflow.
- Convert several ps1 scripts to be modules to conform to recommended standards.
  - Updated remaining ps1 scripts and GitHub Worklows accordingly.
  - RenameInstall-Conclude.ps1 to Conclude-Install.psm1
  - Rename Conclude-UpgradePrep.ps1 to Conclude-UpgradePrep.psm1
- Cleanup the vscode configuration file.
- Improved Install.ps1
- Add -Pester support for all ps1 scripts. It is limited to the more important functions. The rest still has to be done.
- Renamed variable names to standards. Not all are done. See https://github.com/PoshCode/PowerShellPracticeAndStyle
- Introduce Utils.psm1 to hold all common utility functions.
- Split functions into smaller portions simplifying the code and to allow for more effective testing.
- Introduce the VENV_CONFIG_DEFAULT_DIR and ~\\VenvIt\\Config environment variables at the expense of VENV_CONFIG_DIR
- Introduce the VENVIT_DIR\\Secrets and ~\\VenvIt\\Secrets environment variables at the expense of VENV_SECRETS_DIR
- Create the Invoke-Script function to abstract PS function calls to enable better testing.

## Ticket(s) Included

1. BEE-00037 | VEnvIt | Add Pester Support
1. BEE-00096 | VEnvIt | Update README with missing information
1. BEE-00234 | VEnvIt | Improve organizational support
1. BEE-00269 | VEnvIt | Implement "Uninstall"
1. BEE-00276 | VEnvIt | Fix broken environment variable values after Pester tests

______________________________________________________________________

# Release 6.0.1

## Ticket(s) Included

1. BEE-00236 | VEnvIt | Set ExecutionPolicy
1. BEE-00030 | VEnvIt | Add Windows PowerShell Support

______________________________________________________________________

# Release 6.0.0

## General Changes

- Fork the project from [Batch](https://github.com/BrightEdgeeServices/Batch)
- General restructure of the project, creating the `src` and `tst` folders with the relevant code.
- Improved and updated README.md

## GitHub

- Reformat the ISSUE_TEMPLATE's.
- Add `New Release` issue template.
- Combine `Pre-Commit` and `Check-Documentation` workflows into 'Pre-Commit-and-Document-Check'
- Add a numbered prefix to the workflow file names.
- Removed `CI` workflow, since no formal testing is done. When Pester is employed, it will be commissioned again.
- Removed unnecessary environment variables from `04-build-and-deploy-to-production.yml`.
- Removed unnecessary steps from `04-build-and-deploy-to-production.yml` not relates to PowerShell scripts.
- Add steps to `04-build-and-deploy-to-production.yml` for PowerShell scripts.

## Source

- Rename `env_var_dev.ps1` to `secrets.ps1`.
- Introduce the `download.ps1` script for facilitating the source from the GitHub repository.
- Introduce the `Install.ps1` script to install the scripts and automate the setup and configuration.
- Rename the RTE_ENVIRONMENT environment variable to VENV_ENVIRONMENT.
- Rename the SCRIPTS_DIR environment variable to VENVIT_DIR.
- Rename the SECRETS_DIR environment variable to VENV_SECRETS_DIR.
- Add the VENV_CONFIG_DIR environment variable for greater flexibility to implement shared installations in an organization.
- Improved the display of messages to the console.
- Moved the bulk of the help functions to `README.md`.
- Improved the `usage` clauses in the help.
- Started a basic testing script.

______________________________________________________________________

# Release 5.3.32 - 66

## General Changes

- Testing the installation scripts.

______________________________________________________________________

# Release 5.3.2 - 31

## General Changes

- Testing the GitHub Actions workflow scripts.

______________________________________________________________________

# Release 5.3.1

## General Changes

- Forked from the original "Batch" project.
