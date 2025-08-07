def save(content, echo = True):
    with open("istoria", "a", encoding="UTF-8") as fp:
        fp.write(f"{content}\n")

        return content


def open_histori():
    with open("istoria", "r", encoding="UTF-8") as fp:
        info = fp.read()
        return f"історія:\n, {info}, \n"

def rozbir(text, dowhuna = 5, zberhenny = True, f = False):
    pruholosni = ["б", "в", "г", "ґ", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч",
                  "ш", "щ", "ь"]
    holosni = ["а", "о", "у", "е", "и", "і", "я", "ю", "є", "ї"]
    text += " "
    prh = 0
    hol = 0
    prob = 0
    sumwol = 0
    inha_mowa = 0
    cufru = 0
    pos = 0
    start = 0
    sl = 0
    lit_5 = 0
    widpowid = ""
    if text == " ":
        print("ти нічого не написав")
        return False
    for i in text:
        if i.lower() in pruholosni:
            prh += 1
        elif i.lower() in holosni:
            hol += 1
        elif i == " " or i == "\n":
            prob += 1
            if pos != start:
                if pos - start >= int(dowhuna):
                    lit_5 += 1
                if zberhenny:
                    save(text[start:pos])
                    widpowid += text[start:pos]
                    widpowid += "\n"
                sl += 1
            start = pos + 1
        elif i == "`" or i == "~" or i == "<" or i == ">" or i == "." or i == "," or i == "?" or i == "!" or i == "(" or i == ")" or i == "/" or i == "\\" or i == "*" or i == "-" or i == "+":
            sumwol += 1
        elif i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" or i == "0":
            cufru += 1
        else:
            inha_mowa += 1
        pos += 1
    if f:
        widpowid += (
            f"слів: {sl}\n"
            f"приголосних: {prh}\n"
            f"голосних: {hol}\n"
            f"пробілів: {prob - 1}\n"
            f"символів: {sumwol}\n"
            f"символів і літер іншої мови: {inha_mowa}\n"
            f"цифр: {cufru}\n"
            f"слів в яких {dowhuna} і більше літер: {lit_5}"
        )
    else:
        widpowid += (
            f"слів: {sl}\n"
            f"приголосних: {prh}\n"
            f"голосних: {hol}\n"
            f"пробілів: {prob - 2}\n"
            f"символів: {sumwol}\n"
            f"символів і літер іншої мови: {inha_mowa}\n"
            f"цифр: {cufru}\n"
            f"слів в яких {dowhuna} і більше літер: {lit_5}"
        )
    return widpowid