def potega(l,w):
    if w==0:
        return 1
    else:
        return l * potega(l, w-1)

liczba = int(input("Podaj liczbę do potęgowania: "))
wykladnik = int(input("Podaj wykładnik liczby: "))

wynik = potega(liczba, wykladnik)
print(f"{liczba}^{wykladnik} = {wynik}")
