#!/usr/bin/env python

#---------------KNIHOVNY--------------#
import pandas as pd

#---------------PROMĚNNÉ--------------#
soubor = "data.xlsx"

#---------------FUNKCE----------------#

def nacti_data(soubor):
    """Načte Excel soubor a vrátí DataFrame"""
    return pd.read_excel(soubor)

def vypis_celou_tabulku(df):
    """Vypíše celou tabulku"""
    print("=== Celá tabulka ===")
    print(df)

def vypis_radky(df):
    """Vypíše data po jednotlivých řádcích v přehledném formátu"""
    print("\n=== Data po řádcích ===")
    for index, row in df.iterrows():
        print(f"{row['Jméno']} ({row['Věk']} let) z {row['Město']}, Povolání: {row['Povolání']}")

def filtr_vek(df, min_vek):
    """Vrátí a vypíše lidi starší než zadaný věk"""
    vysledek = df[df['Věk'] > min_vek]
    print(f"\n=== Lidé starší než {min_vek} let ===")
    print(vysledek)
    return vysledek

def filtr_mesto(df, mesto):
    """Vrátí a vypíše lidi z konkrétního města"""
    vysledek = df[df['Město'] == mesto]
    print(f"\n=== Lidé z {mesto} ===")
    print(vysledek)
    return vysledek

#---------------MAIN------------------#

def main():
    df = nacti_data(soubor)
    vypis_celou_tabulku(df)
    vypis_radky(df)
    filtr_vek(df, 30)
    filtr_mesto(df, "Praha")

if __name__ == "__main__":
    main()

