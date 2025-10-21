from lark import Lark
import tkinter
import tkinter.ttk as ttk

from core import Eval, PARSER

root = tkinter.Tk()
root.title("Simple GUI Calculator")
root.geometry("400x400")


class Calculator:
    def __init__(self) -> None:
        self.is_calculated = False

        self.display_text = tkinter.StringVar(value="")
        self.display = ttk.Label(root, textvariable=self.display_text)
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
        if self.is_calculated:
            self.display_text.set("")
            self.is_calculated = False

        self.display_text.set(self.display_text.get() + str(char))

    def on_enter(self):
        self.on_input("=")
        try:
            tree = PARSER.parse(self.display_text.get())
        except:
            pass
        else:
            self.on_input(Eval().transform(tree))
        finally:
            self.is_calculated = True


gui = Calculator()
root.mainloop()
