import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def show_city_with_the_biggest_pollution(df: pd.DataFrame) -> tuple[str, float]: #funkcja zwraca krotkę z nazwą miasta i wartością zanieczyszczenia
    '''Ta funkcja zwraca miasto o największym zanieczyszczeniu powietrza'''
    max_pollution = df["AQI"].max() #najwyższy poziom zanieczyszczenia
    max_pollution_index = df["AQI"].idxmax() #indeks wiersza, w którym znajduje się najwyższe zanieczyszczenie
    city_max_pollution = df.iloc[max_pollution_index, 1] #miasto, w którym  jest największe zanieczyszczenie, gdzie: iloc[wiersz, kolumna]
    return (city_max_pollution, max_pollution)

def show_city_with_the_smallest_pollution(df: pd.DataFrame) -> tuple[str, float]:
    '''Ta funkcja zwraca miasto o najmniejszym zanieczyszczeniu powietrza'''
    min_pollution = df["AQI"].min() #najniższy poziom zanieczyszczenia
    min_pollution_index = df["AQI"].idxmin() #indeks najniższego poziomu zanieczyszczenia
    city_min_pollution = df.iloc[min_pollution_index, 1] #nazwa miasta o najnizszym zanieczyszczeniu
    return (city_min_pollution, min_pollution)

def statistics(df: pd.DataFrame) -> tuple[float]:
    '''Ta funkcja zwraca podstawowe statystyki dla AQI'''
    aqi = pd.to_numeric(df["AQI"], errors="coerce")
    mean_poll = aqi.mean()
    std_poll = aqi.std()
    var_poll = aqi.var()
    mean_poll = round(mean_poll, 4) #zaokrąglenie wartości do czterech miejsc po przecinku
    std_poll = round(std_poll, 4)
    var_poll = round(var_poll, 4)
    return (mean_poll, std_poll, var_poll)

def bar_plot_of_aqi_in_cities(df: pd.DataFrame) -> matplotlib.figure.Figure:
    '''Ta funkcja wyświetla wykres kolumnowy pokazujący ogólny poziom zanieczyszczenia w każdym mieście'''
    city = df["Miasto"].tolist() #przekształcenie kolumny z nazwami miast w listę
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

def barh_plot_tempetarure(df: pd.DataFrame) -> matplotlib.figure.Figure:
    '''Ta funkcja wyświetla wykres słupkowy porównujący temperaturę'''
    cities = df["Miasto"].tolist() #konwersja kolumny do listy
    temp = df["Temperatura"].tolist()
    fig, ax = plt.subplots()
    plt.barh(cities, temp, color="#63ACC3")
    plt.title("Temperatura")
    plt.xlabel("\u00B0C") #kod \u00B0 to symbol stopnia
    plt.ylabel("Miasto") 
    return fig

def barh_plot_humidity(df: pd.DataFrame) -> matplotlib.figure.Figure:
    '''Ta funkcja rysuje wykres słupkowy porównujący wilgotność powietrza'''
    cities = df["Miasto"].tolist() #konwersja kolumny do listy
    hum = df["Wilgotność"].tolist()
    fig, ax = plt.subplots()
    plt.barh(cities, hum, color="#B387DA")
    plt.title("Wilgotność")
    plt.xlabel("%")
    plt.ylabel("Miasto")
    return fig

def barh_plot_wind(df: pd.DataFrame) -> matplotlib.figure.Figure:
    '''Ta funkcja rysuje wykres słupkowy porównujący prędkość wiatru'''
    cities = df["Miasto"].tolist() 
    wind = df["Wiatr"].tolist()
    fig, ax = plt.subplots()
    plt.barh(cities, wind, color="#D4E730")
    plt.title("Prędkość wiatru")
    plt.xlabel("m/s")
    plt.ylabel("Miasto")
    return fig

def barh_plot_press(df: pd.DataFrame) -> matplotlib.figure.Figure:
    '''Ta funkcja rysuje wykres słupkowy porównujący ciśnienie atmosferyczbe'''
    cities = df["Miasto"].tolist() 
    press = df["Ciśnienie"].tolist()
    fig, ax = plt.subplots()
    plt.barh(cities, press, color="#F361C0")
    plt.title("Ciśnienie atmosferyczne")
    plt.xlabel("hPa")
    plt.ylabel("Miasto")
    return fig


