import kalkulator as k
while True:
    widpowid = input("дія: ")
    if widpowid == "+":
        a = float(input("число 1: "))
        b = float(input("число 2: "))
        print("відповідь:", k.plus(a, b))
    elif widpowid == "-":
        a = float(input("число 1: "))
        b = float(input("число 2: "))
        print("відповідь:", k.minus(a, b))
    elif widpowid == "*":
        a = float(input("число 1: "))
        b = float(input("число 2: "))
        print("відповідь:", k.mult(a, b))
    elif widpowid == "/":
        a = float(input("число 1: "))
        b = float(input("число 2: "))
        print("відповідь:", k.div(a, b))
    else:
        print("ти не те написав")

