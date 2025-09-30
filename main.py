import enum
from enum import Enum


class Token(Enum):
    NUMBER = enum.auto()
    ADD = enum.auto()
    SUB = enum.auto()
    MUL = enum.auto()
    DIV = enum.auto()

    def __init__(self, num):
        self.num = num


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

    def _skip(self):
        try:
            self.current_char = next(self.iter_input)
        except StopIteration:
            self.current_char = '\n'

    def __next__(self) -> str:
        num: str = ""

        while True:
            if self.state == State.INTEGER_PART_MSD:
                if '1' <= self.current_char <= '9':
                    num = self.current_char
                    self.state = State.INTEGER_PART
                else:
                    # パースエラー
                    raise StopIteration()
            elif self.state == State.INTEGER_PART:
                if '0' <= self.current_char <= '9':
                    num += self.current_char
                elif self.current_char == '.':
                    # 少数部の処理へ飛ぶ
                    num += self.current_char
                    self.state = State.FRACTIONAL_PART
                elif self.current_char in {"+", "\n"}:
                    # 受理
                    self.state = State.INTEGER_PART_MSD
                    self._skip()
                    return num
                else:
                    raise StopIteration()
            elif self.state == State.FRACTIONAL_PART:
                if '0' <= self.current_char <= '9':
                    num += self.current_char
                elif self.current_char in {"+", "\n"}:
                    # 受理
                    self.state = State.INTEGER_PART_MSD
                    self._skip()
                    return num
                else:
                    raise StopIteration()

            # 次の文字へ進める
            try:
                self.current_char = next(self.iter_input)
            except StopIteration:
                self.current_char = '\n'


if __name__ == "__main__":
    tokenizer = Tokenizer(input())
    for token in tokenizer:
        print(token)
