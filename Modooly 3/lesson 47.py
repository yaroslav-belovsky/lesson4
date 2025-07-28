import customtkinter as ctk

def button_pressed():
    print("Кнопка натиснута!")

root = ctk.CTk()

root.title("Мій CustomTkinter додаток")

button = ctk.CTkButton(root, text="натисни мене!", command=button_pressed)
button.pack(pady=20)


root.mainloop()