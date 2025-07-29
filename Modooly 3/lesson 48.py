import customtkinter as ctk

BTC_TO_UAH = float(2000000) # Наприклад, 1 BTC = 110 0000 UAH
ETH_TO_UAH = float(112000) # Наприклад, 1 ETH = 112 000 UAH
USDT_TO_UAH = float(38) # Наприклад, 1 USDT = 38 UAH
EURO_TO_UAH = float(49)
USD_TO_UAH = float(41.77)

def convert():
    try:
        zn = float(entry_amount.get())
        from_value = from_currency_var.get()
        to_value = to_currency_var.get()
        result = ""

        if from_value == "BTC":
            if to_value == "BTC":
                result = BTC_TO_UAH / BTC_TO_UAH * zn

            if to_value == "ETH":
                result = BTC_TO_UAH / ETH_TO_UAH * zn

            if to_value == "USDT":
                result = BTC_TO_UAH / USDT_TO_UAH * zn

            if to_value == "UAH":
                result = zn * BTC_TO_UAH

            if to_value == "EURO":
                result = BTC_TO_UAH / EURO_TO_UAH * zn

            if to_value == "USD":
                result = BTC_TO_UAH / USD_TO_UAH * zn


        if from_value == "ETH":
            if to_value == "BTC":
                result = BTC_TO_UAH / ETH_TO_UAH * zn

            if to_value == "ETH":
                result = ETH_TO_UAH / ETH_TO_UAH * zn

            if to_value == "USDT":
                result = ETH_TO_UAH / USDT_TO_UAH * zn

            if to_value == "UAH":
                result = zn * ETH_TO_UAH

            if to_value == "EURO":
                result = ETH_TO_UAH / EURO_TO_UAH * zn

            if to_value == "USD":
                result = ETH_TO_UAH / USD_TO_UAH * zn


        if from_value == "USDT":
            if to_value == "BTC":
                result = BTC_TO_UAH / USDT_TO_UAH * zn

            if to_value == "ETH":
                result = ETH_TO_UAH / USDT_TO_UAH * zn

            if to_value == "USDT":
                result = USDT_TO_UAH / USDT_TO_UAH * zn

            if to_value == "UAH":
                result = zn * USDT_TO_UAH

            if to_value == "EURO":
                result = EURO_TO_UAH / USDT_TO_UAH * zn

            if to_value == "USD":
                result = USD_TO_UAH / USDT_TO_UAH * zn


        if from_value == "UAH":
            if to_value == "BTC":
                result = zn * BTC_TO_UAH

            if to_value == "ETH":
                result = zn * ETH_TO_UAH

            if to_value == "USDT":
                result = zn * USDT_TO_UAH

            if to_value == "UAH":
                result = zn * 1

            if to_value == "EURO":
                result = EURO_TO_UAH * zn

            if to_value == "USD":
                result = USD_TO_UAH * zn

        if from_value == "EURO":
            if to_value == "BTC":
                result = BTC_TO_UAH / EURO_TO_UAH * zn

            if to_value == "ETH":
                result = ETH_TO_UAH / EURO_TO_UAH * zn

            if to_value == "USDT":
                result = EURO_TO_UAH / USDT_TO_UAH * zn

            if to_value == "UAH":
                result = EURO_TO_UAH * zn

            if to_value == "EURO":
                result = EURO_TO_UAH / EURO_TO_UAH * zn

            if to_value == "USD":
                result = EURO_TO_UAH / USD_TO_UAH * zn


        if from_value == "USD":
            if to_value == "BTC":
                result = BTC_TO_UAH / USD_TO_UAH * zn

            if to_value == "ETH":
                result = ETH_TO_UAH / USD_TO_UAH * zn

            if to_value == "USDT":
                result = USD_TO_UAH / USDT_TO_UAH * zn

            if to_value == "UAH":
                result = USD_TO_UAH * zn

            if to_value == "EURO":
                result = EURO_TO_UAH / USD_TO_UAH * zn

            if to_value == "USD":
                result = USD_TO_UAH / USD_TO_UAH * zn


        result_label.configure(text=f"{zn} {from_value} = {result} {to_value}")
    except ValueError:
        result_label.configure(text="це не число!")





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
from_currency_menu = ctk.CTkOptionMenu(app, variable=from_currency_var, values=["BTC", "ETH", "USDT", "UAH", "EURO", "USD"])
from_currency_menu.pack(pady=5)

# Вибір валюти для конвертації в
to_currency_var = ctk.StringVar(value="UAH")
to_currency_menu = ctk.CTkOptionMenu(app, variable=to_currency_var, values=["BTC", "ETH", "USDT", "UAH", "EURO", "USD"])
to_currency_menu.pack(pady=5)

# Кнопка конвертації
convert_button = ctk.CTkButton(app, text="Конвертувати", command=convert)
convert_button.pack(pady=10)

# Результат конвертації
result_label = ctk.CTkLabel(app, text="Результат")
result_label.pack(pady=10)


# Запуск програми
app.mainloop()