import random

def liczba():
    dolny = int(input("Podaj dolną granicę zakresu liczb: "))
    gorny = int(input("Podaj górną granicę zakresu liczb: "))
    liczba = random.randint(dolny,gorny)
    return [liczba, dolny,gorny]


liczbaProb = 0

lista = liczba()
if lista[2] - lista[1]<4:
    print("Zakres jest za mały")
    liczbaProb=99
liczba = lista[0]


while liczbaProb<3:
    propozycja = input(f"Zgadnij wylosowaną liczbę z przedziału: {lista[1]} - {lista[2]} : ")
    if str(propozycja).isdigit()==False:
        print("To nie liczba")
        break
    propozycja=int(propozycja)
    liczbaProb+=1
    if propozycja==liczba:
        print("Brawo! Odgadłeś liczbę!")
        break


    else:
        if liczbaProb <= 2:
            print(f"To nie ta liczba, spróbuj ponownie, masz jeszcze {3 - liczbaProb}  próby/a: ")
        if liczbaProb>2:
            print("Przegrałeś")
            break
        if propozycja>liczba:
            print("Liczba jest mniejsza od podanej")
        if propozycja<liczba:
            print("Liczba jest większa od podanej")
