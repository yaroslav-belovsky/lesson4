import tkinter as tk

# Це буде функція для обробки натискання кнопок(поки що вона порожня):
def on_button_click(button):

    pass


# Функція для зміни теми:
def set_theme(theme):

    if theme == "light":

        root.config(bg='white')

        display.config(bg='lightgray', fg='black')

    elif theme == "dark":

        root.config(bg='black')

        display.config(bg='gray', fg='white')

    elif theme == "red":

        root.config(bg='red')

        display.config(bg='red4', fg='gray1')

    elif theme == "blue":

        root.config(bg='blue')

        display.config(bg='blue4', fg='gray')

    for button in buttons:

        button.config(bg='lightgray' if theme == "light" else 'darkgray' if theme == "dark"  else 'red4' if theme == "red" else 'lightblue', fg='black' if theme != "dark" else 'white')

# Головне вікно
root = tk.Tk()
root.title("Калькулятор")
root.geometry("390x370")
root.resizable(False, False)

display = tk.Entry(root, font=('Arial', 24), justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Кнопки калькулятора
buttons = []
button_texts = [

    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'

]

row_val = 1
col_val = 0

# Створюємо кнопки:
for text in button_texts:

    button = tk.Button(root, text=text, font=('Arial', 18), width=5, height=2, command=lambda text=text: on_button_click(text))
    button.grid(row=row_val, column=col_val)
    buttons.append(button)
    col_val += 1
    if col_val > 3:

        col_val = 0
        row_val += 1

# МЕНЮ
menubar = tk.Menu(root)
theme_menu = tk.Menu(menubar, tearoff=0)
theme_menu.add_command(label="Світла тема", command=lambda: set_theme("light"))
theme_menu.add_command(label="Темна тема", command=lambda: set_theme("dark"))
theme_menu.add_command(label="червона тема", command=lambda: set_theme("red"))
theme_menu.add_command(label="синя тема", command=lambda: set_theme("blue"))
menubar.add_cascade(label="налаштування теми", menu=theme_menu)
root.config(menu=menubar)

root.mainloop()