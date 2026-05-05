import pandas as pd
from tabulate import tabulate
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv("jakosc_powietrza.csv") #zczytanie danych z pliku csv
df = df.dropna(axis=1, how='all') #usunięcie kolumn, w których nie ma żadnych danych

def pie_chart_of_air_composition_in_chosen_city(df: pd.DataFrame, city: str) -> matplotlib.figure.Figure:
    '''Ta funkcja rysuje wykres kołowy przedstawiający skład powietrza dla wybranego miasta'''
    chosen_city = df[df["Miasto"]==city] #wydzielenie tylko tego wiersza, który dotyczy wybranego miasta
    list_of_air_data = []
    names = ["Dwutlenek azotu", "Ozon", "Dwutlenek siarki", "Tlenek węgla"]
    names_to_use = []
    for i in names:
        if not np.isnan(chosen_city[i].values[0]): #np.isnan sprawdza, czy dana wartość istnieje czy nie (is not a number)
            list_of_air_data.append(chosen_city[i].values[0]) #jeżeli wartość istnieje, to jest dodawana do listy
            names_to_use.append(i) #jeżeli dana wartość jest dostępna, to jej nazwa musi pojawić się na wykresie, więc ta nazwa jest dodawana do listy nazw
    if not list_of_air_data: #sprawdzenie, czy lista zawiera jakieś elementy, jeśli nie, to wyświetli się poniższy komunikat
        print("Brak wystarczających danych")
        return None
    else: #jeśli lista zawiera jakieś wartości, to wyświetli się wykres kołowy
        fig, ax = plt.subplots()
        plt.pie(list_of_air_data, labels=names_to_use, autopct='%1.1f%%') #autopct wyświetla stosunek procentowy danego składnika
        plt.title(f"Skład powietrza dla miasta {city}")
    return fig




def main():
    pie_chart_of_air_composition_in_chosen_city(df, "Warszawa")


if __name__ == "__main__":
    main()