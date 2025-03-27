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
        start_mengde = float(start_mengde_entry.get())
        total_tid = float(total_tid_entry.get())
        
        halveringstid_graf(start_mengde, halveringstid, total_tid)
    except ValueError:
        print("Vennligst sjekk at alle verdier er riktig angitt.")

# Opprett Tkinter-vindu
root = Tk()
root.title("Halveringstid Graf")

# Liste over isotoper og deres halveringstider (i tidsenheter)
isotoper = {
    "Karbon-14": 5730,
    "Uran-238": 445800000,
    "Radon-222": 3.8,
    "Tritium": 12.3,
    "Cesium-137": 30.1
}

# Nedtrekksliste for isotoper
isotop_var = StringVar(root)
isotop_var.set(list(isotoper.keys())[0])  # Standardvalg
isotop_dropdown = OptionMenu(root, isotop_var, *isotoper.keys())
isotop_dropdown.pack()

# Inputfelt for startmengde
start_mengde_label = Label(root, text="Startmengde:")
start_mengde_label.pack()
start_mengde_entry = Entry(root)
start_mengde_entry.pack()

# Inputfelt for total tid
total_tid_label = Label(root, text="Total tid:")
total_tid_label.pack()
total_tid_entry = Entry(root)
total_tid_entry.pack()

# Knappe for å vise grafen
vis_graf_knapp = Button(root, text="Vis graf", command=vis_graf)
vis_graf_knapp.pack()

# Kjør hovedsløyfen
root.mainloop()