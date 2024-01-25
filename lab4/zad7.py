def odwroc(tekst):
    if len(tekst) <= 1:
        return tekst
    else:
        return odwroc(tekst[1:]) + tekst[0]

tekst = input("Podaj tekst do odwrócenia: ")
odwrocony = odwroc(tekst)
print(f"Odwrócony tekst: {odwrocony}")
