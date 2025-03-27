"""
Flott! Da kan vi lage et program som viser hvordan mengden av en radioaktiv isotop reduseres over tid, og gjør dette i form av en graf.

Vi kan bruke biblioteket matplotlib for å lage grafen. Vi trenger også numpy for å enklere håndtere matematiske beregninger. Har du disse bibliotekene installert på datamaskinen din? Hvis ikke, kan vi gå gjennom hvordan du installerer dem.

La oss gå videre til "M" (Make) og lage et grunnleggende Python-program som modellerer halveringstiden og tegner grafen.
"""

import numpy as np
import matplotlib.pyplot as plt

# Definerer halveringstiden og initialmengden
halveringstid = 5  # Halveringstiden i år
initial_mengde = 100  # Startmengden av isotopen

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