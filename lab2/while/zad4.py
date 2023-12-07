#zadanie4
a=int(input("Podaj pierwszą liczbę: "))
b=int(input("Podaj drugą liczbę: "))

if a<b:
    while a<=b:
        if a%2!=0:
            a+=1
            continue
        print(a)
        a+=1

elif a==b:
    print("Liczby są równe, nie ma co liczyć")

else:
    while b<=a:
        if b%2!=0:
            b+=1
            continue
        print(b)
        b+=1