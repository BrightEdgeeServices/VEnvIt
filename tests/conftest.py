from os import environ
from pathlib import Path
from tempfile import mkdtemp
from tempfile import TemporaryDirectory

import pytest
from beetools.utils import rm_tree

from tests.testdata import test_data
from venvit.core.env_setup import EnvSetUpV000000
from venvit.core.env_setup import EnvSetUpV060000
from venvit.core.env_setup import EnvSetUpV070000
from venvit.core.env_setup import EnvSetUpV070300

# sys.path.append('path')


def create_config_files(setup, project_list):
    for project in project_list:
        for config_type in ["CustomSetup", "EnvVar", "Install"]:
            config_filename = setup.get_config_filename(project, config_type)
            Path(setup.env_var_set_def.venv_config_default_dir.def_val / config_filename).touch()
            Path(setup.env_var_set_def.venv_config_user_dir.def_val / config_filename).touch()
        secrets_filename = setup.get_secrets_filename()
        Path(setup.env_var_set_def.venv_secrets_default_dir.def_val / secrets_filename).touch()
        Path(setup.env_var_set_def.venv_secrets_user_dir.def_val / secrets_filename).touch()


class WorkingDir:
    def __init__(self, p_secure=True):
        if p_secure:
            self.dir = Path(mkdtemp(prefix="venvit_"))
        else:
            self.dir = Path(str(TemporaryDirectory()))


@pytest.fixture
def env_setup_v000000_self_destruct():
    base_dir = WorkingDir().dir
    environment = test_data.v000000["scripts_dir"]
    rte_environment = test_data.v000000["scripts_dir"]
    scripts_dir = Path(base_dir / test_data.v000000["scripts_dir"])
    secrets_dir = Path(base_dir / test_data.v000000["secrets_dir"])
    venv_base_dir = Path(base_dir / test_data.v000000["venv_base_dir"])
    venv_python_base_dir = Path(base_dir / test_data.v000000["venv_python_base_dir"])
    virtual_env = test_data.v000000["virtual_env"]

    environ["ENVIRONMENT"] = environment
    environ["RTE_ENVIRONMENT"] = rte_environment
    environ["SCRIPTS_DIR"] = str(scripts_dir)
    environ["SECRETS_DIR"] = str(secrets_dir)
    environ["VENV_BASE_DIR"] = str(venv_base_dir)
    environ["VENV_PYTHON_BASE_DIR"] = str(venv_python_base_dir)
    environ["VIRTUAL_ENV"] = virtual_env

    setup_env = EnvSetUpV000000()

    yield setup_env
    rm_tree(base_dir, p_crash=False)


@pytest.fixture
def env_setup_06_00_00_self_destruct():
    base_dir = WorkingDir().dir
    project_name: str = test_data.v000000["project_name"]
    projects_base_dir = Path(base_dir / test_data.v000000["projects_base_dir"])
    venv_base_dir = Path(base_dir / test_data.v000000["venv_base_dir"])
    venv_config_dir = Path(base_dir / test_data.v000000["venv_config_dir"])
    venv_environment: str = test_data.v000000["venv_environment"]
    venv_organization_name: str = test_data.v000000["venv_organization_name"]
    venv_python_base_dir = Path(base_dir / test_data.v000000["venv_python_base_dir"])
    venv_secrets_dir = Path(base_dir / test_data.v000000["venv_secrets_dir"])
    venvit_dir: Path = Path(base_dir / test_data.v000000["venvit_dir"])
    virtual_env = test_data.v000000["virtual_env"]

    environ["PROJECT_NAME"] = project_name
    environ["PROJECTS_BASE_DIR"] = str(projects_base_dir)
    environ["VENV_BASE_DIR"] = str(venv_base_dir)
    environ["VENV_CONFIG_DIR"] = str(venv_config_dir)
    environ["VENV_ENVIRONMENT"] = venv_environment
    environ["VENV_ORGANIZATION_NAME"] = venv_organization_name
    environ["VENV_PYTHON_BASE_DIR"] = str(venv_python_base_dir)
    environ["VENV_SECRETS_DIR"] = str(venv_secrets_dir)
    environ["VENVIT_DIR"] = str(venvit_dir)
    environ["VIRTUAL_ENV"] = virtual_env

    setup_env = EnvSetUpV060000()

    yield setup_env
    rm_tree(base_dir, p_crash=False)


@pytest.fixture
def env_setup_07_00_00_self_destruct_virgin(monkeypatch):
    base_dir = WorkingDir().dir
    app_data: Path = Path(base_dir / test_data.v070300["app_data"])
    project_name = test_data.v070000["project_name"]
    projects_base_dir = Path(base_dir / test_data.v070000["projects_base_dir"])
    venv_base_dir = Path(base_dir / test_data.v070000["venv_base_dir"])
    venv_config_default_dir = Path(base_dir / test_data.v070000["venv_config_default_dir"])
    venv_config_user_dir = Path(base_dir / test_data.v070000["venv_config_user_dir"])
    venv_environment: str = test_data.v070000["venv_environment"]
    venv_organization_name = test_data.v070000["venv_organization_name"]
    venv_python_base_dir = Path(base_dir / test_data.v070000["venv_python_base_dir"])
    venv_secrets_default_dir = Path(base_dir / test_data.v070000["venv_secrets_default_dir"])
    venv_secrets_user_dir = Path(base_dir / test_data.v070000["venv_secrets_user_dir"])
    venvit_dir = Path(base_dir / test_data.v070000["venvit_dir"])
    virtual_env = test_data.v070000["virtual_env"]

    environ["PROJECT_NAME"] = project_name
    environ["PROJECTS_BASE_DIR"] = str(projects_base_dir)
    environ["VENV_BASE_DIR"] = str(venv_base_dir)
    environ["VENV_CONFIG_DEFAULT_DIR"] = str(venv_config_default_dir)
    environ["VENV_CONFIG_USER_DIR"] = str(venv_config_user_dir)
    environ["VENV_ENVIRONMENT"] = venv_environment
    environ["VENV_ORGANIZATION_NAME"] = venv_organization_name
    environ["VENV_PYTHON_BASE_DIR"] = str(venv_python_base_dir)
    environ["VENV_SECRETS_DEFAULT_DIR"] = str(venv_secrets_default_dir)
    environ["VENV_SECRETS_USER_DIR"] = str(venv_secrets_user_dir)
    environ["VENVIT_DIR"] = str(venvit_dir)
    environ["VIRTUAL_ENV"] = virtual_env
    monkeypatch.setenv("APPDATA", str(app_data))

    env_var_setup = EnvSetUpV070000()

    yield env_var_setup
    rm_tree(base_dir, p_crash=False)


@pytest.fixture
def env_setup_07_00_00_self_destruct_with_config_files(monkeypatch, env_setup_07_00_00_self_destruct_virgin):
    env_var_setup = env_setup_07_00_00_self_destruct_virgin
    env_var_setup.setup_structure()
    create_config_files(env_var_setup, ["MyProject", "YourProject"])

    yield env_var_setup


@pytest.fixture
def env_setup_07_03_00_self_destruct(monkeypatch):
    base_dir = WorkingDir().dir
    app_data: Path = Path(base_dir / test_data.v070300["app_data"])
    project_name: str = test_data.v070300["project_name"]
    projects_base_dir = Path(base_dir / test_data.v070300["projects_base_dir"])
    venv_base_dir = Path(base_dir / test_data.v070300["venv_base_dir"])
    venv_environment: str = test_data.v070300["venv_environment"]
    venv_organization_name: str = test_data.v070300["venv_organization_name"]
    venv_python_base_dir = Path(base_dir / test_data.v070300["venv_python_base_dir"])
    venvit_dir: Path = Path(base_dir / test_data.v070300["venvit_dir"])
    virtual_env = test_data.v070300["virtual_env"]

    environ["APPDATA"] = str(app_data)
    environ["PROJECT_NAME"] = project_name
    environ["PROJECTS_BASE_DIR"] = str(projects_base_dir)
    environ["VENV_BASE_DIR"] = str(venv_base_dir)
    environ["VENV_ENVIRONMENT"] = venv_environment
    environ["VENV_ORGANIZATION_NAME"] = venv_organization_name
    environ["VENV_PYTHON_BASE_DIR"] = str(venv_python_base_dir)
    environ["VENVIT_DIR"] = str(venvit_dir)
    environ["VIRTUAL_ENV"] = virtual_env
    monkeypatch.setenv("APPDATA", str(base_dir))

    setup_env = EnvSetUpV070300()

    yield setup_env
    rm_tree(base_dir, p_crash=False)
