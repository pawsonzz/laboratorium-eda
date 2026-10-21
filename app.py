import streamlit as st
import pandas as pd
from analiza import (
    wczytaj_dane,
    wyczysc_dane,
    podsumowanie,
    sprzedaz_wg_kanalu
)

st.set_page_config(
    page_title="Analiza sprzedaży - projekt laboratoryjny",
    layout="wide"
)

st.title("Analiza sprzedaży – projekt laboratoryjny")

df = wczytaj_dane(
    "data/sprzedaz.csv"
)
df = wyczysc_dane(df)

st.sidebar.header("Filtry")

kanaly = sorted(
    df["kanal"].dropna().unique()
)

wybrane = st.sidebar.multiselect(
    "Kanał sprzedaży",
    kanaly,
    default=kanaly
)

df_filtr = df[
    df["kanal"].isin(wybrane)
]

wyniki = podsumowanie(df_filtr)

c1, c2, c3 = st.columns(3)

c1.metric(
    "Liczba zamówień",
    wyniki["liczba"]
)
c2.metric(
    "Suma sprzedaży",
    f'{wyniki["suma"]:.2f} zł'
)
c3.metric(
    "Średnia wartość",
    f'{wyniki["srednia"]:.2f} zł'
)

st.subheader("Sprzedaż według kanału")

tabela = sprzedaz_wg_kanalu(
    df_filtr
)

kol_tabela, kol_wykres = st.columns(2)

with kol_tabela:
    st.dataframe(tabela)

with kol_wykres:
    if not tabela.empty:
        kolory = {"internet": "#1f77b4", "sklep": "#ff7f0e"}

        fig, ax = plt.subplots(figsize=(5, 3.5))
        slupki = ax.bar(
            tabela["kanal"],
            tabela["suma_sprzedazy"],
            color=[kolory.get(k, "#888888") for k in tabela["kanal"]],
            width=0.5,
        )
        ax.bar_label(slupki, fmt="%d zł", padding=3)
        ax.set_ylim(0, tabela["suma_sprzedazy"].max() * 1.15)
        ax.set_ylabel("Suma sprzedaży [zł]")
        ax.set_xlabel("Kanał")
        ax.grid(axis="y", linestyle="--", alpha=0.4)
        ax.set_axisbelow(True)
        fig.tight_layout()
        st.pyplot(fig)

st.subheader("Dane po filtrowaniu")
st.dataframe(df_filtr)

csv = df_filtr.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    "Pobierz CSV",
    csv,
    "wyniki.csv",
    "text/csv"
)
