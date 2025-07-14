while True:
    my_kontakt = {}
    k = 0
    print("1 + контакт\n2 пошук\n3 видалити")
    komanda = input("ваша команда: ")
    if komanda == "1":
        k = input("додавай: ")
        d = input("тепер номер: ")
    my_kontakt[k] = d
    elif komanda == "2":
        k = input("назва контакта: ")
        b = my_kontakt.get(k)
    else:
        k = input("що видалити: ")
        del my_kontakt[k]