print("Jaką operację chcesz wykonać? \n 1)dodawanie \n 2)odejmowanie \n 3)mnożenie \n 4)dzielenie \n 5)potęgowanie")
operacja = int(input("Podaj numer operacji: "))
arg1 = float(input("Wpisz pierwszy argument: "))
arg2 = float(input("Wpisz drugi argument: "))

match(operacja):
    case 1:
        print("Wynik: "+str(arg1+arg2))
    case 2:
        print("Wynik: " + str(arg1-arg2))
    case 3:
        print("Wynik: "+str(arg1*arg2))
    case 4:
        print("Wynik: " + str(arg1/arg2))
    case 5:
        print("Wynik: " + str(arg1**arg2))