import random
k = random.randint(0, 101)
r = 0
while True:
    i = int(input("число: "))
    if i > k:
        print("ні в тебе число бльше за моє")
    if i < k:
        print("ні в тебе число менше за моє")
    if i == k:
        break
    r += 1

print(f"ти вгадав! правильне число: {k}  ти вгадав за {r} спроб!")