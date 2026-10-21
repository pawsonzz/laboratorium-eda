import pandas as pd


def wczytaj_dane(sciezka):
    return pd.read_csv(
        sciezka,
        sep=";"
    )


def wyczysc_dane(df):
    wynik = df.copy()
    wynik["kanal"] = (
        wynik["kanal"].astype(str).str.strip().str.lower()
    )
    return wynik


def podsumowanie(df):
    wartosci = df["wartosc"]
    
    if wartosci.empty:
        return {
            "liczba": 0,
            "suma": 0.0,
            "srednia": 0.0,
            "mediana": 0.0,
        }
        
    return {
        "liczba": int(len(wartosci)), ## liczba zamowien
        "suma": float(wartosci.sum()), ## suma sprzedazy
        "srednia": float(wartosci.mean()), ## srednia wartosc
        "mediana": float(wartosci.median()), ## mediana
    }

    raise NotImplementedError


def sprzedaz_wg_kanalu(df):
    wynik = (
        df.groupby("kanal", as_index=False)["wartosc"].sum()
            .rename(columns={"wartosc": "suma_sprzedazy"})
    )
    
    return wynik

    raise NotImplementedError
