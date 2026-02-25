from os import environ
from pathlib import Path

import pytest

from venvit import main


@pytest.mark.upgrade
class TestUpgrade:

    def test_upgrade_070200_to_v070300(self, monkeypatch, env_setup_07_02_00_self_destruct):
        venvit_dir = Path(environ.get("VENVIT_DIR"))

        # Verify that vi.ps1 exists (created by Set-TestSetup_7_2_0 to simulate pre-7.3.0 installation)
        vi_script_path = venvit_dir / "vi.ps1"
        assert vi_script_path.exists(), "vi.ps1 should exist before upgrade (created by test setup)"

        monkeypatch.setattr("sys.argv", ["pytest", "upgrade", "7.3.0"])

        # os.chdir(env_setup.dir)
        pa = main.ParseArgs()
        pa.upgrade()
        args = pa.parser.parse_args()
        args.func(args)

        # Verify that vi.ps1 has been deleted during upgrade
        assert not vi_script_path.exists(), "vi.ps1 should be deleted after upgrade to 7.3.0"

        # Verify that vs.ps1 exists (the new renamed script)
        vs_script_path = venvit_dir / "vs.ps1"
        assert vs_script_path.exists(), "vs.ps1 should exist after upgrade to 7.3.0"

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
