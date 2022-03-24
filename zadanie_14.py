import random

from numpy import infty

a=random.randint(1,50)
b=random.randint(1,50)
c=random.randint(1,50)
d=random.randint(1,50)
e=random.randint(1,50)
f=random.randint(1,50)

proby = []

print("Twoim zadaniem bedzie odgadniecie szesc liczb, ktore wylosowal program w przediale od 1 do 50.")

strzal1=int(input("Podaj pierwsza liczbe: "))

proby.append(strzal1)

strzal2=int(input("Podaj druga liczbe: "))

proby.append(strzal2)

strzal3=int(input("Podaj trzecialiczbe: "))

proby.append(strzal3)

strzal4=int(input("Podaj czwarta liczbe: "))

proby.append(strzal4)

strzal5=int(input("Podaj piata liczbe: "))

proby.append(strzal5)

strzal6=int(input("Podaj szosta liczbe: "))

proby.append(strzal6)

if strzal1 < 50 and strzal2<50 and strzal3<50 and strzal4 < 50 and strzal5<50 and strzal6<50:
   print("umiesz liczyc")
else:
    print("Zlamales zasady, tak sie nie bawimy. Nara!")