import matplotlib.pyplot as plt
import numpy as np

# Funksjon for å beregne mengden radioaktivt stoff igjen etter en viss tid
def mengde_etter_tid(startmengde, halveringstid, dager):
    halveringer = dager / halveringstid
    gjenværende_mengde = startmengde * (0.5 ** halveringer)
    return gjenværende_mengde

# Interaktiv del
while True:
    try:
        startmengde = float(input("Skriv inn startmengde jod-131 i mikrogram (må være > 0): "))
        halveringstid = float(input("Skriv inn halveringstid i dager (må være > 0): "))
        dager = float(input("Skriv inn antall dager som har gått (må være >= 0): "))
        
        # Sjekk for fornuftige verdier
        if startmengde <= 0 or halveringstid <= 0 or dager < 0:
            print("Vennligst oppgi verdier som er større enn 0 for startmengde og halveringstid, og ≥ 0 for dager.")
            continue

        break  # Bryt ut av løkken dersom input er ok

    except ValueError:
        print("Ugyldig inndata, vennligst skriv inn tall.")

# Lag en liste for dager og mengde
dager_liste = np.arange(0, dager + 1)
mengde_liste = [mengde_etter_tid(startmengde, halveringstid, d) for d in dager_liste]

# Plot grafen
plt.plot(dager_liste, mengde_liste)
plt.title("Mengde jod-131 over tid")
plt.xlabel("Dager")
plt.ylabel("Mengde (mikrogram)")
plt.grid()
plt.show()

# Kall funksjonen og skriv ut resultatet for den angitte dagen
resultat = mengde_etter_tid(startmengde, halveringstid, dager)
print(f"Etter {dager} dager er det igjen {resultat:.2f} mikrogram jod-131.")