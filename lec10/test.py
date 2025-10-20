from tkinter import *
from tkinter import ttk
root = Tk()
frame = ttk.Frame(root, padding=50, borderwidth=30)
frame.grid()
ttk.Button(frame, text="Hello World").grid()
root.mainloop()