def f(n):
    if n == 1 or n == 0:
        return 1
    else:
        return f(n-1)+f(n-2)

nr=int(input("Podaj liczbę ciągu którą chcesz uzyskać: "))
print(f(nr))