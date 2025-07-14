from faker import Faker

fake = Faker("uk")
print(fake.name())
print(fake.address())
print(fake.text())

print(fake.email())
print()
print(fake.credit_card_full())