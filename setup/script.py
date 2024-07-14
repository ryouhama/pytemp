from logging import getLogger
from prompt import QuestionPrompt, Question
from update_pyproject import create_backup, overwrite_pyproject


logger = getLogger(__name__)


def main():
    logger.info("Start")
    answer_of_name = QuestionPrompt(Question("What's your project name")).ask()
    answer_of_description = QuestionPrompt(
        Question("What's your project description")
    ).ask()

    project_name = answer_of_name.value
    project_description = answer_of_description.value

    try:
        backup_file_path = create_backup()
        logger.info(f"Create backup file. {backup_file_path or None}")
    except Exception as e:
        logger.exception(e)
        return None

    try:
        overwrite_pyproject(project_name, project_description)
        logger.info("Overwrite pyproject.toml")
    except Exception as e:
        logger.exception(e)


if __name__ == "__main__":
    main()
