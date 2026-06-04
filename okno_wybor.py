import customtkinter as ctk
from typing import Callable

class ctkAppChoice:
    def __init__(self, root: ctk.CTk, callback: Callable):
        self.callback = callback 
        self.window = ctk.CTkToplevel(root)  #utworzenie dodatkowego okna
        self.window.title("Jakość powietrza")
        self.window.geometry(self._center(self.window, 700, 200))
        self.window.resizable(False, False) #zablokowanie możliwości zmiany rozmiaru okna

        self.textbox = ctk.CTkTextbox(master=self.window, width=636, height=85, text_color="#99CCFF", font=('Helvetica', 19))
        self.textbox.pack(padx=20, pady=20)
        self.textbox.insert("0.0", "Co chcesz zrobić? Porównać poziom zanieczyszczenia dla największych miast w wybranym kraju, czy wyświetlić dane dla jednego z tych miast? Wciśnij odpowiedni przycisk.")
        self.textbox.tag_config("center", justify="center")
        self.textbox.tag_add("center", "1.0", "end")

        ctk.CTkButton(master=self.window, text="Porównanie miast", font=('Helvetica', 15), command=lambda: self._close("compare")).place(relx=0.15, rely=0.7)
        ctk.CTkButton(master=self.window, text="Dane dla wybranego miasta", font=('Helvetica', 15), command=lambda: self._close("city")).place(relx=0.6, rely=0.7)

        self.window.protocol("WM_DELETE_WINDOW", lambda: self._close(None))

    def _close(self, next_window):
        '''Zamknięcie okna i, jeśli użyttkownik wybrał kolejne okno, otwarcie nowego okna'''
        self.window.destroy()
        self.callback(next_window)

    def _center(self, window, width, height):
        '''Wyświetlanie okna idealnie na środku ekranu'''
        sw = window.winfo_screenwidth() #szerokość ekranu
        sh = window.winfo_screenheight() #wysokość ekranu
        x = (sw - width) // 2
        y = (sh - height) // 2
        return f"{width}x{height}+{x}+{y}"

