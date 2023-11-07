import random
#droga = int(input("Podaj drogę w kilometrach: "))

droga=random.randint(1, 100000)

spalanie = int(input("Podal spalanie w l/100km: "))
zuzycie=droga*spalanie/100
koszt=zuzycie*6.5

print("Zużycie paliwa wyniesie: "+str(zuzycie))

print("Koszt podróży wyniesie:"+str(koszt))