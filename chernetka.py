import tkinter as tk

def get_text():
    content = text_area.get("1.0", tk.END)
    print(content)

root = tk.Tk()
root.title("Ввід тексту")

text_area = tk.Text(root, height=10, width=30)
text_area.pack()

get_button = tk.Button(root, text="Отримати текст", command=get_text)
get_button.pack()

root.mainloop()