from datetime import datetime, timedelta

dataLaboratoriow = datetime(2024, 2, 4)
dzisiaj = datetime.now()
dataKolokwium = datetime(2024, 2, 11)

dniOdLaboratoriow = (dzisiaj - dataLaboratoriow).days
dniDoKolokwium = (dataKolokwium - dzisiaj).days

print(f"Od ostatnich laboratoriów minęło {dniOdLaboratoriow} dni.")
print(f"Do kolokwium pozostało {dniDoKolokwium} dni.")
