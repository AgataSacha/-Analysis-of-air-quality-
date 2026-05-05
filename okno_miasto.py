import customtkinter as ctk
import analiza_danych_miasto as ad
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #bibloteka, dzięki której można wyświetlać wykresy w oknie
from collections.abc import Callable
import pandas as pd
from tworzenie_csv import cities

class ctkAppCity:
    def __init__(self):
        ctk.set_appearance_mode("dark")
        self.app = ctk.CTk() 
        self.app.title("Jakość powietrza") #nazwa wyświetlanego okna
        self.app.geometry("1100x700") #wymiary wyświetlanego okna
        self.app.update()

        self.frame = ctk.CTkFrame(master=self.app, height=680, width=self.app.winfo_width()*0.6, fg_color="black") #pole, w którym będą się wyświetlać wykresy
        self.frame.grid(row=0, column=0, padx=10, pady=10)
        self.frame.grid_propagate(False) #frame nie będzie dopasowywał swojego rozmiaru do zawartości

        combobox = ctk.CTkComboBox(master=self.app, values=cities, command=self.combobox_callback)
        combobox.place(relx=0.8, rely=0.1)
        combobox.set("Poznań")

        self.button_air_composition = ctk.CTkButton(master=self.app, width=210, text="Wyświetl wykres kołowy przedstawiający skład powietrza", command=lambda: self.choose_plot(ad.pie_chart_of_air_composition_in_chosen_city))
        self.button_air_composition.place(relx=0.79, rely=0.4)
        self.button_air_composition._text_label.configure(wraplength=210) #zawijanie tekstu na przycisku

        self.app.protocol("WM_DELETE_WINDOW", self.on_closing) #po ręcznym zamknięciu okna zadziała funkcja on_closing (bez tego program będzie cały czas działał, nawet po zamknięciu okna)
        self.app.mainloop() 

    def on_closing(self) -> None:
        '''Zakończenie pracy okna'''
        self.app.quit() #zakończenie pętli mainloop
        self.app.destroy() #zniszczenie okna

    def combobox_callback(self, chosen_city) -> None:
        '''Przypisanie zmiennej miasta wybranego z listy rozwijalnej'''
        self.city = chosen_city

    def choose_plot(self, plot_func: Callable[[pd.DataFrame, str], None]) -> None: #ta funkcja przyjmuje za argument funkcję, która z kolei przyjmuje za argument pandas data Frame oraz str (czyli nazwę miasta)
        '''Wywołanie odpowiedniej funkcji rysującej wykres, a następnie wywołanie funkcji, która go wyświetli'''
        fig = plot_func(ad.df, self.city)
        if fig is None: #jeśli jest za mało danych, to funkcja pie_chart_of_air_composition_in_chosen_city zwraca None
            self.not_enough_data() #wówczas wyświetli się textbox informujący o za wiewystarczającej liczbie danych
        else:
            self.show_plot(fig) #jeśli są wszystkie dane, to zostanie wyświetlony wykres
    

    def not_enough_data(self) -> None:
        '''Jeśli nie ma wystarczająco danych, w oknie wyświetli się komunikat'''
        self.textbox = ctk.CTkTextbox(master=self.frame, height=680, width=self.app.winfo_width()*0.6, text_color="#99CCFF", font=('Helvetica',19)) #pole tekstowe
        self.textbox.place(relx=0.5, rely=0.5, anchor="center")  #wyśrodkowanie w frame, musi być place a nie pack, bo pack ignoruje rozmiar frame'a ustawiony poprzez propagate(False)
        self.textbox.insert("0.0", "Brak wystarczających danych") #tekst
        self.textbox.tag_config("center", justify="center") #ta linijka i jedna poniżej odpowiadają za wyrównanie tekstu do środka
        self.textbox.tag_add("center", "1.0", "end")


    def show_plot(self, fig) -> None:
        '''Wyświetlanie w oknie wybranego wykresu'''
        canvas = FigureCanvasTkAgg(fig, master=self.frame)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0, rely=0, relwidth=1.0, relheight=1.0) #przy wyświetlaniu wykres wypełni cały frame

if __name__ == "__main__":        
    CTK_Window = ctkAppCity()