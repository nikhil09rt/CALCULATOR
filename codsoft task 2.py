# TASK 2:-  CALCULATOR

import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.result_var = tk.StringVar()

        self.create_ui()

    def create_ui(self):
        entry = tk.Entry(self.root, textvariable=self.result_var, font=("Helvetica", 18), bd=10, insertwidth=1, width=14, justify="right")
        entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row_num = 1
        col_num = 0

        for button_text in buttons:
            button = tk.Button(self.root, text=button_text, padx=20, pady=20, font=("Helvetica", 16), command=lambda text=button_text: self.button_click(text))
            button.grid(row=row_num, column=col_num)
            col_num += 1
            if col_num > 3:
                col_num = 0
                row_num += 1

    def button_click(self, text):
        if text == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif text == 'C':
            self.result_var.set("")
        else:
            current_text = self.result_var.get()
            new_text = current_text + text
            self.result_var.set(new_text)

def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
