import math
a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))
c = float(input("Podaj współczynnik c: "))

delta = (b**2)-(4*a*c)
print(delta)
if (delta>0):
    x1=(-b + math.sqrt(delta))/(2*a)
    x2=(-b - math.sqrt(delta))/(2*a)
    print("Rozwiązania: "+str(x1)+" i "+str(x2))
elif(delta==0):
    x0=-b
    print(str(x0))
else:print("Równanie nie ma rozwiązań")
