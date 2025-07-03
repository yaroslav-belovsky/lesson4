while True:
    wubir = int(input("натисни: 1: показати всі справи;\n         2:додати нову справу;\n         3:очистити всі справи;\n         4:вийти з програми;\n         5:видалити рядок за номером;\n"))
    if wubir == 1:
        with open("sprawu", "r", encoding="UTF-8") as fp:
            info = fp.read()
            print(info)
    if wubir == 2:
        with open("sprawu", "a", encoding="UTF-8") as fp:
            widpowid = input("яку справу додати: ")
            fp.write(f"{widpowid}\n")
    if wubir == 3:
        with open("sprawu", "w") as fp:
            print("папа справи :)")

    if wubir == 4:
        break
    if wubir == 5:
        with open("sprawu", "r", encoding="UTF-8") as fp:
            info = fp.read()
            print(f"що з цьго видаляти?\n\n{info}")
            wubir = int(input("який рядок видалити? напиши цифру того який хочеш видалити: "))

        with open("sprawu", "r", encoding="UTF-8") as fp:
            sprawu = fp.readlines()
            wudalutu = sprawu[wubir]


        with open("sprawu", "w") as fp:
            sprawu.remove(wudalutu)

        with open("sprawu", "a", encoding="UTF-8") as fw:
            s = ""
            for i in sprawu:
                s += i + "\n"
            fw.write(s)

