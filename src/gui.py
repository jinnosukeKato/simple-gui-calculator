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
        layout = [
            ("7", 0, 0), ("8", 0, 1), ("9", 0, 2),
            ("4", 1, 0), ("5", 1, 1), ("6", 1, 2),
            ("1", 2, 0), ("2", 2, 1), ("3", 2, 2),
            ("0", 3, 1),
        ]
        for label, row, col in layout:
            ttk.Button(
                self.frame,
                text=label,
                command=lambda l=label: self.input(l)
            ).grid(row=row, column=col)

        for i, op in enumerate(["+", "-", "*", "/", "%", "^", "."]):
            ttk.Button(
                self.frame,
                text=op,
                command=lambda op=op: self.input(op)
            ).grid(row=i, column=3)

        ttk.Button(
            self.frame,
            text="=",
            command=self.on_enter
        ).grid(row=0, column=4)

        self.frame.pack()

    def input(self, char):
        if self.is_calculated:
            self.display_text.set("")
            self.is_calculated = False

        self.display_text.set(self.display_text.get() + str(char))

    def on_enter(self):
        self.input("=")
        try:
            tree = PARSER.parse(self.display_text.get())
        except:
            pass
        else:
            self.input(Eval().transform(tree))
        finally:
            self.is_calculated = True


gui = Calculator()
root.mainloop()
