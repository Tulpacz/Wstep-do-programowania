import random

liczby =[]
for i in range(48):
    liczby.append(i+1)
wylosowane = random.sample(liczby,6)
print("Wylosowane liczby to: "+str(wylosowane))