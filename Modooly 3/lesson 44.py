from tkinter import Tk, Label

def on_click(event):
    print(event)
    label.config(text="Мене натиснули")

root = Tk()
label = Label(root, text="Натисни мене", bg="lightblue")
label.pack(padx=20, pady=20)

label.bind("<Button-1>", on_click)

root.mainloop()