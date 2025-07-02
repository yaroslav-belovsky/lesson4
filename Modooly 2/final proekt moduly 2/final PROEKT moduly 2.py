pruholosni = ["б", "в", "г", "ґ", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ"]
holosni = ["а", "о", "у", "е", "и", "і", "я", "ю", "є", "ї"]
while True:
    prh = 0
    hol = 0
    prob = 0
    sumwol = 0
    inha_mowa = 0
    cufru = 0
    pos = 0
    start = 0
    sl = 0
    lit = 0
    lit_5 = 0
    text = str(input("1:історія\nнапиши текст українською: ") + ' ')
    with open("istoria", "a", encoding="UTF-8") as fp:
        fp.write(f"{text}\n")
    if text == "1":
        with open("istoria", "r", encoding="UTF-8") as fp:
            info = fp.read()
            print("історія:")
            print(info, "\n")
            continue
    if text == " ":
        print("ти нічого не написав")
        continue
    for i in text:
        if i.lower() in pruholosni:
            prh += 1
            lit += 1
        elif i.lower() in holosni:
            hol += 1
            lit += 1
        elif i == " ":
            prob += 1
            if pos != start:
                if lit >= 5:
                    lit_5 += 1
                    lit = 0
                print(text[start:pos])
                with open("istoria", "a", encoding="UTF-8") as fp:
                    fp.write(f"{text[start:pos]}\n")
                sl += 1
            start = pos + 1
        elif i == "`" or i == "~" or i == "<" or i == ">" or i == "." or i == "," or i == "?" or i == "!" or i == "(" or i == ")" or i == "/" or i == "\\" or i == "*" or i == "-" or i == "+":
            sumwol += 1
        elif i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" or i == "0":
            cufru += 1
        else:
            inha_mowa += 1
        pos += 1
    print(f"слів: {sl}")
    print(f"приголосниг: {prh}")
    print(f"голосних: {hol}")
    print(f"пробілів: {prob}")
    print(f"символів: {sumwol}")
    print(f"символів і літер іншої мови: {inha_mowa}")
    print(f"цифр: {cufru}")
    print(f"слів в яких 5 і більше літер: {lit_5}")
    with open("istoria", "a", encoding="UTF-8") as fp:
        fp.write(str(f"слів: {sl}\n"))
        fp.write(str(f"приголосниг: {prh}\n"))
        fp.write(str(f"голосних: {hol}\n"))
        fp.write(str(f"пробілів: {prob}\n"))
        fp.write(str(f"символів: {sumwol}\n"))
        fp.write(str(f"символів і літер іншої мови: {inha_mowa}\n"))
        fp.write(str(f"цифр: {cufru}\n"))




