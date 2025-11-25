from core import Eval, PARSER
import tkinter.ttk as ttk
import tkinter


root = tkinter.Tk()
root.title("Simple GUI Calculator")


class CalculatorGUI(ttk.Frame):
    def __init__(self) -> None:
        super().__init__(root)
        self.is_calculated = False

        self.display_text = tkinter.StringVar(value="")
        self.display = ttk.Label(
            root, textvariable=self.display_text, font=("Segoe UI", 20))
        self.display.pack()

        # キーの作成
        layout = [
            ("(", 0, 1), (")", 0, 2),
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3), ("%", 1, 4),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3), ("^", 2, 4),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 1), (".", 4, 2), ("+", 4, 3),
        ]

        for label, row, col in layout:
            ttk.Button(
                self,
                text=label,
                command=lambda l=label: self.input(l)
            ).grid(row=row, column=col)

        ttk.Button(
            self,
            text="=",
            command=self.on_enter
        ).grid(row=4, column=4)

        ttk.Button(
            self,
            text="BS",
            command=self.delete
        ).grid(row=4, column=0)

        ttk.Button(
            self,
            text="AC",
            command=self.all_clear
        ).grid(row=0, column=0)

        self.pack()

    def input(self, char):
        if self.is_calculated:
            self.display_text.set("")
            self.is_calculated = False

        self.display_text.set(self.display_text.get() + str(char))

    def on_enter(self):
        if self.is_calculated:
            return

        self.input("=")
        try:
            tree = PARSER.parse(self.display_text.get())
            result = Eval().transform(tree)
        except:
            self.display_text.set("Error")
        else:
            self.display_text.set(result)
        finally:
            self.is_calculated = True

    def delete(self):
        text = self.display_text.get()
        if self.is_calculated:
            self.all_clear()
        elif text:
            self.display_text.set(text[:-1])

    def all_clear(self):
        self.display_text.set("")
        self.is_calculated = False


gui = CalculatorGUI()
root.update_idletasks()
root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")
root.resizable(False, False)
root.mainloop()
