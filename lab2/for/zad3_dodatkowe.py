liczbaGwiazdek = int(input("Podaj liczbę gwiazdek w linii: "))



for i in range(liczbaGwiazdek):
    print(" "*(liczbaGwiazdek-i), end=" ")
    print("* "*(i+1))

