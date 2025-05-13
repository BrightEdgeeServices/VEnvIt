# from beetools.msg import error
import shutil
from pathlib import Path

from pydantic import BaseModel

from venvit.core.env_setup import EnvSetUpV070000
from venvit.core.env_setup import EnvSetUpV070300

# class Settings(BaseSettings):
#     source: str


class UpgradeId(BaseModel):
    upgrade_id: str = ""


class Upgrade:
    def __init__(self, p_settings=None):
        self.upgrade_list = {"v070000to070300": Version070000to070300}
        self.upgrade_process = UpgradeId(upgrade_id=p_settings.upgrade_id)
        self.upgrade_list[self.upgrade_process.upgrade_id]()
        self.success = True
        pass


class Version070000to070300:
    def __init__(self):
        self.success = True
        self.old_def_values = EnvSetUpV070000()
        self.new_def_values = EnvSetUpV070300()
        self.set_to_inspect = [
            [
                Path(self.old_def_values.env_var_set_def.venv_config_default_dir.def_val).resolve(strict=False),
                Path(self.new_def_values.env_var_set_def.venvit_dir.def_val / "Config").resolve(strict=False),
            ],
            [
                Path(self.old_def_values.env_var_set_def.venv_secrets_default_dir.def_val).resolve(strict=False),
                Path(self.new_def_values.env_var_set_def.venvit_dir.def_val / "Secrets").resolve(strict=False),
            ],
            [
                Path(self.old_def_values.env_var_set_def.venv_config_user_dir.def_val).resolve(strict=False),
                Path(self.new_def_values.env_var_set_def.app_data.def_val / "VEnvIt", "Config").resolve(strict=False),
            ],
            [
                Path(self.old_def_values.env_var_set_def.venv_secrets_user_dir.def_val).resolve(strict=False),
                Path(self.new_def_values.env_var_set_def.app_data.def_val / "VEnvIt", "Secrets").resolve(strict=False),
            ],
        ]
        self.success = self.fix_structure()

    def fix_structure(self):
        success = True
        for set_pair in self.set_to_inspect:
            if not self.is_same_dir(set_pair[0], set_pair[1]):
                success = self.move_files(set_pair[0], set_pair[1]) and success
        return success

    @staticmethod
    def is_same_dir(src: Path, dst: Path) -> bool:
        if (src.resolve(strict=False).exists() and dst.resolve(strict=False).exists() and not src.samefile(dst)) or (
            src.resolve(strict=False).exists() and not dst.resolve(strict=False).exists()
        ):
            return False
        return True

    @staticmethod
    def move_files(src: Path, dst: Path) -> bool:
        success = True
        if not dst.resolve(strict=False).exists():
            dst.mkdir(parents=True, exist_ok=True)
            # Iterate over all files in src and move them
            for item in src.iterdir():
                if item.is_file():
                    dest_path = dst / item.name
                    success = shutil.move(str(item), str(dest_path)) and success
        return success
