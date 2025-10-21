from lark import Lark, Transformer


class Eval(Transformer):
    # それぞれのルール名に関数が対応
    def sum(self, values) -> float:
        result = float(values[0])
        # [2::2]でvalue[2]から2個刻みのスライスができる ex) 2, 4, 6, ...
        # これにより，+を飛ばす
        for op, value in zip(values[1::2], values[2::2]):
            if op == "+":
                result += float(value)
            else:
                result -= float(value)
        return result

    def mul(self, values) -> float:
        result = float(values[0])
        for op, value in zip(values[1::2], values[2::2]):
            if op == "*":
                result *= float(value)
            else:
                result /= float(value)
        return result


with open("./calculator.lark", encoding="utf-8") as grammar:
    parser = Lark(grammar.read(), start="expr")

tree = parser.parse("2.0+2.5*-2=")
print(tree)
print(tree.pretty())
print(Eval().transform(tree))
