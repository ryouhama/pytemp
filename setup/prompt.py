from dataclasses import dataclass
from constants import COLOR


@dataclass
class Answer:
    value: str


@dataclass
class Question:
    value: str


@dataclass
class QuestionPrompt:
    question: Question

    def ask(self) -> Answer:
        input_text = input(self.__format())
        print(COLOR.RESET, end="")
        return Answer(input_text)

    def __format(self) -> str:
        return f"{COLOR.BLUE}?{COLOR.RESET} {self.question.value}: {COLOR.YELLOW}"
