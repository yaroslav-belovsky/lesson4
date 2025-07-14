for i in range(0, 1000, 2):
    print(i * 2)

fruits = ["яблуко", "банан", "груша", "кавун"]
my_dict = {"name": "Alice",
           "age": 10,
           "city": "Wonderland"}
name = "Kostya"

for fruit in fruits:
    print(fruit.upper())

for char in name:
    print(char)
for key in my_dict:
    print(my_dict.get(key))
for key, value in my_dict.items():
    print(f"[{key} -->]")