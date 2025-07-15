import tkinter as tk
def f():
    name = Entry.get()
    label.config(text=f"Привіт {name}!")
root =tk.Tk()
root.geometry("1800x900")
root.title("вітання")
label = tk.Label(root, font=("Arial", 30), text="напиши ім'я і натисни привітатись, щоб я написав привітання", fg="blue", bg="yellow")
label.pack()
Entry = tk.Entry(root, font=("Arial", 30))
Entry.pack()
Button = tk.Button(root, text="Привітатись", command=f)
Button.pack()
root.mainloop()