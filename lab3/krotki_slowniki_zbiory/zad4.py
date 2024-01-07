import random
a = random.randint(3,7)
b = random.randint(3,7)
X = set()
Y = set()
for e in range(a):
    X.add(random.randint(0,10))
print(X)

for e in range(b):
    Y.add(random.randint(0,10))
print(Y)
#a
print("zbiór X zawiera liczbę 5: "+str(5 in X))
#b
print("zbiór X jest podzbiorem zbioru Y: "+str(X.issubset(Y)))
#c
print("zbiór Y jest podzbiorem zbioru X: "+str(Y.issubset(X)))
#d
print("zbiór X jest nadzbiorem zbioru Y: "+str(X.issuperset(Y)))
#e
print("zbiór Y jest nadzbiorem zbioru X: "+str(Y.issuperset(X)))
#f
print("Suma zbiorów X i Y: "+str(X.union(Y)))
#g
print("Różnica zbiorów X i Y: "+str(X.difference(Y)))
#h
print("Różnica zbiorów Y i X: "+str(Y.difference(X)))
#i
print("Iloczyn zbiorów X i Y: "+str(X.intersection(Y)))
#j
print("Różnica symetryczna zbiorów X i Y: "+str(X.symmetric_difference(Y)))
#k
print("Najwyższy element w obu zbiorach: "+str(max(X.union(Y))))
#l
lista_x = list(X)
lista_x.reverse()
Y.add(lista_x.pop())
X = set(lista_x)
#m
for x in X:
    Y.add(x)
#n
X.clear()
Y.clear()
