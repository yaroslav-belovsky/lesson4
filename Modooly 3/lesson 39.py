from tkinter import Tk, Label, Button

root = Tk()
root.title("GUI з Pack")

header = Label(root, text="Вітаємо у веселому GUI!", bg="lightblue", fg="white", font=("Arial", 20), padx=10, pady=10)
header.pack(side="top", fill="x")

instruction = Label(root, text="Я Верхній рядочок", bg="lime", fg="black", font=("Arial", 14), padx=20, pady=10)
instruction.pack(side="top", fill="x", padx=10, pady=10)

left_button = Button(root, text="Я Ліва кнопка", bg="orange", fg="white", font=("Arial", 12), padx=20, pady=10)
left_button.pack(side="left", fill="y", expand=True, padx=10, pady=10)

right_button = Button(root, text="Я Права кнопка", bg="purple", fg="white", font=("Arial", 12), padx=20, pady=10)
right_button.pack(side="right", fill="y", expand=True, padx=10, pady=10)

status = Label(root, text="А я Нижній рядок", bg="yellow", fg="black", font=("Arial", 12), padx=20, pady=10)
status.pack(side="bottom", fill="x")

root.mainloop()