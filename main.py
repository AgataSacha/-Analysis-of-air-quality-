import pandas as pd
import customtkinter as ctk

import start
from tworzenie_csv import choose_country, download_country_data
from okno_wybor import ctkAppChoice
from okno_porownanie import ctkAppCompare
from okno_miasto import ctkAppCity

start_window = start.starting_window()
cities = choose_country(start_window.country)
download_country_data(cities)
df = pd.read_csv("jakosc_powietrza.csv")
df = df.dropna(axis=1, how='all')

ctk.set_appearance_mode("dark")
root = ctk.CTk()
root.withdraw()  # ukryj główne okno — każdy widok będzie Toplevel

def show_choice():
    ctkAppChoice(root, cities, df, on_choice)

def on_choice(next_window):
    if next_window == "compare":
        ctkAppCompare(root, df, cities, on_compare_close)
    elif next_window == "city":
        ctkAppCity(root, df, cities, on_city_close)
    else:
        root.quit()

def on_compare_close(go_back):
    if go_back:
        show_choice()
    else:
        root.quit()

def on_city_close(go_back):
    if go_back:
        show_choice()
    else:
        root.quit()

show_choice()
root.mainloop()