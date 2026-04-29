#W tym pliku znajdują się wszystkie funkcje odpowiadające za wyświetlanie okienka za pomocą biblioteki customtkinter
# CAŁY KOD TUTAJ JEST PRÓBNY, TO TRZEBA PRZEROBIĆ

import analiza_danych as ad
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #bibloteka, dzięki której można wyświetlać wykresy w oknie
from collections.abc import Callable
import pandas as pd

class ctkApp:
    def __init__(self):
        ctk.set_appearance_mode("dark") #ciemny tryb wyświetlanego okna
        self.app = ctk.CTk() 
        self.app.title("Jakość powietrza") #nazwa wyświetlanego okna
        self.app.geometry("1100x700") #wymiary wyświetlanego okna
        self.app.update()

        self.frame = ctk.CTkFrame(master=self.app, height=680, width=self.app.winfo_width()*0.6, fg_color="black") #pole, w którym będą się wyświetlać wykresy
        self.frame.grid(row=0, column=0, padx=10, pady=10) 

        self.button = ctk.CTkButton(master=self.app, text="Wyświetl wykres porównujący AQI", command=lambda: self.choose_plot(ad.bar_plot_of_aqi_in_cities)) #musi być lambda, bo inaczej funkcja wywoła się od razu, a nie dopiero po kliknięciu przycisku (dlatego, że self.choose_plot() wymaga argumentu, gdyby było samo choose_plot, to nie byłoby problemu)
        self.button.grid(row=0, column=1, padx=10, pady=5)
        
        self.app.protocol("WM_DELETE_WINDOW", self.on_closing) #po ręcznym zamknięciu okna zadziała funkcja on_closing (bez tego program będzie cały czas działał, nawet po zamknięciu okna)
        self.app.mainloop() 

    def choose_plot(self, plot_func: Callable[[pd.DataFrame], None]): #ta funkcja przyjmuje za argument funkcję, która z kolei przyjmuje za argument pandas data Frame, ale nic nie zwraca, dlatego None
        '''Wywołanie odpowiedniej funkcji rysującej wykres, a następnie wywołanie funkcji, która go wyświetli'''
        fig = plot_func(ad.df)
        self.show_plot(fig)

    def show_plot(self, fig):
        '''Wyświetlanie w oknie wybranego wykresu'''
        canvas = FigureCanvasTkAgg(fig, master=self.frame)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0, rely=0, relwidth=1.0, relheight=1.0) #przy wyświetlaniu wykres wypełni cały frame

    def on_closing(self):
        self.app.quit() #zakończenie pętli mainloop
        self.app.destroy() #zniszczenie okna

if __name__ == "__main__":        
    CTK_Window = ctkApp()
