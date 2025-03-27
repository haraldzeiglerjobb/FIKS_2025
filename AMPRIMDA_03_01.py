import numpy as np
import matplotlib.pyplot as plt
from tkinter import *

def halveringstid_graf(start_mengde, halveringstid, total_tid):
    tid = np.linspace(0, total_tid, 100)
    mengde = start_mengde * (0.5 ** (tid / halveringstid))

    plt.figure(figsize=(10, 6))
    plt.plot(tid, mengde, label='Mengde over tid', color='blue')
    plt.title('Utvikling av mengde over tid')
    plt.xlabel('Tid')
    plt.ylabel('Mengde')
    plt.axhline(y=0, color='k', linestyle='--')  
    plt.axvline(x=halveringstid, color='red', linestyle='--', label='Halveringstid')
    plt.legend()
    plt.grid()
    plt.show()

def vis_graf():
    try:
        valgt_isotop = isotop_var.get()
        halveringstid = isotoper[valgt_isotop]
        
        # Håndtere måleenheter
        mengde_enhet = mengde_enhet_var.get()
        tid_enhet = tid_enhet_var.get()

        # Konverteringer basert på valgte enheter
        if mengde_enhet == 'ug':
            start_mengde = float(start_mengde_entry.get())
        elif mengde_enhet == 'mg':
            start_mengde = float(start_mengde_entry.get()) / 1000
        elif mengde_enhet == 'g':
            start_mengde = float(start_mengde_entry.get())
        elif mengde_enhet == 'kg':
            start_mengde = float(start_mengde_entry.get()) * 1000
        elif mengde_enhet == 'tonn':
            start_mengde = float(start_mengde_entry.get()) * 1000000

        total_tid = float(total_tid_entry.get())

        # Konvertere total_tid til dager
        if tid_enhet == 'sekunder':
            total_tid /= 86400  # Antall sekunder i en dag
        elif tid_enhet == 'timer':
            total_tid /= 24  # Antall timer i en dag
        elif tid_enhet == 'år':
            total_tid *= 365  # Antall dager i et år

        halveringstid_graf(start_mengde, halveringstid, total_tid)
    except ValueError:
        print("Vennligst sjekk at alle verdier er riktig angitt.")

def oppdater_isotoper(*args):
    valgt_grunnstoff = grunnstoff_var.get()
    isotop_var.set("")  # Resett isotop-valg
    if valgt_grunnstoff == "Karbon":
        isotoper_dict = {
            "Karbon-14": 5730
        }
    elif valgt_grunnstoff == "Uran":
        isotoper_dict = {
            "Uran-238": 445800000,
            "Uran-235": 703800000
        }
    elif valgt_grunnstoff == "Radon":
        isotoper_dict = {
            "Radon-222": 3.8
        }
    elif valgt_grunnstoff == "Tritium":
        isotoper_dict = {
            "Tritium": 12.3
        }
    elif valgt_grunnstoff == "Cesium":
        isotoper_dict = {
            "Cesium-137": 30.1
        }
    
    isotoper.clear()
    isotoper.update(isotoper_dict)
    isotop_dropdown['menu'].delete(0, 'end')
    for isotop in isotoper.keys():
        isotop_dropdown['menu'].add_command(label=isotop, command=lambda value=isotop: isotop_var.set(value))

# Opprett Tkinter-vindu
root = Tk()
root.title("Halveringstid Graf")

# Grunnstoffer og isotoper
grunnstoffer = ["Karbon", "Uran", "Radon", "Tritium", "Cesium"]
isotoper = {}

# Nedtrekksliste for grunnstoffer
grunnstoff_var = StringVar(root)
grunnstoff_var.set(grunnstoffer[0])  # Standardvalg
grunnstoff_dropdown = OptionMenu(root, grunnstoff_var, *grunnstoffer, command=oppdater_isotoper)
grunnstoff_dropdown.pack()

# Nedtrekksliste for isotoper
isotop_var = StringVar(root)
isotop_dropdown = OptionMenu(root, isotop_var, "")
isotop_dropdown.pack()

# Inputfelt for startmengde
start_mengde_label = Label(root, text="Startmengde:")
start_mengde_label.pack()
start_mengde_entry = Entry(root)
start_mengde_entry.pack()

# Målenhet for mengde
mengde_enhet_var = StringVar(root)
mengde_enhet_var.set("g")  # Standardvalg
mengde_enhet_dropdown = OptionMenu(root, mengde_enhet_var, "ug", "mg", "g", "kg", "tonn")
mengde_enhet_dropdown.pack()

# Inputfelt for total tid
total_tid_label = Label(root, text="Total tid:")
total_tid_label.pack()
total_tid_entry = Entry(root)
total_tid_entry.pack()

# Målenhet for tid
tid_enhet_var = StringVar(root)
tid_enhet_var.set("dager")  # Standardvalg
tid_enhet_dropdown = OptionMenu(root, tid_enhet_var, "sekunder", "timer", "dager", "år")
tid_enhet_dropdown.pack()

# Knappe for å vise grafen
vis_graf_knapp = Button(root, text="Vis graf", command=vis_graf)
vis_graf_knapp.pack()

# Kjør hovedsløyfen
root.mainloop()