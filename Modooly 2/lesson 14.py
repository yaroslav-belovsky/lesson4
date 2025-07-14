import random as r
card = ["❤️", "♦️", "♣️", "♠️", "⭐"]
card_copy = ["❤️", "♦️", "♣️", "♠️", "⭐"]
s = 0
while True:
    r.shuffle(card_copy)
    s = s + 1
    print(card_copy)
    if card_copy == card:
        break

print(s)
