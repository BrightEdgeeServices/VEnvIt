import os

import pytest

from venvit import __main__


@pytest.mark.main
class TestVenvIt:
    def test_venvit_with_no_args(self, monkeypatch):
        monkeypatch.setattr(
            "sys.argv",
            ["pytest", "venvit"],
        )
        with pytest.raises(SystemExit):
            __main__.main()
        pass

    def test_venvit_with_args_upgrade(self, monkeypatch, env_setup_secure_self_destruct):
        env_setup = env_setup_secure_self_destruct
        env_setup.make_structure()
        monkeypatch.setattr(
            "sys.argv",
            ["upgrade", env_setup.dir],
        )
        os.chdir(env_setup.dir)
        __main__.main()
        assert env_setup.dir
        pass
