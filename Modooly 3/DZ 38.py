import tkinter as tk
import random as r

root = tk.Tk()

color = ["blue", "red", "yellow", "green", "brown4", "SlateBlue1", "yellow4", "SkyBlue1", "wheat1", "red2", "goldenrod", "cyan", "SlateBlue2", "snow"]

root.title("магічний екран ;)")
root.geometry("1800x900")

def color_BG():
    root.config(bg=r.choice(color))

button = tk.Button(root, text="магія", command=color_BG)
button.pack()

root.mainloop()