from tkinter import *
from tkinter import ttk
import math

class Calculator:
    def __init__(self, root):
        self.root = root

        self.operand1 = None
        self.operand2 = None
        self.operator = None
        self.memory = 0
        self.reset_next = False

        self.text_input = StringVar()
        self.screen = ttk.Label(root, textvariable=self.text_input, background="white", height=1, width=20, font=('Arial', 23))
        self.screen.grid(row=0, column=0, columnspan=5)

        buttons = [
            ('CE', 1, 0), ('/', 1, 1), ('*', 1, 2), ('-', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('+', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('=', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('√', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('+/-', 5, 2), ('!', 5, 3),
            ('M+', 6, 0), ('M-', 6, 1), ('MR', 6, 2), ('MC', 6, 3)
        ]

        for (text, row, col) in buttons:
            ttk.Button(root, text=text, padding=30, font=('Arial', 14), command=lambda x=text: self.on_button_click(x)).grid(row=row, column=col)

    def on_button_click(self, char):
        if char in '0123456789.':
            if self.reset_next:
                self.text_input.set("")
                self.reset_next = False
            current = self.text_input.get()
            self.text_input.set(current + char)
        elif char in '+-*/':
            if self.text_input.get():
                self.operand1 = float(self.text_input.get())
                self.operator = char
                self.reset_next = True
        elif char == 'CE':
            self.operand1 = None
            self.operand2 = None
            self.operator = None
            self.text_input.set("")
        elif char == '=':
            if self.operator and self.text_input.get():
                self.operand2 = float(self.text_input.get())
                result = self.calculate(self.operand1, self.operand2, self.operator)
                self.text_input.set(result)
                self.operand1 = result
                self.operator = None
                self.reset_next = True
        elif char == '√':
            try:
                value = float(self.text_input.get())
                result = value ** 0.5
                self.text_input.set(result)
                self.operand1 = result
                self.reset_next = True
            except:
                self.text_input.set("Error")
        elif char == '!':
            try:
                value = int(float(self.text_input.get()))
                result = math.factorial(value)
                self.text_input.set(result)
                self.operand1 = result
                self.reset_next = True
            except:
                self.text_input.set("Error")
        elif char == '+/-':
            try:
                value = self.text_input.get()
                if value:
                    if value[0] == '-':
                        value = value[1:]
                    else:
                        value = '-' + value
                    self.text_input.set(value)
            except:
                self.text_input.set("Error")
        elif char == 'M+':
            try:
                self.memory += float(self.text_input.get())
            except:
                pass
        elif char == 'M-':
            try:
                self.memory -= float(self.text_input.get())
            except:
                pass
        elif char == 'MR':
            self.text_input.set(self.memory)
            self.operand1 = self.memory
            self.reset_next = True
        elif char == 'MC':
            self.memory = 0

    def calculate(self, op1, op2, operator):
        try:
            if operator == '+':
                return op1 + op2
            elif operator == '-':
                return op1 - op2
            elif operator == '*':
                return op1 * op2
            elif operator == '/':
                return op1 / op2 if op2 != 0 else "Error"
        except:
            return "Error"

root = Tk()
calc = Calculator(root)
root.mainloop()