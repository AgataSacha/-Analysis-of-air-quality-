#W tym pliku znajdują się wszystkie funkcje odpowiadające za wyświetlanie okienka za pomocą biblioteki customtkinter
# CAŁY KOD TUTAJ JEST PRÓBNY, TO TRZEBA PRZEROBIĆ

import analiza_danych as ad
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #bibloteka, dzięki której można wyświetlać wykresy w oknie

class ctkApp:
    def __init__(self):
        ctk.set_appearance_mode("dark") #ciemny tryb wyświetlanego okna
        self.app = ctk.CTk() 
        self.app.title("Jakość powietrza") #nazwa wyświetlanego okna
        self.app.geometry("1100x700") #wymiary wyświetlanego okna
        self.app.update()
        self.frame = ctk.CTkFrame(master=self.app, height=680, width=self.app.winfo_width()*0.6, fg_color="black") #pole, w którym będą się wyświetlać wykresy
        self.frame.grid(row=0, column=0, padx=10, pady=10) 

        self.button = ctk.CTkButton(master=self.app, text="Wyświetl wykres porównujący AQI", command=self.show_bar_plot_of_aqi_in_cities) #jeżeli użytkownik wciśnie ten przycisk, to uruchomi się funkcja show_bar_plot_of_aqi_in_cities
        self.button.grid(row=0, column=1, padx=10, pady=5)
        
        self.app.protocol("WM_DELETE_WINDOW", self.on_closing) #po ręcznym zamknięciu okna zadziała funkcja on_closing (bez tego program będzie cały czas działał, nawet po zamknięciu okna)
        self.app.mainloop() 

    def show_bar_plot_of_aqi_in_cities(self):
        '''Ta funkcja pobiera rysowanie wykresu kolumnowego z analiza_danych.py'''
        fig = ad.bar_plot_of_aqi_in_cities(ad.df)
        self.show_plot(fig)

    def show_plot(self, fig):
        '''Wyświetlanie w oknie wybranego wykresu'''
        canvas = FigureCanvasTkAgg(fig, master=self.frame)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0, rely=0)
        self.app.update()

    def on_closing(self):
        self.app.quit() #zakończenie pętli mainloop
        self.app.destroy() #zniszczenie okna

if __name__ == "__main__":        
    CTK_Window = ctkApp()
