import matplotlib.pyplot as plt
import numpy as np

def mengde_etter_tid(startmengde, halveringstid, dager):
    halveringer = dager / halveringstid
    gjenværende_mengde = startmengde * (0.5 ** halveringer)
    return gjenværende_mengde

while True:
    try:
        startmengde = float(input("Skriv inn startmengde jod-131 i mikrogram (må være > 0): "))
        halveringstid = float(input("Skriv inn halveringstid i dager (må være > 0): "))
        maks_dager = float(input("Skriv inn maks antall dager for grafen (må være ≥ 0): "))
        
        if startmengde <= 0 or halveringstid <= 0 or maks_dager < 0:
            print("Vennligst oppgi gyldige verdier.")
            continue

        break

    except ValueError:
        print("Ugyldig inndata, vennligst skriv inn tall.")

# Lag 200 datapunkter jevnt fordelt mellom 0 og maks_dager
dager_liste = np.linspace(0, maks_dager, num=200)
mengde_liste = [mengde_etter_tid(startmengde, halveringstid, d) for d in dager_liste]

# Plot grafen
plt.plot(dager_liste, mengde_liste)
plt.title("Mengde jod-131 over tid")
plt.xlabel("Dager")
plt.ylabel("Mengde (mikrogram)")
plt.grid()
plt.show()

# Kall funksjonen og skriv ut resultatet for dagen valgt
resultat = mengde_etter_tid(startmengde, halveringstid, maks_dager)
print(f"Etter {maks_dager} dager er det igjen {resultat:.2f} mikrogram jod-131.")