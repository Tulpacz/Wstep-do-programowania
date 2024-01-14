def ObliczBMI(waga,wzrost):
    #0<wzr<3.0
    bmi = waga/wzrost**2
    print("Twoje BMI wynosi: ",bmi, sep="",end="")
    if bmi<18.5:
        print(" - masz niedowagę")
    elif bmi<25:
        print(" - w normie")
    elif bmi < 30:
        print(" - masz nadwagę")
    elif bmi < 35:
        print(" - masz otyłość I stopnia")
    elif bmi < 40:
        print(" - masz otyłość II stopnia")
    else:
        print(" - Niepoprawne dane")


    return bmi

waga = float(input("Podaj masę ciała w kilogramach: "))
wzrost = float(input("Podaj wzrost w metrach: "))
ObliczBMI(waga,wzrost)