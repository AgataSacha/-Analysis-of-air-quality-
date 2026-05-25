import customtkinter as ctk #biblioteka oparta na bibliotece tkinter, dzięki której wyświetlane okno lepiej wygląda
import pandas as pd

from okno_porownanie import ctkAppCompare
from okno_miasto import ctkAppCity
import start
from tworzenie_csv import choose_country, download_country_data

class ctkAppChoice:
    def __init__(self, cities, df):
        self.cities = cities
        self.df = df
        ctk.set_appearance_mode("dark")
        self.app = ctk.CTk() 
        self.app.title("Jakość powietrza") #nazwa wyświetlanego okna
        self.app.geometry(self.CenterWindowToDisplay(self.app, 700, 200, self.app._get_window_scaling())) #wymiary i położenie wyświetlanego okna
        self.app.resizable(False, False)
        self.app.update()

        self.textbox = ctk.CTkTextbox(master=self.app, width=636, height=85, text_color="#99CCFF", font=('Helvetica',19)) #pole tekstowe
        self.textbox.pack(padx=20, pady=20) #położenie pola tekstowego
        self.textbox.insert("0.0", "Co chcesz zrobić? Porównać poziom zanieczyszczenia dla największych miast w wybranym kraju, czy wyświetlić dane dla jednego z tych miast? Wciśnij odpowiedni przycisk.") #tekst
        self.textbox.tag_config("center", justify="center") #ta linijka i jedna poniżej odpowiadają za wyrównanie tekstu do środka
        self.textbox.tag_add("center", "1.0", "end")

        self.button1 = ctk.CTkButton(master=self.app, text="Porównanie miast",font=('Helvetica',15), command=lambda:[self.on_closing(), self.show_comparing_window()]) #po wciśnięciu przycisku zadziałają dwie funckcje, zamkknięcie tego okna i otwarcie nowego (dlatego musi być lambda)
        self.button1.place(relx=0.15, rely=0.7)

        self.button2 = ctk.CTkButton(master=self.app, text="Dane dla wybranego miasta",font=('Helvetica',15), command=lambda:[self.on_closing(), self.show_city_window()])
        self.button2.place(relx=0.6, rely=0.7)

        self.app.protocol("WM_DELETE_WINDOW", self.on_closing) #po ręcznym zamknięciu okna zadziała funkcja on_closing (bez tego program będzie cały czas działał, nawet po zamknięciu okna)
        self.app.mainloop() 

    def on_closing(self) -> None:
        '''Zakończenie pracy okna'''
        self.app.quit() #zakończenie pętli mainloop
        self.app.destroy() #zniszczenie okna

    def show_comparing_window(self) -> None:
        '''Wyświetlenie okna, w którym można porównać różne miasta w danym kraju'''
        CTK_Window = ctkAppCompare(self.df, self.cities)

    def show_city_window(self) -> None:
        '''Wyświetlenie okna, w którym można wyświetlić dane dla wybranego miasta w danym kraju'''
        CTk_Window = ctkAppCity(self.df, self.cities)

    def CenterWindowToDisplay(self, Screen: ctk.CTk, width: int, height: int, scale_factor: float=1.0) -> str:
        '''Wyśrodkowanie na ekranie wyświetlanego okna'''
        screen_width = Screen.winfo_screenwidth() #szerokość ekranu w pikselach
        screen_height = Screen.winfo_screenheight() #wysokość ekranu w pikselach
        x = int(((screen_width/2) - (width/2)) * scale_factor)
        y = int(((screen_height/2) - (height/1.5)) * scale_factor)
        return f"{width}x{height}+{x}+{y}"

if __name__ == "__main__":     
    start_window = start.starting_window()
    cities = choose_country(start_window.country)    
    download_country_data(cities)
    df = pd.read_csv("jakosc_powietrza.csv") #zczytanie danych z pliku csv
    df = df.dropna(axis=1, how='all') #usunięcie kolumn, w których nie ma żadnych danych
    CTK_Window = ctkAppChoice(cities, df)