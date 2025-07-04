import librori_to_final_proekt as l

try:

    while True:

        menu = int(input("1: історія;     2: розбір речення з консолі     3: пошук слів заданої довжини з консолі     4:розібрати файл\n"))
        if menu == 1:
            l.open_histori()
            continue
        if menu == 2:
            text = str(input("напиши текст українською: ") + ' ')
            l.save(text, False)

            l.save(l.rozbir(text))
        if menu == 3:
            text = str(input("напиши текст українською: ") + ' ')
            l.save(text, False)

            dowhuna = int(input("напиши довжину слів для пошуку: "))
            l.save(f"довжина для пошуку: {dowhuna}", False)

            l.save(l.rozbir(text, dowhuna))
        if menu == 4:
            nazwa_faila = str(input("напиши назву файлу: "))
            with open(nazwa_faila, "r", encoding="UTF-8") as fp:
                info = fp.read()
                print(info)
                print(l.rozbir(info + " ",5))
except ValueError as error:
    print("це не число")
except FileNotFoundError as error:
    print("файл не знайдено")


