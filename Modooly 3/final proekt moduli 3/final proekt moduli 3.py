import labrori_to_final_proekt_moduli_3 as l
import tkinter as tk
import customtkinter as ctk

global start
start = False

def prewirka(theme):
    global entry2bg, entry2fg

    if theme == "light":
        theme_menu.config(bg="white", fg="black")

        root.config(bg='white')

        label.config(bg='white')

        rozbir.config(bg="white", fg="black")

        entry.config(bg='lightgray', fg='black')
        freim.config(bg='white')
        label_entry.config(bg='white', fg="black")
        entry2.config(bg='lightgray', fg='black')
        freim2.config(bg='white')
        label_entry2.config(bg='white', fg="black")

    elif theme == "dark":
        theme_menu.config(bg="black", fg="white")

        root.config(bg='black')

        label.config(bg='black')

        rozbir.config(bg="black", fg="white")

        entry.config(bg='gray', fg='white')
        freim.config(bg='black')
        label_entry.config(bg='black', fg="white")
        entry2.config(bg='gray', fg='white')
        freim2.config(bg='black')
        label_entry2.config(bg='black', fg="white")


    elif theme == "red":
        theme_menu.config(bg="red", fg="black")

        root.config(bg='red')

        label.config(bg='red')

        rozbir.config(bg="red4", fg="black")

        entry.config(bg='red4', fg='gray1')
        freim.config(bg='red')
        label_entry.config(bg='red', fg="black")
        entry2.config(bg='red4', fg='gray1')
        freim2.config(bg='red')
        label_entry2.config(bg='red', fg="black")


    elif theme == "blue":
        theme_menu.config(bg="blue", fg="black")

        root.config(bg='blue')

        label.config(bg='blue')

        rozbir.config(bg="blue", fg="black")

        entry.config(bg='blue4', fg='gray')
        freim.config(bg='blue')
        label_entry.config(bg='blue', fg="black")
        entry2.config(bg='blue4', fg='gray')
        freim2.config(bg='blue')
        label_entry2.config(bg='blue', fg="black")

    elif theme == "istoria":
        try:
            label.config(text=l.open_histori())

        except ValueError as error:
            print("це не число")
        except FileNotFoundError as error:
            print("файл не знайдено")

    elif theme == "ros_re":
        entry.pack()
        global ros_re, ros_fail
        entry.config(height=3)
        ros_fail = False
        label_entry.config(text="введи речення")
        label_entry2.pack()
        entry2.pack()
        label_entry2.config(text="введи кількість літер для пошуку(не обов'язково)")

        ros_re = True

    elif theme == "ros_fail":
        entry.pack()
        ros_re = False
        entry.config(height=1)
        label_entry.config(text="введи назву файлу який хочеш розібрати")
        label_entry2.pack_forget()
        entry2.pack_forget()

        ros_fail = True

def click():
    global ros_re, ros_fail
    if ros_re:
        try:
            text = entry.get("1.0", tk.END)
            text2 = entry2.get()
            if text2 == "":
                label.config(text=l.save(l.rozbir(text)))
            else:
                label.config(text=l.save(l.rozbir(text,text2)))
        except ValueError as error:
            label.config(text="це не число")
        except FileNotFoundError as error:
            label.config(text="файл не знайдено")

    elif ros_fail:
        try:
            text = entry.get("1.0", tk.END)
            text = text[:-1]


            with open(f"{text}", "r", encoding="UTF-8") as fp:
                info = fp.read()
                label.configure(text=l.rozbir(info, f=True))
        except ValueError as error:
            label.config(text="це не число")
        except FileNotFoundError as error:
            label.config(text="файл не знайдено")



root = ctk.CTk()
root.geometry("460x460")
root.config(bg="black")
root.title("розбір тексту")

freim = tk.Frame(root, bg="black")
freim.pack()

freim2 = tk.Frame(root, bg="black")
freim2.pack()

label_entry = tk.Label(freim, bg="black", fg='white', font=("Arial", 15))
label_entry.pack()

entry = tk.Text(freim, bg='gray', fg='white', font=("Arial", 15), height=3, width=30)
entry.pack()

label_entry2 = tk.Label(freim2, bg="black", fg='white', font=("Arial", 15))
label_entry2.pack()

entry2 = tk.Entry(freim2,bg='gray', fg='white', font=("Arial", 15))
entry2.pack()

label = tk.Label(root, text="", bg="black", fg='white', font=("Arial", 15))
label.pack()

rozbir = tk.Button(root, text="розібрати!", command=click, bg="grey6", fg="white", font=("Arial", 15))
rozbir.pack()

entry.pack_forget()
entry2.pack_forget()


menubar = tk.Menu(root)
theme_menu = tk.Menu(menubar, tearoff=0, bg="black", fg="white")
theme_menu.add_command(label="Світла тема", command=lambda: prewirka("light"))
theme_menu.add_command(label="Темна тема", command=lambda: prewirka("dark"))
theme_menu.add_command(label="Червона тема", command=lambda: prewirka("red"))
theme_menu.add_command(label="Синя тема", command=lambda: prewirka("blue"))
theme_menu2 = tk.Menu(menubar, tearoff=0, bg="black", fg="white")
theme_menu2.add_command(label="історія", command=lambda: prewirka("istoria"))
theme_menu2.add_command(label="режим розбір тексту", command=lambda: prewirka("ros_re"))
theme_menu2.add_command(label="режим розібрати файл", command=lambda: prewirka("ros_fail"))
menubar.add_cascade(label="теми", menu=theme_menu)
menubar.add_cascade(label="режими", menu=theme_menu2)
root.config(menu=menubar)

root.mainloop()