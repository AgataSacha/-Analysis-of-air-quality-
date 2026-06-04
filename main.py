import pandas as pd
import customtkinter as ctk

import start
from tworzenie_csv import choose_country, download_country_data
from okno_wybor import ctkAppChoice
from okno_porownanie import ctkAppCompare
from okno_miasto import ctkAppCity

start_window = start.starting_window() #wyświetlenie pierwszego okna, w którym użytkownik wybiera z listy rozwijalnej kraj, który go interesuje
cities = choose_country(start_window.country) #utworzenie listy miast w wybranym kraju
download_country_data(cities) #pobranie danych poprzez API, zapisanie ich w pliku csv
df = pd.read_csv("jakosc_powietrza.csv") #odczytanie pliku csv
df = df.dropna(axis=1, how='all') #usinięcie pustych wartości

ctk.set_appearance_mode("dark") #ustawienie ciemnego trybu dla wyświetlanego okna
root = ctk.CTk() #stworzenie głównego okna 
root.withdraw()  #ukrycie głównego okna 

def show_choice():
    '''Wyświetlenie głównego okna, w którym użytkownik wybiera, co chce dalej wyświetlić'''
    ctkAppChoice(root, on_choice) 

def on_choice(next_window):
    '''Wyświetlenie okna wybranego przez użytkownika'''
    if next_window == "compare":
        ctkAppCompare(root, df, cities, on_compare_close) 
    elif next_window == "city":
        ctkAppCity(root, df, cities, on_city_close)
    else:
        root.quit()

def on_compare_close(go_back):
    '''Jeśli użytkownik wcisnął przycisk "Cofnij", cofnięcie się do głównego okna, jeśli nie, zamknięcie wszystkich okien'''
    if go_back:
        show_choice()
    else:
        root.quit()

def on_city_close(go_back):
    '''Jeśli użytkownik wcisnął przycisk "Cofnij", cofnięcie się do głównego okna, jeśli nie, zamknięcie wszystkich okien'''
    if go_back:
        show_choice()
    else:
        root.quit()

show_choice()
root.mainloop()