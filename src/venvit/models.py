from abc import ABC
from os import environ
from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings

env_location = {"dev", "test", "github", "preprod", "prod"}


class EnvVarSettingsModel(BaseModel):
    def_val: Path | str | None
    is_dir: bool
    system_mandatory: bool


class EnvVarModelV000000(BaseSettings):
    ENVIRONMENT: str = "dev"
    RTE_ENVIRONMENT: str = "dev"
    SCRIPTS_DIR: Path = ""
    SECRETS_DIR: Path = ""
    VENV_BASE_DIR: Path = ""
    VENV_PYTHON_BASE_DIR: Path = ""
    VIRTUAL_ENV: str | None = None


class EnvVarModelV060000(BaseSettings):
    # ENVIRONMENT: str = ""  # Deprecated in 0.6.0
    # RTE_ENVIRONMENT: str = ""  # Deprecated in 0.6.0
    # SCRIPTS_DIR: str = ""  # Deprecated in 0.6.0
    # SECRETS_DIR: str = ""  # Deprecated in 0.6.0

    PROJECT_NAME: str = ""
    PROJECTS_BASE_DIR: Path = ""
    VENV_BASE_DIR: Path = ""
    VENV_CONFIG_DIR: Path = ""
    VENV_ENVIRONMENT: str = ""
    VENV_ORGANIZATION_NAME: str = ""
    VENV_PYTHON_BASE_DIR: Path = ""
    VENV_SECRETS_DIR: Path = ""
    VENVIT_DIR: Path = ""
    VIRTUAL_ENV: str | None = None


class EnvVarModelV070000(BaseSettings):
    # ENVIRONMENT deprecated 6.0.0
    # RTE_ENVIRONMENT deprecated 6.0.0
    # SCRIPTS_DIR deprecated 6.0.0
    # SECRETS_DIR deprecated 6.0.0

    environ["VENV_CONFIG_DIR"] = ""  # Deprecated 0.7.0
    environ["VENV_SECRETS_DIR"] = ""  # Deprecated 0.7.0
    VENV_CONFIG_DIR: str = ""  # Deprecated 0.7.0
    VENV_SECRETS_DIR: str = ""  # Deprecated 0.7.0

    PROJECT_NAME: str = ""
    PROJECTS_BASE_DIR: Path = ""
    VENV_BASE_DIR: Path = ""
    VENV_ENVIRONMENT: str = ""
    VENV_ORGANIZATION_NAME: str = ""
    VENV_CONFIG_DEFAULT_DIR: Path = ""
    VENV_CONFIG_USER_DIR: Path = ""
    VENV_PYTHON_BASE_DIR: Path = ""
    VENV_SECRETS_DEFAULT_DIR: Path = ""
    VENV_SECRETS_USER_DIR: Path = ""
    VENVIT_DIR: Path = ""
    VIRTUAL_ENV: str | None = None


class EnvVarModelV070300(BaseSettings):
    # ENVIRONMENT deprecated 6.0.0
    # RTE_ENVIRONMENT deprecated 6.0.0
    # SCRIPTS_DIR deprecated 6.0.0
    # SECRETS_DIR deprecated 6.0.0

    # VENV_CONFIG_DIR deprecated 0.7.0
    # VENV_SECRETS_DIR deprecated 0.7.0

    environ["VENV_CONFIG_DEFAULT_DIR"] = ""  # Deprecated 0.7.3
    environ["VENV_CONFIG_USER_DIR"] = ""  # Deprecated 0.7.3
    environ["VENV_SECRETS_DEFAULT_DIR"] = ""  # Deprecated 0.7.3
    environ["VENV_SECRETS_USER_DIR"] = ""  # Deprecated 0.7.3

    VENV_CONFIG_DEFAULT_DIR: str = ""  # Deprecated 0.7.3
    VENV_CONFIG_USER_DIR: str = ""  # Deprecated 0.7.3
    VENV_SECRETS_DEFAULT_DIR: str = ""  # Deprecated 0.7.3
    VENV_SECRETS_USER_DIR: str = ""  # Deprecated 0.7.3

    APPDATA: Path = ""
    PROJECT_NAME: str = ""
    PROJECTS_BASE_DIR: Path = ""
    VENV_BASE_DIR: Path = ""
    VENV_ENVIRONMENT: str = ""
    VENV_ORGANIZATION_NAME: str = ""
    VENV_PYTHON_BASE_DIR: Path = ""
    VENVIT_DIR: Path = ""
    VIRTUAL_ENV: str | None = None


class EnvVarSetV000000Model(BaseModel):
    environment: EnvVarSettingsModel
    rte_environment: EnvVarSettingsModel
    scripts_dir: EnvVarSettingsModel
    secrets_dir: EnvVarSettingsModel
    venv_base_dir: EnvVarSettingsModel
    venv_python_base_dir: EnvVarSettingsModel
    virtual_env: EnvVarSettingsModel


class EnvVarSetV060000Model(EnvVarSetV000000Model):
    environment: None = None  # Deprecated
    rte_environment: None = None  # Deprecated
    scripts_dir: None = None  # Deprecated
    secrets_dir: None = None  # Deprecated

    # venv_base_dir: EnvVarDetail # Inherited
    # venv_python_base_dir: EnvVarDetail # Inherited
    # virtual_env: EnvVarDetail # Inherited

    project_name: EnvVarSettingsModel
    projects_base_dir: EnvVarSettingsModel
    venv_config_dir: EnvVarSettingsModel
    venv_environment: EnvVarSettingsModel
    venv_organization_name: EnvVarSettingsModel
    venv_secrets_dir: EnvVarSettingsModel
    venvit_dir: EnvVarSettingsModel


class EnvVarSetV070000Model(EnvVarSetV060000Model):
    # environment: None # Deprecated
    # rte_environment: None # Deprecated
    # scripts_dir: None # Deprecated
    # secrets_dir: None # Deprecated

    venv_config_dir: None = None  # Deprecated
    venv_secrets_dir: None = None  # Deprecated

    # venv_base_dir: EnvVarDetail # Inherited
    # venv_python_base_dir: EnvVarDetail # Inherited
    # virtual_env: EnvVarDetail # Inherited
    # project_name: EnvVarDetail # Inherited
    # projects_base_dir: EnvVarDetail # Inherited
    # venv_environment: EnvVarDetail # Inherited
    # venv_organization_name: EnvVarDetail # Inherited
    # venvit_dir: EnvVarDetail # Inherited

    venv_config_default_dir: EnvVarSettingsModel
    venv_config_user_dir: EnvVarSettingsModel
    venv_secrets_default_dir: EnvVarSettingsModel
    venv_secrets_user_dir: EnvVarSettingsModel


class EnvVarSetV070300Model(EnvVarSetV070000Model):
    # venv_base_dir: EnvVarDetail # Inherited
    # venv_python_base_dir: EnvVarDetail # Inherited
    # virtual_env: EnvVarDetail # Inherited
    # project_name: EnvVarDetail # Inherited
    # projects_base_dir: EnvVarDetail # Inherited
    # venv_environment: EnvVarDetail # Inherited
    # venv_organization_name: EnvVarDetail # Inherited
    # venvit_dir: EnvVarDetail # Inherited

    venv_config_default_dir: None = None  # Deprecated
    venv_config_user_dir: None = None  # Deprecated
    venv_secrets_default_dir: None = None  # Deprecated
    venv_secrets_user_dir: None = None  # Deprecated

    app_data: EnvVarSettingsModel


class EnvVarSetUpBase(ABC):

    def __init__(self):
        self.env_var_set_def = None
        pass

    def setup_structure(self):
        for x in self.env_var_set_def:
            if x[1] and x[1].is_dir and x[1].system_mandatory:
                if not x[1].def_val.exists():
                    x[1].def_val.mkdir(parents=True)
        Path(self.env_var_set_def.venvit_dir.def_val / "Config").mkdir(parents=True, exist_ok=True)
        Path(self.env_var_set_def.venvit_dir.def_val / "Secrets").mkdir(parents=True, exist_ok=True)
        Path(Path.home() / "VEnvIt" / "Config").mkdir(parents=True, exist_ok=True)
        Path(Path.home() / "VEnvIt" / "Secrets").mkdir(parents=True, exist_ok=True)

        pass

    def get_config_filename(self, project_name, postfix):
        return f"VEnv{project_name}{postfix}.ps1"

    def get_secrets_filename(self):
        return "Secrets.ps1"


class EnvSetUpV000000(EnvVarSetUpBase):
    def __init__(self):
        super().__init__()
        self.env_vars = EnvVarModelV000000()
        self.env_var_set_def = EnvVarSetV000000Model(
            environment=EnvVarSettingsModel(
                def_val=self.env_vars.ENVIRONMENT,
                is_dir=False,
                system_mandatory=False,
            ),
            rte_environment=EnvVarSettingsModel(
                def_val=self.env_vars.RTE_ENVIRONMENT,
                is_dir=False,
                system_mandatory=False,
            ),
            scripts_dir=EnvVarSettingsModel(
                def_val=self.env_vars.SCRIPTS_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            secrets_dir=EnvVarSettingsModel(
                def_val=self.env_vars.SECRETS_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            venv_base_dir=EnvVarSettingsModel(
                def_val=self.env_vars.VENV_BASE_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            venv_python_base_dir=EnvVarSettingsModel(
                def_val=self.env_vars.VENV_PYTHON_BASE_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            virtual_env=EnvVarSettingsModel(
                def_val=self.env_vars.VIRTUAL_ENV,
                is_dir=False,
                system_mandatory=False,
            ),
        )

    def create_structure(self):
        pass


class EnvSetUpV060000(EnvVarSetUpBase):
    def __init__(self, p_secure=True):
        super().__init__()
        self.env_vars = EnvVarModelV060000()
        self.env_var_set_def = EnvVarSetV060000Model(
            project_name=EnvVarSettingsModel(
                def_val=self.env_vars.PROJECT_NAME,
                is_dir=True,
                system_mandatory=False,
            ),
            projects_base_dir=EnvVarSettingsModel(
                def_val=self.env_vars.PROJECTS_BASE_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            venv_base_dir=EnvVarSettingsModel(
                def_val=self.env_vars.VENV_BASE_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            venv_config_dir=EnvVarSettingsModel(
                def_val=self.env_vars.VENV_CONFIG_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            venv_environment=EnvVarSettingsModel(
                def_val=self.env_vars.VENV_ENVIRONMENT,
                is_dir=False,
                system_mandatory=True,
            ),
            venv_organization_name=EnvVarSettingsModel(
                def_val=self.env_vars.VENV_ORGANIZATION_NAME,
                is_dir=False,
                system_mandatory=False,
            ),
            venv_python_base_dir=EnvVarSettingsModel(
                def_val=self.env_vars.VENV_PYTHON_BASE_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            venv_secrets_dir=EnvVarSettingsModel(
                def_val=self.env_vars.VENV_SECRETS_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            venvit_dir=EnvVarSettingsModel(
                def_val=self.env_vars.VENVIT_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            virtual_env=EnvVarSettingsModel(
                def_val=self.env_vars.VIRTUAL_ENV,
                is_dir=False,
                system_mandatory=False,
            ),
        )

    def create_structure(self):
        pass


class EnvSetUpV070000(EnvVarSetUpBase):
    def __init__(self, p_secure=True):
        super().__init__()
        self.env_vars = EnvVarModelV070000()
        self.env_var_set_def = EnvVarSetV070000Model(
            project_name=EnvVarSettingsModel(
                def_val=self.env_vars.PROJECT_NAME,
                is_dir=True,
                system_mandatory=False,
            ),
            projects_base_dir=EnvVarSettingsModel(
                def_val=self.env_vars.PROJECTS_BASE_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            venv_base_dir=EnvVarSettingsModel(
                def_val=self.env_vars.VENV_BASE_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            venv_config_default_dir=EnvVarSettingsModel(
                def_val=self.env_vars.VENV_CONFIG_DEFAULT_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            venv_config_user_dir=EnvVarSettingsModel(
                def_val=self.env_vars.VENV_CONFIG_USER_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            venv_environment=EnvVarSettingsModel(
                def_val=self.env_vars.VENV_ENVIRONMENT,
                is_dir=False,
                system_mandatory=True,
            ),
            venv_organization_name=EnvVarSettingsModel(
                def_val=self.env_vars.VENV_ORGANIZATION_NAME,
                is_dir=False,
                system_mandatory=False,
            ),
            venv_python_base_dir=EnvVarSettingsModel(
                def_val=self.env_vars.VENV_PYTHON_BASE_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            venv_secrets_default_dir=EnvVarSettingsModel(
                def_val=self.env_vars.VENV_SECRETS_DEFAULT_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            venv_secrets_user_dir=EnvVarSettingsModel(
                def_val=self.env_vars.VENV_SECRETS_USER_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            venvit_dir=EnvVarSettingsModel(
                def_val=self.env_vars.VENVIT_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            virtual_env=EnvVarSettingsModel(
                def_val=self.env_vars.VIRTUAL_ENV,
                is_dir=False,
                system_mandatory=False,
            ),
        )

    # def create_structure(self):
    #     pass


class EnvSetUpV070300(EnvVarSetUpBase):
    def __init__(self, p_secure=True):
        super().__init__()
        self.env_vars = EnvVarModelV070300()
        self.env_var_set_def = EnvVarSetV070300Model(
            app_data=EnvVarSettingsModel(
                def_val=self.env_vars.APPDATA,
                is_dir=True,
                system_mandatory=False,
            ),
            project_name=EnvVarSettingsModel(
                def_val=self.env_vars.PROJECT_NAME,
                is_dir=False,
                system_mandatory=False,
            ),
            projects_base_dir=EnvVarSettingsModel(
                def_val=self.env_vars.PROJECTS_BASE_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            venv_base_dir=EnvVarSettingsModel(
                def_val=self.env_vars.VENV_BASE_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            venv_environment=EnvVarSettingsModel(
                def_val=self.env_vars.VENV_ENVIRONMENT,
                is_dir=False,
                system_mandatory=True,
            ),
            venv_organization_name=EnvVarSettingsModel(
                def_val=self.env_vars.VENV_ORGANIZATION_NAME,
                is_dir=False,
                system_mandatory=False,
            ),
            venv_python_base_dir=EnvVarSettingsModel(
                def_val=self.env_vars.VENV_PYTHON_BASE_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            venvit_dir=EnvVarSettingsModel(
                def_val=self.env_vars.VENVIT_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            virtual_env=EnvVarSettingsModel(
                def_val=self.env_vars.VIRTUAL_ENV,
                is_dir=False,
                system_mandatory=False,
            ),
        )
