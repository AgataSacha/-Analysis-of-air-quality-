#W tym pliku znajdują się wszystkie funkcje odpowiadające za wyświetlanie okienka za pomocą biblioteki customtkinter
# CAŁY KOD TUTAJ JEST PRÓBNY, TO TRZEBA PRZEROBIĆ

import analiza_danych_porownanie as ad
import customtkinter as ctk
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #bibloteka, dzięki której można wyświetlać wykresy w oknie
from collections.abc import Callable
import pandas as pd
import tkinter.ttk as ttk

class ctkAppCompare:
    def __init__(self):
        ctk.set_appearance_mode("dark") #ciemny tryb wyświetlanego okna
        self.app = ctk.CTk() 
        self.app.title("Jakość powietrza") #nazwa wyświetlanego okna
        self.app.geometry("1100x700") #wymiary wyświetlanego okna
        self.app.update()

        self.frame = ctk.CTkFrame(master=self.app, height=680, width=self.app.winfo_width()*0.6, fg_color="black") #pole, w którym będą się wyświetlać wykresy
        self.frame.grid(row=0, column=0, padx=10, pady=10) 
        self.frame.grid_propagate(False) #frame nie będzie dopasowywał swojego rozmiaru do zawartości

        self.button_aqi_in_cities = ctk.CTkButton(master=self.app, width=210, text="Wyświetl wykres porównujący AQI", command=lambda: self.choose_plot(ad.bar_plot_of_aqi_in_cities)) #musi być lambda, bo inaczej funkcja wywoła się od razu, a nie dopiero po kliknięciu przycisku (dlatego, że self.choose_plot() wymaga argumentu, gdyby było samo choose_plot, to nie byłoby problemu)
        self.button_aqi_in_cities.place(relx=0.79, rely=0.2) #położenie przycisku względem frame

        self.button_typ_of_pollution = ctk.CTkButton(master=self.app, width=210, text="Wyświetl wykres porównujący rodzaj i poziom zanieczyszczenia", command=lambda: self.choose_plot(ad.stacked_bar_plot_type_of_pollution))
        self.button_typ_of_pollution.place(relx=0.79, rely=0.3)
        self.button_typ_of_pollution._text_label.configure(wraplength=210) #zawijanie tekstu na przycisku

        self.button_table = ctk.CTkButton(master=self.app, width=210, text="Wyświetl tabelę ze wszystkimi danymi", command=self.show_table)
        self.button_table.place(relx=0.79, rely=0.4)
        self.button_table._text_label.configure(wraplength=210)

        self.button_table = ctk.CTkButton(master=self.app, width=210, text="Wyświetl miasto o największym zanieczyszczeniu", command=lambda:self.show_city_with_biggest_pollution(ad.show_city_with_the_biggest_pollution))
        self.button_table.place(relx=0.79, rely=0.5)
        self.button_table._text_label.configure(wraplength=210)

        self.app.protocol("WM_DELETE_WINDOW", self.on_closing) #po ręcznym zamknięciu okna zadziała funkcja on_closing (bez tego program będzie cały czas działał, nawet po zamknięciu okna)
        self.app.mainloop() 

    def choose_plot(self, plot_func: Callable[[pd.DataFrame], matplotlib.figure.Figure]) -> None: #ta funkcja przyjmuje za argument funkcję, która z kolei przyjmuje za argument pandas data Frame i zwraca wykres matplotlib
        '''Wywołanie odpowiedniej funkcji rysującej wykres, a następnie wywołanie funkcji, która go wyświetli'''
        fig = plot_func(ad.df)
        self.show_plot(fig)

    def show_plot(self, fig: matplotlib.figure.Figure) -> None:
        '''Wyświetlanie w oknie wybranego wykresu'''
        canvas = FigureCanvasTkAgg(fig, master=self.frame)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0, rely=0, relwidth=1.0, relheight=1.0) #przy wyświetlaniu wykres wypełni cały frame

    def show_table(self) -> None:
        '''Wyświetlanie tabeli z danymi z pandas DataFrame'''
        tree = ttk.Treeview(self.frame, columns=list(ad.df.columns), show="headings")
        for col in ad.df.columns:
            tree.heading(col, text=col) #nazwy kolumn
        for _, row in ad.df.iterrows(): #iterowanie po elementach dataframe'u
            tree.insert("", "end", values=list(row)) #dodawanie wartości do komórek
        scrollbar_x = ttk.Scrollbar(self.frame, orient="horizontal", command=tree.xview) #poziomy pasek przewijania
        tree.configure(xscrollcommand=scrollbar_x.set)
        tree.grid(row=0, column=0, sticky="nsew") #umieszczenie tabeli w siatce frame'u
        scrollbar_x.grid(row=1, column=0, sticky="ew") #dodanie widoku paska przesuwania
        self.frame.grid_rowconfigure(0, weight=1) #dzięki tej i następnej linii tkinter wie, że tabela ma zająć całego frame'a
        self.frame.grid_columnconfigure(0, weight=1)


    def show_city_with_biggest_pollution(self, text_func: Callable[[pd.DataFrame], tuple[str, float]]) -> None:
        '''Wyświetlenie nazwy miasta o najgorszej jakości powietrza wraz z wartością'''
        city_biggest_poll, biggest_poll = text_func(ad.df)
        self.textbox = ctk.CTkTextbox(master=self.frame, height=680, width=self.app.winfo_width()*0.6, text_color="#99CCFF", font=('Helvetica',19)) #pole tekstowe
        self.textbox.place(relx=0.5, rely=0.5, anchor="center")  #wyśrodkowanie w frame, musi być place a nie pack, bo pack ignoruje rozmiar frame'a ustawiony poprzez propagate(False)
        self.textbox.insert("0.0", f"Największe zanieczyszczenie jest w mieście {city_biggest_poll}. \nIndeks jakości powietrza wynosi tam {biggest_poll}.") #tekst
        self.textbox.tag_config("center", justify="center") #ta linijka i jedna poniżej odpowiadają za wyrównanie tekstu do środka
        self.textbox.tag_add("center", "1.0", "end")


    def on_closing(self) -> None:
        '''Zakończenie pracy okna'''
        self.app.quit() #zakończenie pętli mainloop
        self.app.destroy() #zniszczenie okna

if __name__ == "__main__":        
    CTK_Window = ctkAppCompare()
