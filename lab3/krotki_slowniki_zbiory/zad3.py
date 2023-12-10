rachunki={"wrzesien":50, "październik": 65, "listopad":57, "grudzień":72}
print(rachunki)
rachunki
print(sum(rachunki.values()))
print(max(rachunki.values()))
print(min(rachunki.values()))

print(sum(rachunki.values())/ len(rachunki))
avg=sum(rachunki.values())/ len(rachunki)
klucze=list(rachunki.keys())
print(klucze[-1])
ostatni=rachunki["grudzień"]
print(ostatni)

if ostatni > avg:
    print("Zacznij oszczędzać")
else:
    print("Jesteś bezpieczny")