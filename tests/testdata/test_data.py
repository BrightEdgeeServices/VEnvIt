from os import environ
from pathlib import Path

v000000 = {
    "environment": "dev",
    "rte_environment": "dev",
    "secrets_dir": "VEnvItSecrets",
    "venv_base_dir": "VenvBase",
    "venv_python_base_dir": "Python",
    "virtual_env": "virtual_env",
}

v060000 = {
    "project_name": "ProjectName",
    "projects_base_dir": "Projects",
    "venv_base_dir": "venv",
    "venv_config_dir": r"ProgramFiles\VenvIt\Config",
    "venv_environment": "dev",
    "venv_organization_name": "OrgName",
    "venv_python_base_dir": "Python",
    "venv_secrets_dir": r"ProgramFiles\VenvIt\Secrets",
    "venvit_dir": r"Program Files\VenvIt",
    "virtual_env": "virtual_env",
}

v070000 = {
    "home_path": environ.get("USERNAME"),
    "app_data": str(Path(environ.get("USERNAME"), "AppData")),
    "project_name": "MyProject",
    "projects_base_dir": str(Path(environ.get("USERNAME"), "Projects")),
    "venv_base_dir": str(Path(environ.get("USERNAME"), "venv")),
    "venv_config_default_dir": str(Path("Program Files", "VenvIt", "Config")),
    "venv_config_user_dir": str(Path(environ.get("USERNAME"), "VenvIt", "Config")),
    "venv_environment": "loc_dev",
    "venv_organization_name": "MyOrg",
    "venv_python_base_dir": r"c:\Python",
    "venv_secrets_default_dir": str(Path("Program Files", "VenvIt", "Secrets")),
    "venv_secrets_user_dir": str(Path(environ.get("USERNAME"), "VenvIt", "Secrets")),
    "venvit_dir": str(Path("Program Files", "VenvIt")),
    "virtual_env": str(Path(environ.get("USERNAME"), "venv", "MyProject_env")),
}
v070300 = {
    "home_path": environ.get("USERNAME"),
    "app_data": str(Path(environ.get("USERNAME"), "AppData")),
    "project_name": "MyProject",
    "projects_base_dir": str(Path(environ.get("USERNAME"), "Projects")),
    "venv_base_dir": str(Path(environ.get("USERNAME"), "venv")),
    "venv_environment": "loc_dev",
    "venv_organization_name": "MyOrg",
    "venv_python_base_dir": r"c:\Python",
    "venvit_dir": str(Path("Program Files", "VenvIt")),
    "virtual_env": str(Path(environ.get("USERNAME"), "venv", "MyProject_env")),
}
