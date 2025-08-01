while True:
    try:
        a = input("введи число а ")
        b = input("введи число b ")
        if a == "вихід" or b == "вихід":
            break
        print(f"{a} + {b} = {eval(f"{a} + {b}")}")
    except NameError:
        print("не число!!!")