import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt


def oddziel(napis: str = '') -> None:
    """
    Ta funkcja po prostu robi ładną przerwę z wybranym wzorkiem XDD
    """
    print("\n"+napis*25+"\n")


# CZY JA TO MUSZĘ KOMENTOWAĆ?
global hal, sa, kub, default_od
default_od = '--'
hal = "Halszka Kościelska"
sa = "Sandra Mleczak"
kub = "Jakub Markil"

print(f"Autorzy:\n{hal},\n{kub},\n{sa}")

file = "LOL.csv"

dane = pd.read_csv(file)

# dane.info()
# oddziel(default_od)

kolumny = list(dane.columns)

indexes = list(dane.index)

role.to_csv("role.csv")
role = pd.read_csv("role.csv")

'''
dane.Mana.value_counts().to_csv("mana.csv")
zdrowie_stats = dane.Health.value_counts()
role_stats = dane.Primary_Role.value_counts()
armor_stats = dane.Armor.value_counts()
mr_stats = dane.Magic_Resistance.value_counts()
armor_stats.to_csv("armor.csv")
mr_stats.to_csv("mr.csv")
zdrowie_stats.to_csv("zdrowie_stats.csv")
print(role_stats)

print("DANE DOT. ZDROWIA BOHATERÓW\n")
print(zdrowie_stats)

oddziel()

print("SZCZEGÓŁOWE STATYSTYKI DANYCH O ZDROWIU BOHATERÓW\n")
print(dane.Health.describe())

oddziel()

global Health_value, length
Health_value = 630
'''

length = range(len(indexes))

# WYPISUJE WSZYSTKIE POSTACIE O DANEJ WARTOŚCI HP ORAZ ICH ROLE
"""
print(f"LISTA BOHATERÓW O {Health_value} PUNKTACH ZDROWIA ORAZ ICH ROLE\n")

for i in length:
    if dane["Health"][i] == Health_value:
        print(f"{dane[kolumny[1]][i]}, {dane[kolumny[2]][i]}")
"""

oddziel(default_od)

# NO TUTAJ RYSUJE WYKRESY JAKIEŚ GŁUPIE
"""
zdrowie = pd.read_csv("zdrowie_stats.csv")
plt.subplot(2,1,1)
plt.plot(zdrowie["zdrowie"], zdrowie["ilosc"], "." ,color = "#09d9a1")
plt.xlabel('Punkty zdrowia')
plt.ylabel('Ilość bohaterów')

plt.subplot(2,1,2)
plt.plot(role["Primary_Role"],role["amount"],"*",color="#5c09d9")
plt.xlabel('Rola')
plt.ylabel('Ilość bohaterów')
plt.ylim([0,45])
plt.tight_layout
plt.show()
"""


global srednie_hp, srednie_ar, srednie_mr, srednie_mana, srednie_manareg

# PĘTLA DO LICZENIA ŚREDNICH STATYSTYK KONKRETNYCH RÓL
def srednie(kategoria: str, prin: bool = False) -> list:
    srednie = np.zeros(len(role))
    for j in range(len(role)):
        suma, ilosc = 0, 0
        for i in length:
            if dane["Primary_Role"][i] == role["Primary_Role"][j]:
                suma += dane[kategoria][i]
                ilosc += 1
        srednia = round(suma/ilosc, 2)
        srednie[j] = srednia

    if prin:
        for i in range(len(role)):
            print(f'Ilość postaci roli {role["Primary_Role"][i]}: {role["amount"][i]}\nŚrednie statystyki {kategoria} dla roli {role["Primary_Role"][i]}: {srednie[i]}\n')

    return srednie


srednie_hp = srednie("Health", True)
oddziel(default_od)

# JAKIEŚ PRÓBY NA WARTOŚCI BOOL
"""
valid = np.zeros(len(dane["Mana"]))
x = 0
for i in dane["Mana"]:
    valid_val = i > 200
    valid[x] = valid_val
    x += 1
"""
