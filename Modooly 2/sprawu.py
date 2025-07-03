from library_spraw import pokazatu_wmist
while True:
    wubir = int(input("натисни: 1: показати всі справи;\n         2:додати нову справу;\n         3:очистити всі справи;\n         4:вийти з програми;\n         5:видалити рядок за номером;\n"))
    if wubir == 1:
        pokazatu_wmist()
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
        print("Що з цього видаляти?")
        sprawu = pokazatu_wmist()
        wubir = int(input("який рядок видалити? напиши цифру того який хочеш видалити: "))-1

        wudalutu = sprawu[wubir]
        sprawu.remove(wudalutu)

        with open("sprawu", "w", encoding="UTF-8") as fw:
            s = ""
            for i in sprawu:
                s += i
            fw.write(s)

