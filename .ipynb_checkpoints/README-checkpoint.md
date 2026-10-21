# Analiza sprzedaży

Projekt wykonany w ramach laboratorium z eksploracji danych.

## Dane

Plik `data/sprzedaz.csv` zawiera 12 fikcyjnych zamówień (kolumny: `id`, `kanal`,
`segment`, `wartosc`). Wartość zamówienia podana jest w złotych. Kanały sprzedaży
(`internet`, `sklep`) były zapisane niespójnie (wielkość liter, zbędne spacje),
dlatego dane są czyszczone przed analizą.

## Wykonane analizy

- kontrola jakości danych (rozmiar, typy, braki, duplikaty, niespójności),
- ujednolicenie nazw kanałów,
- liczba zamówień, suma, średnia i mediana wartości,
- suma sprzedaży według kanału (tabela i wykres słupkowy),
- interaktywna aplikacja z filtrem kanału i pobieraniem przefiltrowanych danych.

## Technologie

Python, pandas, matplotlib, Jupyter, pytest, Streamlit, GitHub, Render

## Struktura projektu

```
app.py              aplikacja Streamlit
analiza.py          funkcje analizy
data/sprzedaz.csv   dane
notebooks/          notebook z eksploracją
tests/              testy pytest
render.yaml         konfiguracja wdrożenia
```

## Uruchomienie lokalne

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
pip install jupyterlab pytest

python -m pytest -q
streamlit run app.py
```

## Aplikacja

https://ADRES-APLIKACJI.onrender.com

## Wnioski

1. Kanał internetowy generuje większość sprzedaży: 1490 zł z 2250 zł (ok. 66%),
   a sklep 760 zł (ok. 34%).
2. Obydwa kanały mają po 6 zamówień, ale średnie zamówienie w internecie
   (ok. 248 zł) jest prawie dwa razy większe niż w sklepie (ok. 127 zł).
