import tkinter as tk
from tkinter import messagebox
import time
import keyboard
import mouse
running = False # змінна, що зберігатиме стан: програма зараз працює або ні
delay = 0 # змінна, що зберігатиме тривалість перерви після кожного кліку

def start_clicker():
    global running, delay # "знаходимо" змінні, що існують поза функцією
    try:
        info_label.config(text="")
        clicks_per_second = int(entry.get())
        delay = 1 / clicks_per_second # рахуємо затримку між кліками
        messagebox.showinfo("Auto Clicker", "Auto Clicker розпочинає роботу.")
        running = True
        schedule_click()
    except ValueError:
        print("Це не число!")
        info_label.config(text="Це не число!")




def schedule_click():

    sumv = 0
    while running:
        sumv += 1
        mouse.click()  # тут потім додамо клацання миші замість print
        Klik_label.config(text=f"Наклікано: {sumv}")
        root.update()
        print(f"Наклікано: {sumv}")
        time.sleep(delay)  # затримка між кліками



def exit_app():

   # тут буде завершення програми
   global running
   running = False
   messagebox.showinfo("Auto Clicker", "Auto Clicker зупинено.")
   root.destroy()  # Закриття вікна Tkinter

def key_i(event):
    messagebox.showinfo("info", "Це автоклікер, він буде клікати мишкою зі швидкістю, яку ти вкажеш!")


root = tk.Tk()
root.title("Auto Clicker")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
new_width = screen_width // 5
new_height = screen_height // 3
root.geometry(f"{new_width}x{new_height}")
root.configure(bg="#989EDB") # Light blue background
root.resizable(False, False)

# Label: назва
title_label = tk.Label(root, text="Auto Clicker", font=("Trebuchet MS", 16, "bold"), bg="#989EDB", fg="#3D41DC")
title_label.pack(pady=10) # Add some padding

# Label: кліки на секунду
label = tk.Label(root, text="Кліків на секунду:", font=("Trebuchet MS", 12), bg="#989EDB", fg="#3D41DC")
label.pack(pady=5)

# Entry для кількості кліків
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

# Frame, в якому будуть кнопки "почати" і "вийти"
button_frame = tk.Frame(root, bg="#989EDB")
button_frame.pack(side=tk.BOTTOM, pady=(20, 30)) # Increase padding from the bottom

Klik_label = tk.Label(root, text=f"Наклікано:", font=("Trebuchet MS", 16, "bold"), bg="#989EDB", fg="#3D41DC")
Klik_label.pack()


# Кнопка "Почати"
start_button = tk.Button(button_frame, text="Почати", command=start_clicker, bg="#4caf50", fg="white", font=("Trebuchet MS", 12))
start_button.grid(row=0, column=0, padx=10) # Add horizontal padding

# Кнопка "Вийти"
exit_button = tk.Button(button_frame, text="Вийти", command=exit_app, bg="#f44336", fg="white", font=("Trebuchet MS", 12))
exit_button.grid(row=0, column=1, padx=10)

info_label = tk.Label(root, text=f"", font=("Trebuchet MS", 16, "bold"), bg="#989EDB", fg="#3D41DC")
info_label.pack()

root.bind('i', key_i)# Add horizontal padding
keyboard.add_hotkey('delete', exit_app)



root.mainloop()