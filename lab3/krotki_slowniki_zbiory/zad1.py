import random
n = int(input("Podaj liczbę elementów tablicy: "))
x = int(input("Podaj maksymalną liczbę znaków w ciągu: "))

lista=[]
for i in range(n):
    dlugosc = random.randint(1,x)
    ciag = ""
    for j in range(dlugosc):
        ciag+=chr(97+random.randint(0,25))
    print(ciag)
    lista.append(ciag)
krotka = tuple(lista)

#a
suma = 0
for element in krotka:
    suma +=len(element)
print("Suma znaków: "+str(suma))
#b
suma_k = 0
for element in krotka:
    for c in element:
         if(c=="k"):
            suma_k+=1
print("Suma liter K : "+str(suma_k))
#c
suma_kt = 0
for element in krotka:
    suma_kt+=element.count("kt")
print("Suma ciągów KT : "+str(suma_kt))
#d
s = int(input("Policz ciągi dłuższe niż: "))
suma_dlozszych = 0
for element in krotka:
    if(len(element)>s):
        suma_dlozszych+=1
print("Liczba ciągów dłuższych niż "+str(s)+": "+str(suma_dlozszych))
