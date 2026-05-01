#W tym pliku znajdują się wszystkie funkcje dotyczące analizy danych, tj. rysowanie wykresów, wyświetlanie tabel itd.
#probny komenatrz
import pandas as pd
from tabulate import tabulate
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv("jakosc_powietrza.csv") #zczytanie danych z pliku csv

def show_table_in_console(df: pd.DataFrame):
    '''Ta funkcja wyświetla pobrane dane w konsoli w formie tabeli'''
    print(tabulate(df))


def show_city_with_the_biggest_pollution(df: pd.DataFrame) -> tuple[str, float]:
    '''Ta funkcja zwraca miasto o największym zanieczyszczeniu powietrza'''
    max_pollution = df["AQI"].max() #najwyższy poziom zanieczyszczenia
    max_pollution_index = df["AQI"].idxmax() #indeks wiersza, w którym znajduje się najwyższe zanieczyszczenie
    city_max_pollution = df.iloc[max_pollution_index, 1] #miasto, w którym  jest największe zanieczyszczenie, gdzie: iloc[wiersz, kolumna]
    return (city_max_pollution, max_pollution)


def bar_plot_of_aqi_in_cities(df: pd.DataFrame) -> matplotlib.figure.Figure:
    '''Ta funkcja wyświetla wykres kolumnowy pokazujący ogólny poziom zanieczyszczenia w każdym mieście'''
    city = df["Miasto"].tolist()
    aqi = df["AQI"].tolist()
    fig, ax = plt.subplots()
    plt.bar(city, aqi)
    plt.title("Ogólny poziom zanieczyszczenia")
    plt.xlabel("Miasto")
    plt.ylabel("AQI")
    return fig


def stacked_bar_plot_type_of_pollution(df: pd.DataFrame) -> matplotlib.figure.Figure:
    '''Ta funkcja wyświetla wykres kolumnowy skumulowany porównujący zawartość pm2,5 i pm10 dla poszczególnych miast'''
    cities = df["Miasto"].tolist() #konwersja kolumny do listy
    pm25 = df["PM2,5 (Pył zawieszony drobny)"].tolist()
    pm10 = df["PM10 (Pył zawieszony gruby)"].tolist()
    x = np.arange(len(cities)) #lista, której długość jest równa liczbie miast
    width = 0.5
    fig, ax = plt.subplots()
    ax.bar(x, pm25, width, label="PM2,5 (Pył zawieszony drobny)")
    ax.bar(x, pm10, width, bottom=pm25, label="PM10 (Pył zawieszony gruby)")
    ax.set_title("Rodzaje zanieczyszczeń")
    ax.set_xlabel("Miasto")
    ax.set_ylabel("Zanieczyszczenie")
    ax.set_xticks(x) #znaczniki będą pod każdym słupkiem
    ax.set_xticklabels(cities, rotation=45, ha="right") #podpisy znaczników mają być nazwami miast
    ax.legend(title="Rodzaje zanieczyszczeń")
    fig.tight_layout() #automatyczne dopasowanie wszystkich elementów (w tym podpisów, żeby nie nachodziły na siebie)
    return fig


def main():
    stacked_bar_plot_type_of_pollution(df)


if __name__ == "__main__":
    main()

