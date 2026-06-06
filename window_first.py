import customtkinter as ctk

countries = ["Poland", "Germany", "France", "Spain", "Sweden", "Finland", "Norway", "Ukraine", "Italy", "Great Britain"]

class starting_window:
    def __init__(self):
        ctk.set_appearance_mode("dark") #ciemny tryb
        self.app = ctk.CTk() 
        self.app.title("Jakość powietrza") #nazwa wyświetlanego okna
        self.app.geometry(self.CenterWindowToDisplay(self.app, 300, 120, self.app._get_window_scaling())) #wymiary i położenie wyświetlanego okna (wycenstrowanie go na ekranie)
        self.app.resizable(False, False) #brak możliwości zmiany rozmiaru okna przez użytkownika
        self.app.update()

        self.textbox = ctk.CTkTextbox(master=self.app, width=270, height=80, text_color="#99CCFF", font=('Helvetica',15)) #pole tekstowe
        self.textbox.pack(padx=20, pady=7) #położenie pola tekstowego
        self.textbox.insert("0.0", "Dla którego kraju chcesz wyświetlić dane?") #tekst
        self.textbox.tag_config("center", justify="center") #ta linijka i jedna poniżej odpowiadają za wyrównanie tekstu do środka
        self.textbox.tag_add("center", "1.0", "end")

        combobox = ctk.CTkComboBox(master=self.app, values=countries, command=self.combobox_callback) #lista rozwijalna z nazwami miast
        combobox.place(relx=0.3, rely=0.45) #położenie listy rozwijalnej
        combobox.set("Wybierz kraj") #komunikat domyślnie wyświetlany na liście rozwijalnej

        self.acceptance = ctk.CTkButton(master=self.app, width=10, height=10, text="OK", command=self.on_closing) #utworzenie przycisku
        self.acceptance.place(relx=0.45, rely=0.8) #położenie przycisku

        self.app.protocol("WM_DELETE_WINDOW", self.on_closing) #WM_DELETE_WINDOW to sygnał wysyłany do aplikacji, gdy użytkownik kliknie X. Wywoła on funkcję on_closing 
        self.app.mainloop()

    def combobox_callback(self, chosen_country: str) -> None:
        '''Przypisanie zmiennej kraju wybranego z listy rozwijalnej'''
        self.country = chosen_country
        
    def CenterWindowToDisplay(self, Screen: ctk.CTk, width: int, height: int, scale_factor: float=1.0) -> str:
        '''Wyśrodkowanie na ekranie wyświetlanego okna'''
        screen_width = Screen.winfo_screenwidth() #szerokość ekranu w pikselach
        screen_height = Screen.winfo_screenheight() #wysokość ekranu w pikselach
        x = int(((screen_width/2) - (width/2)) * scale_factor)
        y = int(((screen_height/2) - (height/1.5)) * scale_factor)
        return f"{width}x{height}+{x}+{y}"
    
    def on_closing(self) -> None:
        '''Zakończenie pracy okna'''
        self.app.quit() #zakończenie pętli mainloop
        self.app.destroy() #zniszczenie okna

