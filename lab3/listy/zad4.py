
#a
imie = input("Podaj imię: ")
print("Witaj, "+imie)
#b
wiek = input("Podaj wiek: ")
print("Twój wiek to: "+wiek)

#c
imie = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")
print("Twoje inicjały to: "+imie[0].capitalize()+". "+nazwisko[0].capitalize()+". ")

#d
tekst = input("Wpisz tekst: ")
for i in range(5):
    print(tekst)

#e
pierwszy = input("Podaj pierwszy tekst: ")
drugi = input("Podaj drugi tekst: ")
polaczona = pierwszy+drugi
print(polaczona)

#f
pierwszy = input("Podaj pierwszy tekst: ")
drugi = input("Podaj drugi tekst: ")
polowa1 = pierwszy[ :int(len(pierwszy)/2)]
polowa2 = drugi[ int(len(drugi)/2):]
polowy = polowa1+polowa2
print(polowy)




