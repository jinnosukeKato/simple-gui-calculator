from lark import Lark
import tkinter
import tkinter.ttk as ttk

from core import Eval, PARSER

root = tkinter.Tk()
root.title("Simple GUI Calculator")
root.geometry("400x400")


class Calculator:
    def __init__(self):

        self.display_str = ""
        self.display = ttk.Label(root)
        self.display.pack()
        self.frame = ttk.Frame(root)

        # キーの作成
        for num in range(10):
            ttk.Button(
                self.frame,
                text=num,
                command=lambda n=num: self.on_input(n)
            ).pack()

        ttk.Button(
            self.frame,
            text="+",
            command=lambda op="+": self.on_input(op)
        ).pack()

        ttk.Button(
            self.frame,
            text="=",
            command=self.on_enter
        ).pack()

        self.frame.pack()

    def on_input(self, char):
        self.display_str += str(char)
        self.display.config(text=self.display_str)

    def on_enter(self):
        self.on_input("=")
        tree = PARSER.parse(self.display_str)
        self.on_input(Eval().transform(tree))


gui = Calculator()
root.mainloop()
