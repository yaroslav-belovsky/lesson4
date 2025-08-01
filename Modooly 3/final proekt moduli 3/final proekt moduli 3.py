from turtledemo.penrose import start

import labrori_to_final_proekt_moduli_3 as l
import tkinter as tk
import customtkinter as ctk
def prewirka(theme):
    global entry2bg, entry2fg

    if theme == "light":

        root.config(bg='white')

        label.configure(bg='white')

        entry.config(bg='lightgray', fg='black')
        entry2bg = 'lightgray'
        entry2fg = 'black'

    elif theme == "dark":

        root.config(bg='black')

        label.configure(bg='black')

        entry.config(bg='gray', fg='white')
        entry2bg = 'gray'
        entry2fg = 'white'

    elif theme == "red":

        root.config(bg='red')

        label.configure(bg='red')

        entry.config(bg='red4', fg='gray1')
        entry2bg = 'red4'
        entry2fg = 'gray1'

    elif theme == "blue":

        root.config(bg='blue')

        label.configure(bg='blue')

        entry.config(bg='blue4', fg='gray')
        entry2bg = 'blue4'
        entry2fg = 'gray'

    elif theme == "istoria":
        try:
            l.open_histori()

        except ValueError as error:
            print("це не число")
        except FileNotFoundError as error:
            print("файл не знайдено")

    elif theme == "ros_re":
        try:
            global p_s_z_d, ros_fail, ros_re
            p_s_z_d = False
            ros_fail = False
            ros_re = True
            while ros_re:
                text = entry.get()
                text2 = entry2.get()
                if start:
                    label.configure(text=l.save(l.rozbir(text,text2)))
                    start = False



        except ValueError as error:
            print("це не число")
        except FileNotFoundError as error:
            print("файл не знайдено")

    elif theme == "ros_fail":
        try:
            with open("istoria", "r", encoding="UTF-8") as fp:
                info = fp.read()
                label.configure(text=l.save(l.rozbir(info)))


        except ValueError as error:
            print("це не число")
        except FileNotFoundError as error:
            print("файл не знайдено")
def click(poosk = True):
    global start
    start = poosk


root = ctk.CTk
root.geometry("390x440")

entry = ctk.CTkEntry(placeholder_text="введи речення:")
entry.pack()

entry2 = ctk.CTkEntry(placeholder_text="введи речення:")
entry2.pack()

label = ctk.CTkLabel(text="")
label.pack()

rozbir = ctk.CTkButton(text="розібрати!", command=click)
rozbir.pack()


menubar = tk.Menu(root)
theme_menu = tk.Menu(menubar, tearoff=0)
theme_menu.add_command(label="Світла тема", command=lambda: prewirka("light"))
theme_menu.add_command(label="Темна тема", command=lambda: prewirka("dark"))
theme_menu.add_command(label="червона тема", command=lambda: prewirka("red"))
theme_menu.add_command(label="синя тема", command=lambda: prewirka("blue"))
theme_menu.add_command(label="історія", command=lambda: prewirka("istoria"))
theme_menu.add_command(label="розбір речення", command=lambda: prewirka("ros_re"))
theme_menu.add_command(label="розібрати файл", command=lambda: prewirka("ros_fail"))
menubar.add_cascade(label="теми і режими", menu=theme_menu)
root.config(menu=menubar)

root.mainloop()