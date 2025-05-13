from os import environ
from pathlib import Path

import pytest

from venvit import __main__


@pytest.mark.upgrade
class TestUpgrade:

    def test_upgrade_070000_to_v070300(self, monkeypatch, env_setup_07_00_00_self_destruct_with_config_files):
        monkeypatch.setattr("sys.argv", ["pytest", "upgrade", "v070000to070300"])

        # os.chdir(env_setup.dir)
        pa = __main__.ParseArgs()
        pa.upgrade()
        args = pa.parser.parse_args()
        args.func(args)

        assert Path(environ.get("VENVIT_DIR"), "Config", "VEnvMyProjectCustomSetup.ps1").exists()
        assert Path(environ.get("APPDATA"), "VEnvIt", "Config", "VEnvMyProjectCustomSetup.ps1").exists()
        assert Path(environ.get("VENVIT_DIR"), "Config", "VEnvMyProjectEnvVar.ps1").exists()
        assert Path(environ.get("APPDATA"), "VEnvIt", "Config", "VEnvMyProjectEnvVar.ps1").exists()
        assert Path(environ.get("VENVIT_DIR"), "Config", "VEnvMyProjectInstall.ps1").exists()
        assert Path(environ.get("APPDATA"), "VEnvIt", "Config", "VEnvMyProjectInstall.ps1").exists()
        assert Path(environ.get("VENVIT_DIR"), "Secrets", "Secrets.ps1").exists()
        assert Path(environ.get("APPDATA"), "VEnvIt", "Secrets", "Secrets.ps1").exists()

    def test_version070000to070300(self, env_setup_07_00_00_self_destruct):
        env_setup_07_00_00 = env_setup_07_00_00_self_destruct
        env_setup_07_00_00.setup_structure()
        pass
