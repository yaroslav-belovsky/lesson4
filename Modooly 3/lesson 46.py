import tkinter as tk

root = tk.Tk()

# Отримуємо розміри екрана
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Розраховуємо нові розміри вікна
new_width = screen_width // 2 # Половина ширини екрану
new_height = screen_height # Вся висота екрану

# Задаємо нові розміри вікна
root.geometry(f"{new_width}x{new_height}")
label = tk.Label(root, text=f"{new_width}x{new_height}", font=("Arial", 50))
label.pack()
root.mainloop()