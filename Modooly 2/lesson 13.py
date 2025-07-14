import random
print ("вгадай число від 1 до 100")
a = random.randint(1,100)
sprobu = 0
while True:
    answer = int(input("твоє число: "))
    if answer == a:
        print("Ви виграли!")
        print("за",sprobu,"спроб.")
        break
    elif answer < a:
        print("ні в мене чсло >")
    else:
        print("ні в мене чсло <")
    sprobu = sprobu + 1