from lark import Lark, Transformer


class Eval(Transformer):
    # それぞれのルール名に関数が対応
    def sum(self, values) -> int:
        result = int(values[0])
        # [2::2]でvalue[2]から2個刻みのスライスができる ex) 0, 2, 4, ...
        # これにより，+を飛ばす
        for i in values[2::2]:
            result += int(i)
        return result


with open("./calculator.lark", encoding="utf-8") as grammar:
    parser = Lark(grammar.read(), start="sum")

tree = parser.parse("1+2+3+4=")
print(tree)
print(tree.pretty())
print(Eval().transform(tree))
