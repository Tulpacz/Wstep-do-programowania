wiek = int(input("Podaj wiek klienta: "))

if (wiek>18):cena=20
elif (wiek>=4):cena=10
elif (wiek>=0):cena=0
else:print("Wiek jest niepoprawny")

if (wiek>=0):print("Cena wynosi: "+str(cena))