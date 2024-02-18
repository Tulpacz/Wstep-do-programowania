import datetime as dt

rok = int(input("Podaj rok: "))
miesiac = int(input("Podaj miesiąc: "))
dzien = int(input("Podaj dzień: "))

data = dt.date(rok, miesiac, dzien)

dzienRoku = data.timetuple().tm_yday
print(f"a. Dzień roku: {dzienRoku}")

numerTygodnia = data.isocalendar()[1]
print(f"b. Numer tygodnia: {numerTygodnia}")

dataPrzed = data - dt.timedelta(weeks=2)
dataPo = data + dt.timedelta(weeks=2)
print(f"c. Daty na 2 tygodnie przed i po: {dataPrzed} - {dataPo}")

dniDoNiedzieli = (6 - data.weekday() + 7) % 7
najblizszaNiedziela = data + dt.timedelta(days=dniDoNiedzieli)
print(f"d. Najbliższa niedziela: {najblizszaNiedziela}")

czasUnixowy = int((dt.datetime.combine(data, dt.datetime.now().time()) - dt.datetime(1970, 1, 1)).total_seconds())
print(f"e. Czas unixowy bieżącej godziny: {czasUnixowy}")
