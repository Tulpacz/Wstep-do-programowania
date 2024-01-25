def obliczPole(a,b,c):
    # czy liczby sa dodatnie i rzeczywiste
    if a<=0 or b<=0 or c<=0:
        return("Błąd - liczby nie są dodatnie/rzeczywiste")

    # czy suma długości 2 krótszych boków jest wieksza od 3
    if a+b<=c or a+c<=b or b+c<=a:
        return("Błąd - wzajemne długości boków są niepoprawne")

    # wzor Herona
    polowaObwodu = (a + b + c)/2
    pole = (polowaObwodu * (polowaObwodu - a) * (polowaObwodu - b) * (polowaObwodu - c)) ** 0.5
    return pole

a = int(input("Podaj długość pierwszego bok trójkąta: "))
b = int(input("Podaj długość drugiego bok trójkąta: "))
c = int(input("Podaj długość trzeciego bok trójkąta: "))

print(f"Pole trójkąta o bokach {a}, {b}, {c}: {obliczPole(a,b,c)}")

