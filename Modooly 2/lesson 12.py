import random as r

print(r.random())
print(r.randint(1, 100))
name = ["A", "B", "C", "D"]
print(r.choice(name))
r.shuffle(name)
print(name)