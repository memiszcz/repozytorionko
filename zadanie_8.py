import random

a=int(input("Podaj a: "))
b=int(input("Podaj b: "))

for i in range(6):
    print("Twoje losowe liczby z tego przedzialu: ",random.randint(a, b))

