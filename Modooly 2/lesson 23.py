zavdannya = []
while True:
    print("menu")

    answer = int(input("число: 1: додати завдання, 2: видалити завдання, 3: Переглянути список завдань.      4: завершити\n"))
    if answer == 1:
        zavdannya.append(input("завдання: "))
    if answer == 2:
        zavdannya.remove(input("завдання: "))
    if answer == 3:
        for zavdannyas in zavdannya:
            print(zavdannyas)
        print("\n")
    if answer == 4:
        break


