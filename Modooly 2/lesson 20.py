fruits = ["apple", "banana", "kiwi", "orange", "watermelon"]

fruits.append("lemon")
fruits.append("lemon")
fruits.append("lemon")
print(fruits)

fruits[1] = "carrot"
print(fruits)

fruits.remove("orange")
print(fruits)

print(fruits[len(fruits)//2])
print(fruits.count("lemon"))