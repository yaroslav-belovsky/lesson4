import tkinter as tk

def read():
    root.config(background="red")

def blue():
    root.config(background="blue")

def green():
    root.config(background="green")

def yellow():
    root.config(background="yellow")

def purple():
    root.config(background="purple")

def orange():
    root.config(background="orange")

# Створюємо головне вікно
root = tk.Tk()
root.title("Мій додаток")

# Створюємо меню
menubar = tk.Menu(root)

# Додаємо перший пункт меню
file_menu1 = tk.Menu(menubar, tearoff=0)
file_menu1.add_command(label="червоний", command=read)
file_menu1.add_command(label="синій", command=blue)
file_menu1.add_command(label="зелений", command=green)
file_menu1.add_command(label="жовтий", command=yellow)
file_menu1.add_command(label="фіолетовий", command=purple)
file_menu1.add_command(label="помаранчевий", command=orange)

# Додаємо два підменю в головне меню
menubar.add_cascade(label="вибір кольору", menu=file_menu1)

# Додаємо головне меню у вікно
root.config(menu=menubar)

root.mainloop()