import time
import os
czas = int(input("Podaj czas w sekundach: "))


while czas > 0:
    os.system("cls")
    print(f"Pozostało {czas} sekund")
    time.sleep(1)
    czas -= 1
print("Czas minął")



