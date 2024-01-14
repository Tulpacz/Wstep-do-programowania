#pole trapezu (a+b)*h/2

bok1 = int(input("Podaj długość pierwszego boku: "))
bok2 = int(input("Podaj długość drugiego boku: "))
wysokosc = int(input("Podaj wysokosc trapezu: "))



def PoleTrapezu(bok1,bok2,wysokosc):
    return (int((bok1+bok2)*wysokosc/2))

print(PoleTrapezu(bok1,bok2,wysokosc))
