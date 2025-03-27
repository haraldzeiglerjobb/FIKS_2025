"""
Det er en god idé! Vi kan gjøre koden slik at den ber brukeren om å angi halveringstid og initialmengde før grafen blir tegnet. På den måten kan du enkelt teste ulike verdier og se hvordan de påvirker grafen.

La oss oppdatere koden for å inkludere input fra brukeren:
"""



import numpy as np
import matplotlib.pyplot as plt

# Be om input fra brukeren
halveringstid = float(input("Skriv inn halveringstid (i år): "))  # Halveringstiden i år
initial_mengde = float(input("Skriv inn initialmengde av isotopen: "))  # Startmengden av isotopen

# Tidspunkter for observasjon (fra 0 til 30 år)
tid = np.linspace(0, 30, 100)

# Beregner mengden isotop over tid
mengde = initial_mengde * (0.5 ** (tid / halveringstid))

# Lager grafen
plt.plot(tid, mengde)
plt.title('Halveringstiden til en radioaktiv isotop')
plt.xlabel('Tid (år)')
plt.ylabel('Mengde isotop')
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.grid()
plt.show()