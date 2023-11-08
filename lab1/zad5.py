liczba1 = float(input("Podaj liczbę x: "))
liczba2 = float(input("Podaj liczbę y: "))
liczba3 = float(input("Podaj liczbę z: "))


if (liczba3<liczba2):
    bufor=liczba3
    liczba3=liczba2
    liczba2=bufor

if (liczba2<liczba1):
    bufor=liczba2
    liczba2=liczba1
    liczba1=bufor

if (liczba3<liczba2):
    bufor=liczba3
    liczba3=liczba2
    liczba2=bufor

print(f"Uporządkowane liczby: 1) {liczba1} 2) {liczba2} 3) {liczba3}")