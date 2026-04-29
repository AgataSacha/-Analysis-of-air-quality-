import customtkinter as ctk
import okno_porownanie
import okno_miasto


class ctkAppChoice:
    def __init__(self):
        ctk.set_appearance_mode("dark")
        self.app = ctk.CTk() 
        self.app.title("Jakość powietrza") #nazwa wyświetlanego okna
        self.app.geometry("700x200") #wymiary wyświetlanego okna
        self.app.update()

        self.textbox = ctk.CTkTextbox(master=self.app, width=670, height=65, text_color="#99CCFF", font=('Helvetica',19)) #pole tekstowe
        self.textbox.pack(padx=20, pady=20) #położenie pola tekstowego
        self.textbox.insert("0.0", "Co chcesz zrobić? Porównać poziom zanieczyszczenia dla miast w Polsce, czy wyświetlić dane dla wybranego miasta? Wciśnij odpowiedni przycisk.") #tekst
        self.textbox.tag_config("center", justify="center") #ta linijka i jedna poniżej odpowiadają za wyrównanie tekstu do środka
        self.textbox.tag_add("center", "1.0", "end")

        self.button1 = ctk.CTkButton(master=self.app, text="Porównanie miast w Polsce",font=('Helvetica',15), command=self.show_comparing_window)
        self.button1.place(relx=0.15, rely=0.7)

        self.button2 = ctk.CTkButton(master=self.app, text="Dane dla wybranego miasta",font=('Helvetica',15), command=self.show_city_window)
        self.button2.place(relx=0.6, rely=0.7)

        self.app.protocol("WM_DELETE_WINDOW", self.on_closing) #po ręcznym zamknięciu okna zadziała funkcja on_closing (bez tego program będzie cały czas działał, nawet po zamknięciu okna)
        self.app.mainloop() 

    def on_closing(self):
        self.app.quit() #zakończenie pętli mainloop
        self.app.destroy() #zniszczenie okna

    def show_comparing_window(self):
        self.on_closing() #po wciśnięciu przycisku zostanie uruchomiona funkcja, która zamknie okno
        CTK_Window = okno_porownanie.ctkAppCompare()

    def show_city_window(self):
        self.on_closing()
        CTk_Window = okno_miasto.ctkAppCity()

if __name__ == "__main__":        
    CTK_Window = ctkAppChoice()