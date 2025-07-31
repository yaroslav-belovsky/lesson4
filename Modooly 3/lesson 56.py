fruits = ["orange", "banan", "kiwi", "apple", "watermelon", "basturma"]


def select_b(fruit):
    return fruit.startswith("b")

def len_biggest_four(fruit):
    if len(fruit) >= 4:
        return True
    return False

filtred_fruits = list(filter(select_b, fruits))
filtred_fruits2 = list(filter(len_biggest_four, fruits))

print(filtred_fruits)
print(filtred_fruits2)