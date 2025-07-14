cod = input("напишіть текст: ")
pruholosni = ["б", "в", "г", "ґ", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ"]
holosni = ["а", "о", "у", "е", "и", "і"]
for i in cod:
    if i in pruholosni:
        cod = cod.replace(i,"0")
    elif i in holosni:
        cod = cod.replace(i,"1")
print(cod)
