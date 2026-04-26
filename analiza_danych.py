#W tym pliku znajdują się wszystkie funkcje dotyczące analizy danych, tj. rysowanie wykresów, wyświetlanie tabel itd.

import pandas as pd
from tabulate import tabulate
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px




df = pd.read_csv("jakosc_powietrza.csv") #zczytanie danych z pliku csv

def convert_data_to_lists(df): #na razie taki zapis
    time_of_measurement = df["Data i godzina pomiaru"].tolist()
    city = df["Miasto"].tolist()
    geo = df["Współrzędne geograficzne"].tolist()
    aqi = df["AQI"].tolist()
    main_pollution = df["Główne zanieczyszczenie"].tolist()
    small_dust = df["PM2,5 (Pył zawieszony drobny)"].tolist()
    big_dust = df["PM10 (Pył zawieszony gruby)"].tolist()
    no2 = df["Dwutlenek azotu"].tolist()
    ozone = df["Ozon"].tolist()
    so2 = df["Dwutlenek siarki"].tolist()
    co = df["Tlenek węgla"].tolist()
    temperature = df["Temperatura"].tolist()
    humidity = df["Wilgotność"].tolist()
    pressure = df["Ciśnienie"].tolist()
    wind = df["Wiatr"].tolist()


def show_table_in_console(df):
    '''Ta funkcja wyświetla pobrane dane w konsoli w formie tabeli'''
    print(tabulate(df))


def show_city_with_the_biggest_pollution(df):
    '''Ta funkcja zwraca miasto o największym zanieczyszczeniu powietrza'''
    max_pollution = df["AQI"].max() #najwyższy poziom zanieczyszczenia
    max_pollution_index = df["AQI"].idxmax() #indeks wiersza, w którym znajduje się najwyższe zanieczyszczenie
    city_max_pollution = df.iloc[max_pollution_index, 1] #miasto, w którym  jest największe zanieczyszczenie, gdzie: iloc[wiersz, kolumna]
    return city_max_pollution


def bar_plot_of_aqi_in_cities(city: list[str], aqi: list[int]):
    '''Ta funkcja wyświetla wykres kolumnowy pokazujący ogólny poziom zanieczyszczenia w każdym mieście'''
    plt.bar(city, aqi)
    plt.title("Ogólny poziom zanieczyszczenia")
    plt.xlabel("Miasto")
    plt.ylabel("AQI")
    plt.show()


def stacked_bar_plot_type_of_pollution(df):
    '''Ta funkcja wyświetla wykres kolumnowy skumulowany porównujący zawartość pm2,5 i pm10 dla poszczególnych miast'''
    fig = px.bar(df, x = "Miasto", y = ["PM2,5 (Pył zawieszony drobny)", "PM10 (Pył zawieszony gruby)"], title="Rodzaje zanieczyszczeń")
    fig.update_yaxes(title="Zanieczyszczenie")
    fig.update_layout(legend_title_text="Rodzaje zanieczyszczeń")
    fig.show()
    

def main():
    show_city_with_the_biggest_pollution(df)

if __name__ == "__main__":
    main()

