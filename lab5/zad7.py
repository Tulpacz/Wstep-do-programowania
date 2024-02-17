import random
poczatek = int(input("Podaj początek przedziału: "))
koniec = int(input("Podaj koniec przedziału: "))



krotka = tuple((random.randint(poczatek,koniec)) for _ in range(10))

def srednia(krotka):
    iloczyn=1
    for i in krotka:
        iloczyn*=i
    return iloczyn**(1/ len(krotka))

print(krotka)
print(srednia(krotka))
