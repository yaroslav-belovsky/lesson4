try:
    gruwni = float(input("Введи суму в гривнях: "))
    valuta = str(input("Вибери валюту (EUR/USD): "))
    if valuta == "EUR":
        print(f"{gruwni} гривень - {49, 24 * gruwni}євро")
    if valuta == "USD":
        print(f"{gruwni} гривень - {41, 76 * gruwni}Долар")
except ValueError as error:
    print("це не число")
except ZeroDivisionError:
    print("на нуль длити не можна")