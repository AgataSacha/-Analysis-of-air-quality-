#W tym pliku tworzone jest okno wyboru, wyświetlane po pobraniu danych, w którym użytkownik wybiera, co chce zrobić dalej.

import customtkinter as ctk
from typing import Callable

class ctkAppChoice:
    def __init__(self, root: ctk.CTk, callback: Callable):
        self.root = root
        self.callback = callback 
        self.window = ctk.CTkToplevel(root)  #utworzenie dodatkowego okna
        self.window.title("Jakość powietrza")
        self.window.geometry(self.center(self.window, 700, 200)) #wycentrowanie okna na ekranie
        self.window.resizable(False, False) #zablokowanie możliwości zmiany rozmiaru okna

        self.textbox = ctk.CTkTextbox(master=self.window, width=636, height=85, text_color="#99CCFF", font=('Helvetica', 19)) #utworzenie pola tekstowego
        self.textbox.pack(padx=20, pady=20) #umiejscowienie pola tekstowego
        self.textbox.insert("0.0", "Co chcesz zrobić? Porównać poziom zanieczyszczenia dla największych miast w wybranym kraju, czy wyświetlić dane dla jednego z tych miast? Wciśnij odpowiedni przycisk.")
        self.textbox.tag_config("center", justify="center") #wyrównanie tekstu do środka
        self.textbox.tag_add("center", "1.0", "end")

        ctk.CTkButton(master=self.window, text="Porównanie miast", font=('Helvetica', 15), command=lambda: self.on_closing("compare")).place(relx=0.15, rely=0.7)
        ctk.CTkButton(master=self.window, text="Dane dla wybranego miasta", font=('Helvetica', 15), command=lambda: self.on_closing("city")).place(relx=0.6, rely=0.7)

        self.window.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(None))

    def on_closing(self, next_window: str|None) -> None:
        '''Zamknięcie okna i, jeśli użytkownik wybrał kolejne okno, otwarcie nowego okna'''
        if not next_window:
            self.window.quit()
        self.window.destroy()
        self.callback(next_window)

    def center(self, window: ctk.CTkToplevel, width: int, height: int) -> str:
        '''Wyświetlanie okna idealnie na środku ekranu'''
        screen_width = window.winfo_screenwidth() #szerokość ekranu w pikselach
        screen_height = window.winfo_screenheight() #wysokość ekranu w pikselach
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        return f"{width}x{height}+{x}+{y}"
