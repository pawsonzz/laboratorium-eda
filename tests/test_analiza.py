import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
from analiza import (
    wyczysc_dane,
    podsumowanie,
    sprzedaz_wg_kanalu,
)


def test_czyszczenie():
    df = pd.DataFrame({
        "kanal": [
            "Internet ",
            "SKLEP"
        ],
        "wartosc": [100, 200]
    })
    
    wynik = wyczysc_dane(df)
    assert list(wynik["kanal"]) == [
        "internet", "sklep"
    ]


def test_czyszczenie_nie_modyfikuje_wejscia():
    df = pd.DataFrame({"kanal": ["Internet "], "wartosc": [1]})
    wyczysc_dane(df)
    assert df["kanal"][0] == "Internet "


def test_podsumowanie():
    df = pd.DataFrame({
        "wartosc": [100, 200, 300]
    })
    wynik = podsumowanie(df)
    assert wynik["liczba"] == 3
    assert wynik["suma"] == 600
    assert wynik["srednia"] == 200
    assert wynik["mediana"] == 200


def test_sprzedaz_wg_kanalu():
    df = pd.DataFrame({
        "kanal": ["internet", "sklep", "internet"],
        "wartosc": [100, 50, 20],
    })
    wynik = sprzedaz_wg_kanalu(df)
    assert list(wynik.columns) == ["kanal", "suma_sprzedazy"]
    assert wynik.set_index("kanal")["suma_sprzedazy"].to_dict() == {
        "internet": 120,
        "sklep": 50,
    }
