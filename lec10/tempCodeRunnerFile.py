from tkinter import *
from tkinter import ttk

state = {
    "total_attempts": 6,
    "guessed_letters": set(),
    "word": "котка",
    "displayed_word": None
}
state["displayed_word"] = " ".join(["_" for _ in state["word"]])

def update_displayed_word():
    state["displayed_word"] = " ".join([letter if letter in state["guessed_letters"] else "_" for letter in state["word"]])
    label_word.config(text=state["displayed_word"])

def check_letter():
    letter = entry.get().lower()
    if len(letter) != 1 or not letter.isalpha():
        label_message.config(text="Моля, въведете една буква.")
        return
    if letter in state["guessed_letters"]:
        label_message.config(text="Вече сте познали тази буква.")
        return
    state["guessed_letters"].add(letter)
    if letter in state["word"]:
        update_displayed_word()
        label_message.config(text="Познахте буква!")
    else:
        state["total_attempts"] -= 1
        label_message.config(text="Грешна буква.")
        if state["total_attempts"] == 0:
            label_message.config(text=f"Загубихте! Думата беше: {state['word']}")
            button_check.config(state=DISABLED)
        else:
            label_attempts.config(text=f"Остават ви {state['total_attempts']} опита")
    entry.delete(0, END)
    if "_" not in state["displayed_word"]:
        label_message.config(text="Поздравления! Познахте думата!")
        button_check.config(state=DISABLED)

root = Tk()
ttk.Label(root, text="Познайте думата:").grid(row=0, column=0, padx=10, pady=10)
label_word = ttk.Label(root, text=state["displayed_word"], font=("Helvetica", 24))
label_word.grid(row=1, column=0, padx=10, pady=10)

ttk.Label(root, text="Въведете буква:").grid(row=2, column=0, padx=10, pady=5)
entry = ttk.Entry(root)
entry.grid(row=3, column=0, padx=10, pady=5)

button_check = ttk.Button(root, text="Провери буква", command=check_letter)
button_check.grid(row=4, column=0, padx=10, pady=10)

label_attempts = ttk.Label(root, text=f"Остават ви {state['total_attempts']} опита")
label_attempts.grid(row=5, column=0, padx=10, pady=5)
label_message = ttk.Label(root, text="")
label_message.grid(row=6, column=0, padx=10, pady=5)
root.mainloop()