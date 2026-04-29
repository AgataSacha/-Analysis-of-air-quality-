import customtkinter as ctk
import analiza_danych as ad
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

        combobox = ctk.CTkComboBox(master=self.app, values=cities, command=self.combobox_callback)
        combobox.place(relx=0.8, rely=0.1)
        combobox.set("Poznań")

        self.button2 = ctk.CTkButton(master=self.app, text="Wyświetl wykres kołowy przedstawiający skład powietrza", command=lambda: self.choose_plot(ad.pie_chart_of_air_composition_in_chosen_city))
        self.button2.place(relx=0.8, rely=0.7)

        self.app.protocol("WM_DELETE_WINDOW", self.on_closing) #po ręcznym zamknięciu okna zadziała funkcja on_closing (bez tego program będzie cały czas działał, nawet po zamknięciu okna)
        self.app.mainloop() 

    def on_closing(self):
        '''Zakończenie pracy okna'''
        self.app.quit() #zakończenie pętli mainloop
        self.app.destroy() #zniszczenie okna

    def combobox_callback(self, chosen_city):
        '''Przypisanie zmiennej miasta wybranego z listy rozwijalnej'''
        self.city = chosen_city

    def choose_plot(self, plot_func: Callable[[pd.DataFrame, str], None]): #ta funkcja przyjmuje za argument funkcję, która z kolei przyjmuje za argument pandas data Frame oraz str (czyli nazwę miasta)
        '''Wywołanie odpowiedniej funkcji rysującej wykres, a następnie wywołanie funkcji, która go wyświetli'''
        fig = plot_func(ad.df, self.city)
        self.show_plot(fig)

    def show_plot(self, fig):
        '''Wyświetlanie w oknie wybranego wykresu'''
        canvas = FigureCanvasTkAgg(fig, master=self.frame)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0, rely=0, relwidth=1.0, relheight=1.0) #przy wyświetlaniu wykres wypełni cały frame


if __name__ == "__main__":        
    CTK_Window = ctkAppCity()