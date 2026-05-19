#W tym pliku znajdują się wszystkie funkcje odpowiadające za wyświetlanie okienka za pomocą biblioteki customtkinter
# CAŁY KOD TUTAJ JEST PRÓBNY, TO TRZEBA PRZEROBIĆ

import analiza_danych_porownanie as ad
import customtkinter as ctk 
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #bibloteka, dzięki której można wyświetlać wykresy w oknie
from typing import Callable 
import pandas as pd
import tkinter.ttk as ttk #moduł biblioteki tkinter, który daje dostęp do widżetów (tu został wykorzystany do wyświetlenia tabeli oraz paska przewijania)

class ctkAppCompare:
    def __init__(self):
        ctk.set_appearance_mode("dark") #ciemny tryb wyświetlanego okna
        self.app = ctk.CTk() 
        self.app.title("Jakość powietrza") #nazwa wyświetlanego okna
        self.app.geometry("1100x700") #wymiary wyświetlanego okna
        self.app.resizable(False, False)
        self.app.update()

        self.frame = ctk.CTkFrame(master=self.app, height=680, width=self.app.winfo_width()*0.6, fg_color="black") #pole, w którym będą się wyświetlać wykresy
        self.frame.grid(row=0, column=0, padx=10, pady=10) #bez tego frame się nie wyświetli
        self.frame.grid_propagate(False) #frame nie będzie dopasowywał swojego rozmiaru do zawartości

        self.button_aqi_in_cities = ctk.CTkButton(master=self.app, width=210, text="Wyświetl wykres porównujący AQI", command=lambda: self.choose_plot(ad.bar_plot_of_aqi_in_cities)) #musi być lambda, bo inaczej funkcja wywoła się od razu, a nie dopiero po kliknięciu przycisku (dlatego, że self.choose_plot() wymaga argumentu, gdyby było samo choose_plot, to nie byłoby problemu)
        self.button_aqi_in_cities.place(relx=0.79, rely=0.1) #położenie przycisku względem frame

        self.button_typ_of_pollution = ctk.CTkButton(master=self.app, width=210, text="Wyświetl wykres porównujący rodzaj i poziom zanieczyszczenia", command=lambda: self.choose_plot(ad.stacked_bar_plot_type_of_pollution))
        self.button_typ_of_pollution.place(relx=0.79, rely=0.16)
        self.button_typ_of_pollution._text_label.configure(wraplength=210) #zawijanie tekstu na przycisku

        self.button_table = ctk.CTkButton(master=self.app, width=210, text="Wyświetl tabelę ze wszystkimi danymi", command=self.show_table)
        self.button_table.place(relx=0.79, rely=0.26)
        self.button_table._text_label.configure(wraplength=210)

        self.textbox_statistic = ctk.CTkTextbox(master=self.app, height=50, width=self.app.winfo_width()*0.18, fg_color="transparent", font=('Helvetica',12, "bold")) #pole tekstowe
        self.textbox_statistic.place(relx=0.88, rely=0.35, anchor="center")
        self.textbox_statistic.insert("0.0", "Wyświetl wykres porównujący któryś z wybranych warunków pogodowych: " )
        
        self.check_var_temp = ctk.StringVar(value="off") #domyślnie checkboxy będą wyłączone (niezaznaczone)
        self.check_var_hum = ctk.StringVar(value="off")
        self.check_var_wind = ctk.StringVar(value="off")
        self.check_var_press = ctk.StringVar(value="off")

        self.checkbox_temp = ctk.CTkCheckBox(master=self.app, width=10, height=10, text="Temperatura", variable=self.check_var_temp, onvalue="on", offvalue="off", command=lambda: self.check_the_checkbox(self.check_var_temp, ad.barh_plot_tempetarure))
        self.checkbox_temp.place(relx=0.79, rely=0.4)

        self.checkbox_hum = ctk.CTkCheckBox(master=self.app, width=10, height=10, text="Wilgotność powietrza", variable=self.check_var_hum, onvalue="on", offvalue="off", command=lambda: self.check_the_checkbox(self.check_var_hum, ad.barh_plot_humidity))
        self.checkbox_hum.place(relx=0.79, rely=0.45)

        self.checkbox_wind = ctk.CTkCheckBox(master=self.app, width=10, height=10, text="Prędkość wiatru", variable=self.check_var_wind, onvalue="on", offvalue="off", command=lambda: self.check_the_checkbox(self.check_var_wind, ad.barh_plot_wind))
        self.checkbox_wind.place(relx=0.79, rely=0.5)

        self.checkbox_press = ctk.CTkCheckBox(master=self.app, width=10, height=10, text="Ciśnienie atmosferyczne", variable=self.check_var_press, onvalue="on", offvalue="off", command=lambda: self.check_the_checkbox(self.check_var_press, ad.barh_plot_press))
        self.checkbox_press.place(relx=0.79, rely=0.55)

        self.statistics_frame = ctk.CTkFrame(master=self.app, height=250, width=self.app.winfo_width()*0.175, fg_color="black") #pole, w którym będą wyświetlane podstawowe statystyki
        self.statistics_frame.place(relx=0.77, rely=0.6)

        city_biggest_poll, biggest_poll = ad.show_city_with_the_biggest_pollution(ad.df)
        city_smallest_poll, smallest_poll = ad.show_city_with_the_smallest_pollution(ad.df)
        mean_poll, std_poll, var_poll = ad.statistics(ad.df)

        self.textbox_statistic = ctk.CTkTextbox(master=self.statistics_frame, height=250, width=self.app.winfo_width()*0.175, fg_color="black", text_color="#99CCFF", font=('Helvetica',12)) #pole tekstowe
        self.textbox_statistic.place(relx=0.5, rely=0.5, anchor="center")
        self.textbox_statistic.insert("0.0", f"Statystyki dotyczące AQI (Air Quality Index) \n \nNajwyższe zanieczyszczenie: {city_biggest_poll} \nPoziom zanieczyszczenia: {biggest_poll} \n \nNajniższe zanieczyszczenie: {city_smallest_poll} \nPoziom zanieczyszczenia: {smallest_poll} \n \nŚrednie zanieczyszczenie: {mean_poll}\n \nOdchylenie standardowe: {std_poll} \n \nWariancja: {var_poll}" )

        self.app.protocol("WM_DELETE_WINDOW", self.on_closing) #po ręcznym zamknięciu okna zadziała funkcja on_closing (bez tego program będzie cały czas działał, nawet po zamknięciu okna)
        self.app.mainloop() 

    def choose_plot(self, plot_func: Callable[[pd.DataFrame], matplotlib.figure.Figure]) -> None: #ta funkcja przyjmuje za argument funkcję, która z kolei przyjmuje za argument pandas data Frame i zwraca wykres matplotlib
        '''Wywołanie odpowiedniej funkcji rysującej wykres, a następnie wywołanie funkcji, która go wyświetli'''
        fig = plot_func(ad.df)
        self.show_plot(fig)

    def show_plot(self, fig: matplotlib.figure.Figure) -> None: #funkcja przyjmuje wykres jako argument
        '''Wyświetlanie w oknie wybranego wykresu'''
        canvas = FigureCanvasTkAgg(fig, master=self.frame)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0, rely=0, relwidth=1.0, relheight=1.0) #przy wyświetlaniu wykres wypełni cały frame

    def check_the_checkbox(self, check_var: ctk.StringVar, plot_func: Callable[[pd.DataFrame], matplotlib.figure.Figure]) -> None:
        '''Jeśli checkbox jest zaznaczony, to zostanie wywołana funkcja rysująca wykres. Jeśli checkbox zostanie odznaczony, to nic nie będzie się wyświetlać we frame'''
        if check_var.get() == "on":
            self.show_plot(plot_func(ad.df))
        else:
            for widget in self.frame.winfo_children(): #iterowanie po elementach, które wyświetlają się we frame i usuwanie ich
                widget.destroy()

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

    def on_closing(self) -> None:
        '''Zakończenie pracy okna'''
        self.app.quit() #zakończenie pętli mainloop
        self.app.destroy() #zniszczenie okna

if __name__ == "__main__":        
    CTK_Window = ctkAppCompare()
