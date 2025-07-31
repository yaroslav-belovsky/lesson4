import tkinter as tk

# Початковий колір пензля
current_color = "black"

# --- Функції для зміни кольору ---
def change_color(color):
    global current_color
    current_color = color

# Малювання
def paint(event):
    x1, y1 = (event.x - 2), (event.y - 2)
    x2, y2 = (event.x + 2), (event.y + 2)
    canvas.create_oval(x1, y1, x2, y2, fill=current_color, outline=current_color)

# --- Головне вікно ---
root = tk.Tk()
root.title("Додаток художника")
root.geometry("600x500")

# Полотно для малювання
canvas = tk.Canvas(root, bg="white", width=600, height=450)
canvas.pack(fill=tk.BOTH, expand=True)

# Прив'язуємо подію малювання
canvas.bind("<B1-Motion>", paint)

# Меню вибору кольору
menubar = tk.Menu(root)
color_menu = tk.Menu(menubar, tearoff=0)

colors = {
    "Червоний": "red",
    "Синій": "blue",
    "Зелений": "green",
    "Жовтий": "yellow",
    "Фіолетовий": "purple",
    "Помаранчевий": "orange",
    "Чорний": "black"
}

for name, color in colors.items():
    color_menu.add_command(label=name, command=lambda c=color: change_color(c))

menubar.add_cascade(label="Вибір кольору", menu=color_menu)
root.config(menu=menubar)

root.mainloop()