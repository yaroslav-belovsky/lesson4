answer1 = input("input yor namber1")
answer2 = input("input yor namber2")
try:
    result = int(answer1) / int(answer2)
    print(result)
except ValueError as error:
    print("це не число")