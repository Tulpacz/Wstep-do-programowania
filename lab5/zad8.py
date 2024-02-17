import math

def pole_trojkata_ostrokatnego(a, b, kat):
    if a == 0 or b == 0 or kat == 0:
        print("Trójkąt o podanych długościach boków i kącie nie istnieje.")
        return False
    if kat >= 90:
        print("Trójkąt nie jest ostrokątny.")
        return False

    pole = 0.5 * a * b * math.sin(math.radians(kat))
    return pole


a = float(input("Podaj długość boku a: "))
b = float(input("Podaj długość boku b: "))
kat = float(input("Podaj szerokość kąta ostrego w stopniach: "))


if pole_trojkata_ostrokatnego(a, b, kat):
    pole = pole_trojkata_ostrokatnego(a, b, kat)
    print("Pole trójkąta ostrokątnego wynosi:", pole)

