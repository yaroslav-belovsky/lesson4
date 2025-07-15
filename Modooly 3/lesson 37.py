from tkinter import Tk, Label, Button

# Створення головного вікна
root = Tk()
root.title("Практика з grid")
root.configure(bg="white")

# Додавання міток
Label(root, text="Текст 1", bg="lightgreen", font=14, padx=20, pady=10).grid(row=0, column=0)
Label(root, text="Текст 2", bg="lightblue", font=14, padx=20, pady=10).grid(row=0, column=1)
Label(root, text="Текст 3", bg="salmon", font=14, padx=20, pady=10).grid(row=1, column=0, columnspan=1)

# Додавання кнопок
Button(root, text="Кнопка 1", bg="orange", fg="white", font=14, width=15).grid(row=2,column=0)
Button(root, text="Кнопка 2", bg="blue", fg="white", font=14, width=15).grid(row=2,column=1)

# Запуск головного циклу
root.mainloop()