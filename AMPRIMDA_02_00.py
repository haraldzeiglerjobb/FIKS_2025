# Funksjon for å beregne mengden radioaktivt stoff igjen etter en viss tid
def mengde_etter_tid(startmengde, halveringstid, dager):
    """
    Beregner hvor mye av et radioaktivt stoff som er igjen etter et bestemt antall dager.
    
    :param startmengde: Initial mengde av jod-131
    :param halveringstid: Halveringstiden til jod-131 (i dager)
    :param dager: Antall dager som har gått
    :return: Mengden av jod-131 som er igjen
    """
    # Beregn antall halveringer som har skjedd
    halveringer = dager / halveringstid
    # Beregn den gjenværende mengden
    gjenværende_mengde = startmengde * (0.5 ** halveringer)
    return gjenværende_mengde

# Eksempel på bruk
startmengde = 1000  # Startmengde i mikrogram
halveringstid = 8   # Halveringstid i dager
dager = 16          # Antall dager som har gått

# Kall funksjonen og skriv ut resultatet
resultat = mengde_etter_tid(startmengde, halveringstid, dager)
print(f"Etter {dager} dager er det igjen {resultat:.2f} mikrogram jod-131.")