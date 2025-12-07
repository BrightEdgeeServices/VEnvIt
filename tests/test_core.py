from os import environ
from pathlib import Path

import pytest

from venvit.core.env_setup import EnvSetUpV070300
from venvit.core.env_setup import EnvVarSettingsModel
from venvit.core.env_setup import EnvVarSetV000000Model
from venvit.core.env_setup import EnvVarSetV060000Model
from venvit.core.env_setup import EnvVarSetV070000Model
from venvit.core.env_setup import EnvVarSetV070300Model
from venvit.core.env_setup import EnvVarV000000Model
from venvit.core.env_setup import EnvVarV060000Model
from venvit.core.env_setup import EnvVarV070000Model
from venvit.core.env_setup import EnvVarV070300Model


# noinspection PyArgumentList
@pytest.mark.upgrade
class TestEnvSetUp:

    def test_env_var_settings_model(self):
        env_set = EnvVarSettingsModel(def_val="def_val", is_dir=True, system_mandatory=True)
        assert env_set.def_val == "def_val"
        assert env_set.is_dir is True
        assert env_set.system_mandatory is True
        pass

    def test_env_var_v000000_model(self):
        environ["ENVIRONMENT"] = "dev"
        environ["RTE_ENVIRONMENT"] = "dev"
        environ["SCRIPTS_DIR"] = ""
        environ["SECRETS_DIR"] = ""
        environ["VENV_BASE_DIR"] = ""
        environ["VENV_PYTHON_BASE_DIR"] = ""
        environ["VIRTUAL_ENV"] = "virtual_env"
        env_var = EnvVarV000000Model()

        assert env_var.ENVIRONMENT == "dev"
        assert env_var.RTE_ENVIRONMENT == "dev"
        assert env_var.SCRIPTS_DIR == Path("")
        assert env_var.SECRETS_DIR == Path("")
        assert env_var.VENV_BASE_DIR == Path("")
        assert env_var.VENV_PYTHON_BASE_DIR == Path("")
        assert env_var.VIRTUAL_ENV == "virtual_env"
        pass

    def test_env_var_v060000_model(self):
        environ["ENVIRONMENT"] = ""
        environ["RTE_ENVIRONMENT"] = ""
        environ["SCRIPTS_DIR"] = ""
        environ["SECRETS_DIR"] = ""

        environ["PROJECT_NAME"] = "Test"
        environ["PROJECTS_BASE_DIR"] = "."
        environ["VENV_CONFIG_DIR"] = ""
        environ["VENV_ENVIRONMENT"] = "venv_environment"
        environ["VENV_ORGANIZATION_NAME"] = "OrgName"
        environ["VENV_SECRETS_DIR"] = ""
        environ["VENVIT_DIR"] = ""

        env_var = EnvVarV060000Model()
        assert env_var.ENVIRONMENT == ""
        assert env_var.RTE_ENVIRONMENT == ""
        assert env_var.SCRIPTS_DIR == ""
        assert env_var.SECRETS_DIR == ""

        assert env_var.PROJECT_NAME == "Test"
        assert env_var.PROJECTS_BASE_DIR == Path("")
        assert env_var.VENV_CONFIG_DIR == Path("")
        assert env_var.VENV_ENVIRONMENT == "venv_environment"
        assert env_var.VENV_ORGANIZATION_NAME == "OrgName"
        assert env_var.VENV_SECRETS_DIR == Path("")
        assert env_var.VENVIT_DIR == Path("")
        pass

    def test_env_var_v070000_model(self):
        environ["ENVIRONMENT"] = ""
        environ["RTE_ENVIRONMENT"] = ""
        environ["SCRIPTS_DIR"] = ""
        environ["SECRETS_DIR"] = ""
        environ["VENV_CONFIG_DIR"] = ""
        environ["VENV_SECRETS_DIR"] = ""

        environ["PROJECT_NAME"] = "Test"
        environ["PROJECTS_BASE_DIR"] = "."
        environ["VENV_ENVIRONMENT"] = "venv_environment"
        environ["VENV_CONFIG_DEFAULT_DIR"] = ""
        environ["VENV_CONFIG_USER_DIR"] = ""
        environ["VENV_ORGANIZATION_NAME"] = "OrgName"
        environ["VENV_SECRETS_DEFAULT_DIR"] = ""
        environ["VENV_SECRETS_USER_DIR"] = ""
        environ["VENVIT_DIR"] = ""

        env_var = EnvVarV070000Model()
        assert env_var.ENVIRONMENT == ""
        assert env_var.RTE_ENVIRONMENT == ""
        assert env_var.SCRIPTS_DIR == ""
        assert env_var.SECRETS_DIR == ""
        assert env_var.VENV_CONFIG_DIR == ""
        assert env_var.VENV_SECRETS_DIR == ""

        assert env_var.PROJECT_NAME == "Test"
        assert env_var.PROJECTS_BASE_DIR == Path("")
        assert env_var.VENV_ENVIRONMENT == "venv_environment"
        assert env_var.VENV_CONFIG_DEFAULT_DIR == Path("")
        assert env_var.VENV_CONFIG_USER_DIR == Path("")
        assert env_var.VENV_ORGANIZATION_NAME == "OrgName"
        assert env_var.VENV_SECRETS_DEFAULT_DIR == Path("")
        assert env_var.VENV_SECRETS_USER_DIR == Path("")
        assert env_var.VENVIT_DIR == Path("")
        pass

    def test_env_var_v070300_model(self):
        environ["ENVIRONMENT"] = ""
        environ["RTE_ENVIRONMENT"] = ""
        environ["SCRIPTS_DIR"] = ""
        environ["SECRETS_DIR"] = ""
        environ["VENV_CONFIG_DIR"] = ""
        environ["VENV_SECRETS_DIR"] = ""
        environ["VENV_CONFIG_DEFAULT_DIR"] = ""
        environ["VENV_CONFIG_USER_DIR"] = ""
        environ["VENV_SECRETS_DEFAULT_DIR"] = ""
        environ["VENV_SECRETS_USER_DIR"] = ""

        environ["APPDATA"] = ""
        environ["PROJECT_NAME"] = "Test"
        environ["PROJECTS_BASE_DIR"] = "."
        environ["VENV_ENVIRONMENT"] = "venv_environment"
        environ["VENV_ORGANIZATION_NAME"] = "OrgName"
        environ["VENVIT_DIR"] = ""

        env_var = EnvVarV070300Model()
        assert env_var.ENVIRONMENT == ""
        assert env_var.RTE_ENVIRONMENT == ""
        assert env_var.SCRIPTS_DIR == ""
        assert env_var.SECRETS_DIR == ""
        assert env_var.VENV_CONFIG_DIR == ""
        assert env_var.VENV_SECRETS_DIR == ""
        assert env_var.VENV_CONFIG_DEFAULT_DIR == ""
        assert env_var.VENV_CONFIG_USER_DIR == ""
        assert env_var.VENV_SECRETS_DEFAULT_DIR == ""
        assert env_var.VENV_SECRETS_USER_DIR == ""

        assert env_var.APPDATA == Path("")
        assert env_var.PROJECT_NAME == "Test"
        assert env_var.PROJECTS_BASE_DIR == Path("")
        assert env_var.VENV_ENVIRONMENT == "venv_environment"
        assert env_var.VENV_ORGANIZATION_NAME == "OrgName"
        assert env_var.VENVIT_DIR == Path("")
        pass

    def test_env_var_set_000000_model(self):
        environ["ENVIRONMENT"] = "dev"
        environ["RTE_ENVIRONMENT"] = "dev"
        environ["SCRIPTS_DIR"] = ""
        environ["SECRETS_DIR"] = ""
        environ["VENV_BASE_DIR"] = ""
        environ["VENV_PYTHON_BASE_DIR"] = ""
        environ["VIRTUAL_ENV"] = "virtual_env"

        env_vars = EnvVarV000000Model()
        env_var_set_def = EnvVarSetV000000Model(
            environment=EnvVarSettingsModel(
                def_val=env_vars.ENVIRONMENT,
                is_dir=False,
                system_mandatory=False,
            ),
            rte_environment=EnvVarSettingsModel(
                def_val=env_vars.RTE_ENVIRONMENT,
                is_dir=False,
                system_mandatory=False,
            ),
            scripts_dir=EnvVarSettingsModel(
                def_val=env_vars.SCRIPTS_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            secrets_dir=EnvVarSettingsModel(
                def_val=env_vars.SECRETS_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            venv_base_dir=EnvVarSettingsModel(
                def_val=env_vars.VENV_BASE_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            venv_python_base_dir=EnvVarSettingsModel(
                def_val=env_vars.VENV_PYTHON_BASE_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            virtual_env=EnvVarSettingsModel(
                def_val=env_vars.VIRTUAL_ENV,
                is_dir=False,
                system_mandatory=False,
            ),
        )
        assert env_var_set_def.environment.def_val == "dev"
        assert env_var_set_def.environment.is_dir is False
        assert env_var_set_def.environment.system_mandatory is False

        assert env_var_set_def.rte_environment.def_val == "dev"
        assert env_var_set_def.rte_environment.is_dir is False
        assert env_var_set_def.rte_environment.system_mandatory is False

        assert env_var_set_def.scripts_dir.def_val == Path("")
        assert env_var_set_def.scripts_dir.is_dir is True
        assert env_var_set_def.scripts_dir.system_mandatory is True

        assert env_var_set_def.secrets_dir.def_val == Path("")
        assert env_var_set_def.secrets_dir.is_dir is True
        assert env_var_set_def.secrets_dir.system_mandatory is True

        assert env_var_set_def.venv_base_dir.def_val == Path("")
        assert env_var_set_def.venv_base_dir.is_dir is True
        assert env_var_set_def.venv_base_dir.system_mandatory is True

        assert env_var_set_def.venv_python_base_dir.def_val == Path("")
        assert env_var_set_def.venv_python_base_dir.is_dir is True
        assert env_var_set_def.venv_python_base_dir.system_mandatory is True

        assert env_var_set_def.virtual_env.def_val == "virtual_env"
        assert env_var_set_def.virtual_env.is_dir is False
        assert env_var_set_def.virtual_env.system_mandatory is False

        pass

    def test_env_var_set_060000_model(self):
        environ["PROJECT_NAME"] = "MyProject"
        environ["PROJECTS_BASE_DIR"] = ""
        environ["VENV_BASE_DIR"] = ""
        environ["VENV_CONFIG_DIR"] = ""
        environ["VENV_ENVIRONMENT"] = "my_environment"
        environ["VENV_ORGANIZATION_NAME"] = "MyOrg"
        environ["VENV_PYTHON_BASE_DIR"] = ""
        environ["VENV_SECRETS_DIR"] = ""
        environ["VENVIT_DIR"] = ""
        environ["VIRTUAL_ENV"] = "virtual_env"

        env_vars = EnvVarV060000Model()
        env_var_set_def = EnvVarSetV060000Model(
            project_name=EnvVarSettingsModel(
                def_val=env_vars.PROJECT_NAME,
                is_dir=False,
                system_mandatory=True,
            ),
            projects_base_dir=EnvVarSettingsModel(
                def_val=env_vars.PROJECTS_BASE_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            venv_base_dir=EnvVarSettingsModel(
                def_val=env_vars.VENV_BASE_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            venv_config_dir=EnvVarSettingsModel(
                def_val=env_vars.VENV_CONFIG_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            venv_environment=EnvVarSettingsModel(
                def_val=env_vars.VENV_ENVIRONMENT,
                is_dir=False,
                system_mandatory=False,
            ),
            venv_organization_name=EnvVarSettingsModel(
                def_val=env_vars.VENV_ORGANIZATION_NAME,
                is_dir=False,
                system_mandatory=False,
            ),
            venv_python_base_dir=EnvVarSettingsModel(
                def_val=env_vars.VENV_PYTHON_BASE_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            venv_secrets_dir=EnvVarSettingsModel(
                def_val=env_vars.VENV_SECRETS_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            venvit_dir=EnvVarSettingsModel(
                def_val=env_vars.VENVIT_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            virtual_env=EnvVarSettingsModel(
                def_val=env_vars.VIRTUAL_ENV,
                is_dir=False,
                system_mandatory=False,
            ),
        )
        assert env_var_set_def.project_name.def_val == "MyProject"
        assert env_var_set_def.project_name.is_dir is False
        assert env_var_set_def.project_name.system_mandatory is True

        assert env_var_set_def.projects_base_dir.def_val == Path("")
        assert env_var_set_def.projects_base_dir.is_dir is True
        assert env_var_set_def.projects_base_dir.system_mandatory is True

        assert env_var_set_def.venv_base_dir.def_val == Path("")
        assert env_var_set_def.venv_base_dir.is_dir is True
        assert env_var_set_def.venv_base_dir.system_mandatory is True

        assert env_var_set_def.venv_config_dir.def_val == Path("")
        assert env_var_set_def.venv_config_dir.is_dir is True
        assert env_var_set_def.venv_config_dir.system_mandatory is True

        assert env_var_set_def.venv_environment.def_val == "my_environment"
        assert env_var_set_def.venv_environment.is_dir is False
        assert env_var_set_def.venv_environment.system_mandatory is False

        assert env_var_set_def.venv_organization_name.def_val == "MyOrg"
        assert env_var_set_def.venv_organization_name.is_dir is False
        assert env_var_set_def.venv_organization_name.system_mandatory is False

        assert env_var_set_def.venv_python_base_dir.def_val == Path("")
        assert env_var_set_def.venv_python_base_dir.is_dir is True
        assert env_var_set_def.venv_python_base_dir.system_mandatory is True

        assert env_var_set_def.venv_secrets_dir.def_val == Path("")
        assert env_var_set_def.venv_secrets_dir.is_dir is True
        assert env_var_set_def.venv_secrets_dir.system_mandatory is True

        assert env_var_set_def.venvit_dir.def_val == Path("")
        assert env_var_set_def.venvit_dir.is_dir is True
        assert env_var_set_def.venvit_dir.system_mandatory is True

        assert env_var_set_def.virtual_env.def_val == "virtual_env"
        assert env_var_set_def.virtual_env.is_dir is False
        assert env_var_set_def.virtual_env.system_mandatory is False

        pass

    def test_env_var_set_070000_model(self):
        environ["PROJECT_NAME"] = "MyProject"
        environ["PROJECTS_BASE_DIR"] = ""
        environ["VENV_BASE_DIR"] = ""
        environ["VENV_CONFIG_DEFAULT_DIR"] = ""
        environ["VENV_CONFIG_USER_DIR"] = ""
        environ["VENV_ENVIRONMENT"] = "my_environment"
        environ["VENV_ORGANIZATION_NAME"] = "MyOrg"
        environ["VENV_PYTHON_BASE_DIR"] = ""
        environ["VENV_SECRETS_DEFAULT_DIR"] = ""
        environ["VENV_SECRETS_USER_DIR"] = ""
        environ["VENVIT_DIR"] = ""
        environ["VIRTUAL_ENV"] = "virtual_env"

        env_vars = EnvVarV070000Model()
        env_var_set_def = EnvVarSetV070000Model(
            project_name=EnvVarSettingsModel(
                def_val=env_vars.PROJECT_NAME,
                is_dir=False,
                system_mandatory=True,
            ),
            projects_base_dir=EnvVarSettingsModel(
                def_val=env_vars.PROJECTS_BASE_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            venv_base_dir=EnvVarSettingsModel(
                def_val=env_vars.VENV_BASE_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            venv_config_default_dir=EnvVarSettingsModel(
                def_val=env_vars.VENV_CONFIG_DEFAULT_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            venv_config_user_dir=EnvVarSettingsModel(
                def_val=env_vars.VENV_CONFIG_USER_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            venv_environment=EnvVarSettingsModel(
                def_val=env_vars.VENV_ENVIRONMENT,
                is_dir=False,
                system_mandatory=False,
            ),
            venv_organization_name=EnvVarSettingsModel(
                def_val=env_vars.VENV_ORGANIZATION_NAME,
                is_dir=False,
                system_mandatory=False,
            ),
            venv_python_base_dir=EnvVarSettingsModel(
                def_val=env_vars.VENV_PYTHON_BASE_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            venv_secrets_default_dir=EnvVarSettingsModel(
                def_val=env_vars.VENV_SECRETS_DEFAULT_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            venv_secrets_user_dir=EnvVarSettingsModel(
                def_val=env_vars.VENV_SECRETS_USER_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            venvit_dir=EnvVarSettingsModel(
                def_val=env_vars.VENVIT_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            virtual_env=EnvVarSettingsModel(
                def_val=env_vars.VIRTUAL_ENV,
                is_dir=False,
                system_mandatory=False,
            ),
        )
        assert env_var_set_def.venv_config_dir is None
        assert env_var_set_def.venv_secrets_dir is None

        assert env_var_set_def.project_name.def_val == "MyProject"
        assert env_var_set_def.project_name.is_dir is False
        assert env_var_set_def.project_name.system_mandatory is True

        assert env_var_set_def.projects_base_dir.def_val == Path("")
        assert env_var_set_def.projects_base_dir.is_dir is True
        assert env_var_set_def.projects_base_dir.system_mandatory is True

        assert env_var_set_def.venv_base_dir.def_val == Path("")
        assert env_var_set_def.venv_base_dir.is_dir is True
        assert env_var_set_def.venv_base_dir.system_mandatory is True

        assert env_var_set_def.venv_config_default_dir.def_val == Path("")
        assert env_var_set_def.venv_config_default_dir.is_dir is True
        assert env_var_set_def.venv_config_default_dir.system_mandatory is True

        assert env_var_set_def.venv_config_user_dir.def_val == Path("")
        assert env_var_set_def.venv_config_user_dir.is_dir is True
        assert env_var_set_def.venv_config_user_dir.system_mandatory is True

        assert env_var_set_def.venv_environment.def_val == "my_environment"
        assert env_var_set_def.venv_environment.is_dir is False
        assert env_var_set_def.venv_environment.system_mandatory is False

        assert env_var_set_def.venv_organization_name.def_val == "MyOrg"
        assert env_var_set_def.venv_organization_name.is_dir is False
        assert env_var_set_def.venv_organization_name.system_mandatory is False

        assert env_var_set_def.venv_python_base_dir.def_val == Path("")
        assert env_var_set_def.venv_python_base_dir.is_dir is True
        assert env_var_set_def.venv_python_base_dir.system_mandatory is True

        assert env_var_set_def.venv_secrets_default_dir.def_val == Path("")
        assert env_var_set_def.venv_secrets_default_dir.is_dir is True
        assert env_var_set_def.venv_secrets_default_dir.system_mandatory is True

        assert env_var_set_def.venv_secrets_user_dir.def_val == Path("")
        assert env_var_set_def.venv_secrets_user_dir.is_dir is True
        assert env_var_set_def.venv_secrets_user_dir.system_mandatory is True

        assert env_var_set_def.venvit_dir.def_val == Path("")
        assert env_var_set_def.venvit_dir.is_dir is True
        assert env_var_set_def.venvit_dir.system_mandatory is True

        assert env_var_set_def.virtual_env.def_val == "virtual_env"
        assert env_var_set_def.virtual_env.is_dir is False
        assert env_var_set_def.virtual_env.system_mandatory is False

        pass

    def test_env_var_set_070300_model(self):
        environ["APPDATA"] = ""
        environ["PROJECT_NAME"] = "MyProject"
        environ["PROJECTS_BASE_DIR"] = ""
        environ["VENV_BASE_DIR"] = ""
        environ["VENV_ENVIRONMENT"] = "my_environment"
        environ["VENV_ORGANIZATION_NAME"] = "MyOrg"
        environ["VENV_PYTHON_BASE_DIR"] = ""
        environ["VENVIT_DIR"] = ""
        environ["VIRTUAL_ENV"] = "virtual_env"

        env_vars = EnvVarV070300Model()
        env_var_set_def = EnvVarSetV070300Model(
            app_data=EnvVarSettingsModel(
                def_val=env_vars.APPDATA,
                is_dir=True,
                system_mandatory=False,
            ),
            project_name=EnvVarSettingsModel(
                def_val=env_vars.PROJECT_NAME,
                is_dir=False,
                system_mandatory=True,
            ),
            projects_base_dir=EnvVarSettingsModel(
                def_val=env_vars.PROJECTS_BASE_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            venv_base_dir=EnvVarSettingsModel(
                def_val=env_vars.VENV_BASE_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            venv_environment=EnvVarSettingsModel(
                def_val=env_vars.VENV_ENVIRONMENT,
                is_dir=False,
                system_mandatory=False,
            ),
            venv_organization_name=EnvVarSettingsModel(
                def_val=env_vars.VENV_ORGANIZATION_NAME,
                is_dir=False,
                system_mandatory=False,
            ),
            venv_python_base_dir=EnvVarSettingsModel(
                def_val=env_vars.VENV_PYTHON_BASE_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            venvit_dir=EnvVarSettingsModel(
                def_val=env_vars.VENVIT_DIR,
                is_dir=True,
                system_mandatory=True,
            ),
            virtual_env=EnvVarSettingsModel(
                def_val=env_vars.VIRTUAL_ENV,
                is_dir=False,
                system_mandatory=False,
            ),
        )
        assert env_var_set_def.venv_config_dir is None
        assert env_var_set_def.venv_secrets_dir is None
        assert env_var_set_def.venv_config_default_dir is None
        assert env_var_set_def.venv_config_user_dir is None
        assert env_var_set_def.venv_secrets_default_dir is None
        assert env_var_set_def.venv_secrets_user_dir is None

        assert env_var_set_def.app_data.def_val == Path("")
        assert env_var_set_def.app_data.is_dir is True
        assert env_var_set_def.app_data.system_mandatory is False

        assert env_var_set_def.project_name.def_val == "MyProject"
        assert env_var_set_def.project_name.is_dir is False
        assert env_var_set_def.project_name.system_mandatory is True

        assert env_var_set_def.projects_base_dir.def_val == Path("")
        assert env_var_set_def.projects_base_dir.is_dir is True
        assert env_var_set_def.projects_base_dir.system_mandatory is True

        assert env_var_set_def.venv_base_dir.def_val == Path("")
        assert env_var_set_def.venv_base_dir.is_dir is True
        assert env_var_set_def.venv_base_dir.system_mandatory is True

        assert env_var_set_def.venv_environment.def_val == "my_environment"
        assert env_var_set_def.venv_environment.is_dir is False
        assert env_var_set_def.venv_environment.system_mandatory is False

        assert env_var_set_def.venv_organization_name.def_val == "MyOrg"
        assert env_var_set_def.venv_organization_name.is_dir is False
        assert env_var_set_def.venv_organization_name.system_mandatory is False

        assert env_var_set_def.venv_python_base_dir.def_val == Path("")
        assert env_var_set_def.venv_python_base_dir.is_dir is True
        assert env_var_set_def.venv_python_base_dir.system_mandatory is True

        assert env_var_set_def.venvit_dir.def_val == Path("")
        assert env_var_set_def.venvit_dir.is_dir is True
        assert env_var_set_def.venvit_dir.system_mandatory is True

        assert env_var_set_def.virtual_env.def_val == "virtual_env"
        assert env_var_set_def.virtual_env.is_dir is False
        assert env_var_set_def.virtual_env.system_mandatory is False

        pass

    def test_env_setup_v070000_init(self, env_setup_07_00_00_self_destruct):
        env_setup = env_setup_07_00_00_self_destruct

        assert env_setup.env_vars.PROJECT_NAME == "ProjectName"
        assert env_setup.env_vars.PROJECTS_BASE_DIR == Path(environ.get("PROJECTS_BASE_DIR"))
        assert env_setup.env_vars.VENV_BASE_DIR == Path(environ.get("VENV_BASE_DIR"))
        assert env_setup.env_vars.VENV_ENVIRONMENT == "dev"
        assert env_setup.env_vars.VENV_ORGANIZATION_NAME == "OrgName"
        assert env_setup.env_vars.VENVIT_DIR == Path(environ.get("VENVIT_DIR"))

        assert env_setup.env_var_set_def.venv_config_dir is None
        assert env_setup.env_var_set_def.venv_secrets_dir is None

        assert env_setup.env_var_set_def.project_name.def_val == "ProjectName"
        assert env_setup.env_var_set_def.projects_base_dir.def_val == Path(environ.get("PROJECTS_BASE_DIR"))
        assert env_setup.env_var_set_def.venv_base_dir.def_val == Path(environ.get("VENV_BASE_DIR"))
        assert env_setup.env_var_set_def.venv_environment.def_val == "dev"
        assert env_setup.env_var_set_def.venv_organization_name.def_val == "OrgName"
        assert env_setup.env_var_set_def.venv_python_base_dir.def_val == Path(environ.get("VENV_PYTHON_BASE_DIR"))
        assert env_setup.env_var_set_def.venvit_dir.def_val == Path(environ.get("VENVIT_DIR"))
        assert env_setup.env_var_set_def.virtual_env.def_val == "virtual_env"

        pass

    def test_env_setup_v070300_setup_structure(self, env_setup_07_00_00_self_destruct):
        env_setup = env_setup_07_00_00_self_destruct
        env_setup.setup_structure()

        assert env_setup.env_var_set_def.projects_base_dir.def_val.exists()
        assert env_setup.env_var_set_def.venv_base_dir.def_val.exists()
        assert env_setup.env_var_set_def.venv_config_default_dir.def_val.exists()
        assert env_setup.env_var_set_def.venv_config_user_dir.def_val.exists()
        assert env_setup.env_var_set_def.venv_python_base_dir.def_val.exists()
        assert env_setup.env_var_set_def.venv_secrets_default_dir.def_val.exists()
        assert env_setup.env_var_set_def.venv_secrets_user_dir.def_val.exists()
        assert env_setup.env_var_set_def.venvit_dir.def_val.exists()
        assert Path(Path.home(), "VEnvIt", "Config").exists()
        assert Path(Path.home(), "VEnvIt", "Secrets").exists()
        pass

    def test_env_setup_v070300_init(self, env_setup_07_02_00_self_destruct):
        env_setup = env_setup_07_02_00_self_destruct

        assert env_setup.env_vars.APPDATA == Path(environ.get("APPDATA"))
        assert env_setup.env_vars.PROJECT_NAME == "MyProject"
        assert env_setup.env_vars.PROJECTS_BASE_DIR == Path(environ.get("PROJECTS_BASE_DIR"))
        assert env_setup.env_vars.VENV_BASE_DIR == Path(environ.get("VENV_BASE_DIR"))
        assert env_setup.env_vars.VENV_ENVIRONMENT == "dev"
        assert env_setup.env_vars.VENV_ORGANIZATION_NAME == "MyOrg"
        assert env_setup.env_vars.VENVIT_DIR == Path(environ.get("VENVIT_DIR"))

        assert env_setup.env_var_set_def.venv_config_dir is None
        assert env_setup.env_var_set_def.venv_secrets_dir is None
        assert env_setup.env_var_set_def.venv_config_default_dir is None
        assert env_setup.env_var_set_def.venv_config_user_dir is None
        assert env_setup.env_var_set_def.venv_secrets_default_dir is None
        assert env_setup.env_var_set_def.venv_secrets_user_dir is None

        assert env_setup.env_var_set_def.app_data.def_val == Path(environ.get("APPDATA"))
        assert env_setup.env_var_set_def.project_name.def_val == "MyProject"
        assert env_setup.env_var_set_def.projects_base_dir.def_val == Path(environ.get("PROJECTS_BASE_DIR"))
        assert env_setup.env_var_set_def.venv_base_dir.def_val == Path(environ.get("VENV_BASE_DIR"))
        assert env_setup.env_var_set_def.venv_environment.def_val == "dev"
        assert env_setup.env_var_set_def.venv_organization_name.def_val == "MyOrg"
        assert env_setup.env_var_set_def.venv_python_base_dir.def_val == Path(environ.get("VENV_PYTHON_BASE_DIR"))
        assert env_setup.env_var_set_def.venvit_dir.def_val == Path(environ.get("VENVIT_DIR"))
        assert env_setup.env_var_set_def.virtual_env.def_val == "hendr\\venv\\MyProject_env"

        pass

    def test_env_setup_v070300_get_config_filename(self):
        setup = EnvSetUpV070300()
        filename = setup.get_config_filename(project_name="test_project", postfix="lastbit")

        assert filename == "VEnvtest_projectlastbit.ps1"
        pass

    def test_env_setup_v070300_get_secrets_filename(self):
        setup = EnvSetUpV070300()
        filename = setup.get_secrets_filename()

        assert filename == "Secrets.ps1"
        pass
