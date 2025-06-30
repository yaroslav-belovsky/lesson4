pruholosni = ["б", "в", "г", "ґ", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ"]
holosni = ["а", "о", "у", "е", "и", "і", "я"]
while True:
    prh = 0
    hol = 0
    prob = 0
    sumwol = 0
    inha_mowa = 0
    cufru = 0
    text = input("напиши текст украюнською: ")
    if text == "":
        print("ти нічого не написав")
        continue
    for i in text:
        if i.lower() in pruholosni:
            prh += 1
        elif i.lower() in holosni:
            hol += 1
        elif i == " ":
            prob += 1
        elif i == "`" or i == "~" or i == "<" or i == ">" or i == "." or i == "," or i == "?" or i == "!" or i == "(" or i == ")" or i == "/" or i == "\\" or i == "*" or i == "-" or i == "+":
            sumwol += 1
        elif i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" or i == "0":
            cufru += 1
        else:
            inha_mowa += 1
    sl = prob + 1
    print(f"слів: {sl}")
    print(f"приголосниг: {prh}")
    print(f"голосних: {hol}")
    print(f"пробілів: {prob}")
    print(f"символів: {sumwol}")
    print(f"символів і літер іншої мови: {inha_mowa}")
    print(f"цифр: {cufru}")



