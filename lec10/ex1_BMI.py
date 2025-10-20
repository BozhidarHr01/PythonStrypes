from tkinter import *
from tkinter import ttk

def calculate_bmi():
    try:
        height = float(entry_height.get()) / 100
        weight = float(entry_weight.get())
        if height <= 0 or weight <= 0:
            label_message.config(text="Моля, въведете валидни положителни числа.")
            label_result.config(text="BMI: ")
            return
    except Exception:
        label_message.config(text="Моля, въведете валидни положителни числа.")
        label_result.config(text="BMI: ")
        return

    bmi = weight / (height ** 2)
    meaning = ""
    if bmi < 18.5:
        meaning = "Недостатъчно тегло"
    elif 18.5 <= bmi < 25:
        meaning = "Нормално тегло"
    elif 25 <= bmi < 30:
        meaning = "Наднормено тегло"
    else:
        meaning = "Затлъстяване"
    label_result.config(text=f"BMI: {bmi:.2f} ({meaning})")
    label_message.config(text="")


root = Tk()

ttk.Label(root, text="Височина (сантиметри):").grid(row=0, column=0, padx=10, pady=5)
entry_height = ttk.Entry(root)
entry_height.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(root, text="Тегло (килограми):").grid(row=1, column=0, padx=10, pady=5)
entry_weight = ttk.Entry(root)
entry_weight.grid(row=1, column=1, padx=10, pady=5)

calculate = ttk.Button(root, text="Изчисли BMI", command=calculate_bmi)
calculate.grid(row=2, column=0, pady=10)

label_result = ttk.Label(root, text="BMI: ")
label_result.grid(row=3, column=0, pady=5)

label_message = ttk.Label(root, text="")
label_message.grid(row=4, column=0, pady=5)

root.mainloop()