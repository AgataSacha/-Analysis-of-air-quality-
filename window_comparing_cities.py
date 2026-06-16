#W tym pliku tworzone jest okno, gdzie są porównywane miasta w wybranym wcześniej kraju.

import customtkinter as ctk 
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #bibloteka, dzięki której można wyświetlać wykresy w oknie
from typing import Callable 
import pandas as pd
import tkinter.ttk as ttk #moduł biblioteki tkinter, który daje dostęp do widżetów (tu został wykorzystany do wyświetlenia tabeli oraz paska przewijania)

import data_analysis_comparing_cities as ad

class ctkAppCompare:
    def __init__(self, root: ctk.CTk, df: pd.DataFrame, cities: list[str], callback: Callable):
        self.df = df
        self.cities = cities
        self.callback = callback #funkcja, która zamyka okno (i ewentualnie cofa do poprzedniego okna)
        self.canvas = None #domyślne ustawienie, że nie ma żadnego wykresu
        self.is_closing = False #domyślne ustawienie zmiennej, która informuje o tym, czy okno właśnie się zamyka czy nie
        self.app = ctk.CTkToplevel(root) #stworzenie dodatkowego okna (dla głównego okna root)
        self.app.title("Jakość powietrza")
        self.app.geometry("1100x700")
        self.app.resizable(False, False)
        self.app.update()

        self.frame = ctk.CTkFrame(master=self.app, height=680, width=self.app.winfo_width()*0.6, fg_color="black") #pole, w którym będą się wyświetlać wykresy
        self.frame.grid(row=0, column=0, padx=10, pady=10) #bez tego frame się nie wyświetli
        self.frame.grid_propagate(False) #frame nie będzie dopasowywał swojego rozmiaru do zawartości

        self.button_aqi_in_cities = ctk.CTkButton(master=self.app, width=210, text="Wyświetl wykres porównujący AQI", command=lambda: self.choose_plot(ad.bar_plot_of_aqi_in_cities)) #musi być lambda, bo inaczej funkcja wywoła się od razu, a nie dopiero po kliknięciu przycisku (dlatego, że self.choose_plot() wymaga argumentu, gdyby było samo choose_plot, to nie byłoby problemu)
        self.button_aqi_in_cities.place(relx=0.79, rely=0.05) #położenie przycisku względem frame

        self.button_typ_of_pollution = ctk.CTkButton(master=self.app, width=210, text="Wyświetl wykres porównujący rodzaj i poziom zanieczyszczenia", command=lambda: self.choose_plot(ad.stacked_bar_plot_type_of_pollution))
        self.button_typ_of_pollution.place(relx=0.79, rely=0.11)
        self.button_typ_of_pollution._text_label.configure(wraplength=210) #zawijanie tekstu na przycisku

        self.button_table = ctk.CTkButton(master=self.app, width=210, text="Wyświetl tabelę ze wszystkimi danymi", command=self.show_table)
        self.button_table.place(relx=0.79, rely=0.21)
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

        self.statistics_frame = ctk.CTkFrame(master=self.app, height=200, width=self.app.winfo_width()*0.175, fg_color="black") #pole, w którym będą wyświetlane podstawowe statystyki
        self.statistics_frame.place(relx=0.77, rely=0.6)

        city_biggest_poll, biggest_poll = ad.show_city_with_the_biggest_pollution(self.df)
        city_smallest_poll, smallest_poll = ad.show_city_with_the_smallest_pollution(self.df)
        mean_poll, std_poll, var_poll = ad.statistics(self.df)

        self.textbox_statistic = ctk.CTkTextbox(master=self.statistics_frame, height=200, width=self.app.winfo_width()*0.175, fg_color="black", text_color="#99CCFF", font=('Helvetica',12)) #pole tekstowe
        self.textbox_statistic.place(relx=0.5, rely=0.5, anchor="center")
        self.textbox_statistic.insert("0.0", f"Statystyki dotyczące AQI (Air Quality Index) \n \nNajwyższe zanieczyszczenie: {city_biggest_poll} \nPoziom zanieczyszczenia: {biggest_poll} \n \nNajniższe zanieczyszczenie: {city_smallest_poll} \nPoziom zanieczyszczenia: {smallest_poll} \n \nŚrednie zanieczyszczenie: {mean_poll}\n \nOdchylenie standardowe: {std_poll} \n \nWariancja: {var_poll}" )

        self.return_button = ctk.CTkButton(master=self.app, width=20, text="Cofnij", command=lambda: self.on_closing(True))
        self.return_button.place(relx=0.86, rely=0.95)

        self.app.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(False)) #po ręcznym zamknięciu okna zadziała funkcja on_closing (bez tego program będzie cały czas działał, nawet po zamknięciu okna)

    def choose_plot(self, plot_func: Callable[[pd.DataFrame], matplotlib.figure.Figure]) -> None: #ta funkcja przyjmuje za argument funkcję, która z kolei przyjmuje za argument pandas data Frame i zwraca wykres matplotlib
        '''Wywołanie odpowiedniej funkcji rysującej wykres, a następnie wywołanie funkcji, która go wyświetli'''
        fig = plot_func(self.df)
        self.show_plot(fig)

    def show_plot(self, fig: matplotlib.figure.Figure) -> None: #funkcja przyjmuje wykres jako argument
        '''Wyświetlanie w oknie wybranego wykresu'''
        if self.is_closing: #zabezpieczenie, że jeśli użytkownik kliknie przycisk rysowania wykresu w trakcie zamykania okna, to nic się nie wydarzy
            return
        if self.canvas is not None: #sprawdzenie, czy jakiś wykres nie jest już wyświetlony, jesli jest, to stary widget jest niszczony
            self.canvas.get_tk_widget().destroy()
            self.canvas = None
        self.canvas = FigureCanvasTkAgg(fig, master=self.frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(relx=0, rely=0, relwidth=1.0, relheight=1.0) #przy wyświetlaniu wykres wypełni cały frame

    def check_the_checkbox(self, check_var: ctk.StringVar, plot_func: Callable[[pd.DataFrame], matplotlib.figure.Figure]) -> None:
        '''Jeśli checkbox jest zaznaczony, to wszystkie inne zostaną odznaczone, a następnie zostanie wywołana funkcja rysująca wykres. Jeśli checkbox zostanie odznaczony, to nic nie będzie się wyświetlać we frame'''
        if self.is_closing:  #zabezpieczenie, że jeśli użytkownik zaznaczy checkboxa w trakcie wyłączania okna, to nic się nie wydarzy
            return
        all_check_boxes = [self.check_var_temp, self.check_var_hum, self.check_var_wind, self.check_var_press] #lista wszystkich checkboxów
        all_check_boxes.remove(check_var) #usunięcie z listy tego checkboxa, który został zaznaczony
        for var in all_check_boxes:
            var.set("off") #odznaczenie wszystkich pozostałych checkboxów
        if check_var.get() == "on":
            self.show_plot(plot_func(self.df)) #dla zaznaczonego checkboxa sotanie wyświetlony odpowiedni wykres
        else:
            for widget in self.frame.winfo_children(): #iterowanie po elementach, które wyświetlają się we frame i usuwanie ich
                widget.destroy()

    def show_table(self) -> None:
        '''Wyświetlanie tabeli z danymi z pandas DataFrame'''
        tree = ttk.Treeview(self.frame, columns=list(self.df.columns), show="headings")
        for col in self.df.columns:
            tree.heading(col, text=col) #nazwy kolumn
        for _, row in self.df.iterrows(): #iterowanie po elementach dataframe'u
            tree.insert("", "end", values=list(row)) #dodawanie wartości do komórek
        scrollbar_x = ttk.Scrollbar(self.frame, orient="horizontal", command=tree.xview) #poziomy pasek przewijania
        tree.configure(xscrollcommand=scrollbar_x.set)
        tree.grid(row=0, column=0, sticky="nsew") #umieszczenie tabeli w siatce frame'u
        scrollbar_x.grid(row=1, column=0, sticky="ew") #dodanie widoku paska przesuwania
        self.frame.grid_rowconfigure(0, weight=1) #dzięki tej i następnej linii tkinter wie, że tabela ma zająć całego frame'a
        self.frame.grid_columnconfigure(0, weight=1)

    def on_closing(self, go_back: bool) -> None:
        '''Zamykanie okna'''
        if self.is_closing: #zabezpieczenie, że jeśli użytkownik dwukrotnie kliknie przycisk wyłączenia, to okno i tak wyłączy się poprawnie
            return
        self.is_closing = True 
        if self.canvas is not None: #jeżeli jest jakiś wykres, to zostanie zniszczony
            try:
                self.canvas.get_tk_widget().destroy()
            except Exception:
                pass
            self.canvas = None
        if not go_back: #jeśli użytkownik kliknął X, to program zakończy swoje działanie 
            self.app.quit() #zakończenie działania pętli mainloop
        self.app.destroy() #zniszczenie okna
        self.callback(go_back) #jeśli użytkownik kliknął "Cofnij", to wyświetli się okno wyboru


if __name__ == "__main__":        
    CTK_Window = ctkAppCompare()