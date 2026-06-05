import pandas as pd
import customtkinter as ctk

from window_first import starting_window
from create_csv import choose_country, download_country_data
from window_choosing import ctkAppChoice
from window_comparing_cities import ctkAppCompare
from window_chosen_city import ctkAppCity

start_window = starting_window() #wyświetlenie pierwszego okna, w którym użytkownik wybiera z listy rozwijalnej kraj, który go interesuje
cities = choose_country(start_window.country) #utworzenie listy miast w wybranym kraju
#download_country_data(cities) #pobranie danych poprzez API, zapisanie ich w pliku csv
df = pd.read_csv("jakosc_powietrza.csv") #odczytanie pliku csv

ctk.set_appearance_mode("dark") #ustawienie ciemnego trybu dla wyświetlanego okna
root = ctk.CTk() #stworzenie głównego okna 
root.withdraw()  #ukrycie głównego okna 

def show_choice() -> None:
    '''Wyświetlenie głównego okna, w którym użytkownik wybiera, co chce dalej wyświetlić'''
    ctkAppChoice(root, on_choice) 

def on_choice(next_window: str) -> None:
    '''Wyświetlenie okna wybranego przez użytkownika'''
    if next_window == "compare": 
        ctkAppCompare(root, df, cities, on_compare_close) 
    elif next_window == "city":
        ctkAppCity(root, df, cities, on_city_close)
    else:
        root.destroy()

def on_compare_close(go_back: bool) -> None:
    '''Jeśli użytkownik wcisnął przycisk "Cofnij", cofnięcie się do głównego okna, jeśli nie, zamknięcie wszystkich okien'''
    if go_back:
        show_choice()
    else:
        root.destroy()

def on_city_close(go_back: bool) -> None:
    '''Jeśli użytkownik wcisnął przycisk "Cofnij", cofnięcie się do głównego okna, jeśli nie, zamknięcie wszystkich okien'''
    if go_back:
        show_choice()
    else:
        root.destroy()

show_choice()
root.mainloop()
