import tkinter as tk
from funkci_1 import info
import random as r

root = tk.Tk()

color = ["blue", "red", "yellow", "green", "white"]

root.title("My super program")
root.geometry("1800x900")
text = "I love Python"


label = tk.Label(root, text=text,
font=("Arial", 30), fg="blue", bg="yellow")
label.pack()

def change_color_label():
    label.config(bg=r.choice(color))

button = tk.Button(root, text="Push me", command=info)
button.pack()

button2 = tk.Button(root, text="Change color", command=change_color_label)
button2.pack()




root.mainloop()