litera = str(input("Podaj jedną literę: "))

if(len(litera)==1):
    if(litera.isupper()):
        print("Litera jest duża")
    elif(litera.islower()):
        print("Litera jest mała")
else:print("Niepoprawna litera")
