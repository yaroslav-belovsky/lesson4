import customtkinter as ctk

BTC_TO_UAH = 2000000 # Наприклад, 1 BTC = 110 0000 UAH
ETH_TO_UAH = 112000 # Наприклад, 1 ETH = 112 000 UAH
USDT_TO_UAH = 38 # Наприклад, 1 USDT = 38 UAH

def convert():
    zn = entry_amount.get
    from_var = from_currency_var.get
    to_var = to_currency_var.get

    if From == "BTC":
        BTC_1 = True
        if To == "BTC":
            result_label.config(text="так не можна!")

        if To == "ETH":
            result_label.config(text=BTC_TO_UAH / ETH_TO_UAH * zn)

        if To == "USDT":
            result_label.config(text=BTC_TO_UAH / USDT_TO_UAH * zn)

        if To == "UAH":
            result_label.config(text=zn * BTC_TO_UAH)


    if From == "ETH":
        if To == "BTC":
            BTC_2 = False
            result_label.config(text=BTC_TO_UAH / ETH_TO_UAH * zn)

        if To == "ETH":
            result_label.config(text="так не можна!")

        if To == "USDT":
            result_label.config(text=ETH_TO_UAH / USDT_TO_UAH * zn)

        if To == "UAH":
            result_label.config(text=zn * ETH_TO_UAH)


    if From == "USDT":
        if To == "BTC":
            BTC_2 = False
            result_label.config(text=BTC_TO_UAH / USDT_TO_UAH * zn)

        if To == "ETH":
            result_label.config(text=ETH_TO_UAH / USDT_TO_UAH * zn)

        if To == "USDT":
            result_label.config(text="так не можна!")

        if To == "UAH":
            result_label.config(text=zn * USDT_TO_UAH)


    if From == "UAH":
        if To == "BTC":
            BTC_2 = False
            result_label.config(text=zn * BTC_TO_UAH)

        if To == "ETH":
            result_label.config(text=zn * ETH_TO_UAH)

        if To == "USDT":
            result_label.config(text=zn * USDT_TO_UAH)

        if To == "UAH":
            result_label.config(text="так не можна!")






# Налаштування вікна
app = ctk.CTk()
app.title("Конвертер криптовалют")
app.geometry("400x300")

# Заголовок
title_label = ctk.CTkLabel(app, text="Конвертер криптовалют", font=("Roboto", 18))
title_label.pack(pady=10)

# Поле для вводу суми
entry_amount = ctk.CTkEntry(app, placeholder_text="Введи суму")
entry_amount.pack(pady=10)

# Вибір валюти для конвертації з
from_currency_var = ctk.StringVar(value="BTC")
from_currency_menu = ctk.CTkOptionMenu(app, variable=from_currency_var, values=["BTC", "ETH", "USDT", "UAH"])
from_currency_menu.pack(pady=5)

# Вибір валюти для конвертації в
to_currency_var = ctk.StringVar(value="UAH")
to_currency_menu = ctk.CTkOptionMenu(app, variable=to_currency_var, values=["BTC", "ETH", "USDT", "UAH"])
to_currency_menu.pack(pady=5)

# Кнопка конвертації
convert_button = ctk.CTkButton(app, text="Конвертувати", command=convert)
convert_button.pack(pady=10)

# Результат конвертації
result_label = ctk.CTkLabel(app, text="Результат")
result_label.pack(pady=10)

# Запуск програми
app.mainloop()