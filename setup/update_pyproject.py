import os
import shutil
import datetime
from pathlib import Path
from typing import Final

PYPROJECT_FILE_NAME: Final[str] = "pyproject.toml"
BACK_UP_DIR_PATH: Final[str] = ".backup"
FILE_SUFFIX_FORMAT: Final[str] = "%Y%m%d%H%M%S"


def create_backup() -> str:
    current_datatime = datetime.datetime.now()

    if not os.path.isdir(BACK_UP_DIR_PATH):
        os.mkdir(BACK_UP_DIR_PATH)

    return shutil.copy(
        "pyproject.toml",
        f"{BACK_UP_DIR_PATH}/pyproject.toml.{current_datatime.strftime(FILE_SUFFIX_FORMAT)}",
    )


def overwrite_pyproject(project_name: str, project_description: str):
    pyproject = Path(PYPROJECT_FILE_NAME)
    content = (
        pyproject.read_text()
        .replace("pytemp", project_name)
        .replace('description = ""', f'description = "{project_description}"')
    )
    pyproject.write_text(content)
