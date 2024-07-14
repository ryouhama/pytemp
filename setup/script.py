from prompt import QuestionPrompt, Question
from update_pyproject import create_backup, update_pyproject


def main():
    answer_of_name = QuestionPrompt(Question("What's your project name")).ask()
    answer_of_description = QuestionPrompt(
        Question("What's your project description")
    ).ask()

    project_name = answer_of_name.value
    project_description = answer_of_description.value

    create_backup()
    update_pyproject(project_name, project_description)


if __name__ == "__main__":
    main()
