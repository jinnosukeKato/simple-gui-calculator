import enum
from enum import Enum


class TokenType(Enum):
    NUMBER = enum.auto()
    ADD = enum.auto()
    SUB = enum.auto()
    MUL = enum.auto()
    DIV = enum.auto()


class Token():
    def __init__(self, token_type: TokenType, value: float | None = None):
        self.token_type = token_type
        self.value = value

    def __str__(self) -> str:
        return f"type: {self.token_type}, value: {self.value}"


class State(Enum):
    INTEGER_PART_MSD = enum.auto()  # most significant digit
    INTEGER_PART = enum.auto()
    FRACTIONAL_PART = enum.auto()


class Tokenizer:
    def __init__(self, input: str):
        self.iter_input = iter(list(input))
        self.state = State.INTEGER_PART_MSD
        try:
            self.current_char = next(self.iter_input)
        except StopIteration:
            self.current_char = '\n'

    def __iter__(self):
        return self

    def _move_next(self):
        try:
            self.current_char = next(self.iter_input)
        except StopIteration:
            self.current_char = '\n'

    def __next__(self) -> Token:
        while self.current_char != '\n' and self.current_char.isspace():
            self._move_next()

        if self.current_char == '\n':
            raise StopIteration()

        if '1' <= self.current_char <= '9':
            num = self.current_char
            self._move_next()

            while self.current_char.isdigit():
                num += self.current_char
                self._move_next()

            if self.current_char == '.':
                num += '.'
                self._move_next()
                while self.current_char.isdigit():
                    num += self.current_char
                    self._move_next()

            return Token(TokenType.NUMBER, float(num))

        if self.current_char == '+':
            self._move_next()
            return Token(TokenType.ADD)

        raise StopIteration()


if __name__ == "__main__":
    tokenizer = Tokenizer(input())
    for token in tokenizer:
        print(token)
