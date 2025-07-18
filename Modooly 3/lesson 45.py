import tkinter as tk
import random as r
def change_background_color(event):
    colors = ["#FF5733", "#33FF57", "#3357FF", "#F0E68C", "#FF33A1"]
    root.config(bg=r.choice(colors))
root = tk.Tk()
label = tk.Label(text="натисни пробіл і буде магія")
label.pack()
root.bind('<space>', change_background_color)
root.mainloop()