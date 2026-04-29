#W tym pliku znajdują się wszystkie funkcje dotyczące analizy danych, tj. rysowanie wykresów, wyświetlanie tabel itd.
#probny komenatrz
import pandas as pd
from tabulate import tabulate
import numpy as np
import matplotlib
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

def stacked_bar_plot_type_of_pollution(df: pd.DataFrame):
    '''Ta funkcja wyświetla wykres kolumnowy skumulowany porównujący zawartość pm2,5 i pm10 dla poszczególnych miast'''
    fig = px.bar(df, x = "Miasto", y = ["PM2,5 (Pył zawieszony drobny)", "PM10 (Pył zawieszony gruby)"], title="Rodzaje zanieczyszczeń")
    fig.update_yaxes(title="Zanieczyszczenie")
    fig.update_layout(legend_title_text="Rodzaje zanieczyszczeń")
    fig.show()

def pie_chart_of_air_composition_in_chosen_city(df: pd.DataFrame, city: str) -> matplotlib.figure.Figure:
    '''Ta funkcja rysuje wykres kołowy przedstawiający skład powietrza dla wybranego miasta'''
    chosen_city = df[df["Miasto"]==city] #wydzielenie tylko tego wiersza, który dotyczy wybranego miasta
    list_of_air_data = []
    names = ["Dwutlenek azotu", "Ozon", "Dwutlenek siarki", "Tlenek węgla"]
    for i in names:
        if not np.isnan(chosen_city[i].values[0]): #np.isnan sprawdza, czy dana wartość istnieje czy nie (is not a number)
            list_of_air_data.append(chosen_city[i].values[0]) #jeżeli wartość istnieje, to jest dodawana do listy
    if not len(list_of_air_data)==4: #sprawdzenie, czy lista zawiera wszystkie elementy, jeśli nie, to wyświetli się poniższy komunikat
        print("Brak wystarczających danych")
    else: #jeśli lista zawiera 4 wartości, to zostaną one wyświetlone na wykresie kołowym
        fig, ax = plt.subplots()
        plt.pie(list_of_air_data, labels=names, autopct='%1.1f%%') #autopct wyświetla stosunek procentowy danego składnika
        plt.title(f"Skład powietrza dla miasta {city}")
        return fig

def main():
    pie_chart_of_air_composition_in_chosen_city(df, "Warszawa")


if __name__ == "__main__":
    main()

