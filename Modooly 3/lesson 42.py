import tkinter as tk
root = tk.Tk()
root.title("Awto Clicker")
root.geometry("315x280")
root.resizable(False, False)
root.config(bg="#989EDB")

label = tk.Label(root, text="Awto Clicker", bg="#989EDB", fg="#3D41DC", font=("Arial", 30))
label.grid(pady=25, column=1)

label2 = tk.Label(root, font=("Arial", 15), fg="#3D41DC", bg="#989EDB", text="Кліків на секунду:")
label2.grid(row=2,column=1)

Entry = tk.Entry(root, font=("Arial", 15))
Entry.grid(pady=10,column=1, row=3)

Button = tk.Button(text="почати", bg="#12DC17")
Button.grid(row=4, column=0)

Button = tk.Button(text="вийти", bg="#DB0F00")
Button.grid(row=4, column=2)

root.mainloop()