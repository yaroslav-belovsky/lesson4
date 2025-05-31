correct_answers = 0
print("це тест на 12 питань різних категорій. В кінці буде кількісьть правильних відповідей. Удачі!")
respond = input("1. яка команда перевіряє чи виконалась якась умова?\nA)if; B)elif; C)else;\nнапиши літеру що стоїть перед правильною відповідю(A, B, C),\n")
if respond == "A":
    correct_answers = correct_answers+1
    print("правильно")
else:
    print("не правильно")
respond = input("2.Який найбільший океан у світі?\nA)Північний Льодовитий; B)Атлантичний; C)Тихий;\nнапиши літеру що стоїть перед правильною відповідю(A, B, C),\n")
if respond == "C":
    correct_answers = correct_answers + 1
    print("правильно")
else:
    print("не правильно")
respond = input("3.Скільки планет у Сонячній системі?\nA)2; B)8; C)10;\nнапиши літеру що стоїть перед правильною відповідю(A, B, C),\n")
if respond == "B":
    correct_answers = correct_answers + 1
    print("правильно")
else:
    print("не правильно")
respond = input("4.Яка компанія розробила операційну систему Windows?\nA)Apple; B)Google; C)Microsoft;\nнапиши літеру що стоїть перед правильною відповідю(A, B, C),\n")
if respond == "C":
    correct_answers = correct_answers + 1
    print("правильно")
else:
    print("не правильно")
respond = input("5.Який газ ми вдихаємо з повітрям для дихання?\nA)Вуглекислий газ; B)Азот; C)Кисень;\nнапиши літеру що стоїть перед правильною відповідю(A, B, C),\n")
if respond == "C":
    correct_answers = correct_answers + 1
    print("правильно")
else:
    print("не правильно")
respond = input("6.Яка планета найближча до Сонця?\nA)Земля; B)Марс; C)Меркурій;\nнапиши літеру що стоїть перед правильною відповідю(A, B, C),\n")
if respond == "C":
    correct_answers = correct_answers + 1
    print("правильно")
else:
    print("не правильно")
respond = input("7.Скільки відмінків в українській мові?\nA)5; B)6; C)7;\nнапиши літеру що стоїть перед правильною відповідю(A, B, C),\n")
if respond == "C":
    correct_answers = correct_answers + 1
    print("правильно")
else:
    print("не правильно")
respond = input("8.Яке з наведених слів є дієсловом?\nA)швидко; B)бігти; C)машина;\nнапиши літеру що стоїть перед правильною відповідю(A, B, C),\n")
if respond == "B":
    correct_answers = correct_answers + 1
    print("правильно")
else:
    print("не правильно")
respond = input("9.Який з наведених кутів є прямим?\nA)30°; B)60°; C)90°;\nнапиши літеру що стоїть перед правильною відповідю(A, B, C),\n")
if respond == "C":
    correct_answers = correct_answers + 1
    print("правильно")
else:
    print("не правильно")
respond = input("10.Скільки лап у павука?\nA)6; B)8; C)10;\nнапиши літеру що стоїть перед правильною відповідю(A, B, C),\n")
if respond == "B":
    correct_answers = correct_answers + 1
    print("правильно")
else:
    print("не правильно")
respond = input("11.Як називається орган, через який людина дихає?\nA)Серце; B)Легені; C)Шлунок;\nнапиши літеру що стоїть перед правильною відповідю(A, B, C),\n")
if respond == "B":
    correct_answers = correct_answers + 1
    print("правильно")
else:
    print("не правильно")
respond = input("12.Що таке Wi-Fi?\nA)Тип кабелю; B)Бездротове з’єднання з інтернетом; C)Додаток;\nнапиши літеру що стоїть перед правильною відповідю(A, B, C),\n")
if respond == "B":
    correct_answers = correct_answers + 1
    print("правильно")
else:
    print("не правильно")
print("дано",correct_answers,"правильних відповідей.")
if correct_answers == 12:
    print("Все правильно!")