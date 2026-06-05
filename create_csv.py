#W tym pliku znajduje się kod, dzięki któremu pobierane są dane ze strony dotyczące wybranych miast i są one wstawiane do pliku csv.

import requests #biblioteka do komunikacji ze stronami internetowymi
import csv #biblioteka potrzebna do utworzenia pliku csv z pobranymi danymi
import time #biblioteka zapewniająca funkcje obliczające czas i opóźniające działanie programu

def choose_country(country: str) -> list[str]:
    '''Przypisanie odpowiedniej listy miast zgodnie z krajem, który wybrał użytkownik'''
    if country == "Poland":
        cities = ["Warszawa", "Kraków", "Wrocław", "Łódź", "Poznań", "Gdańsk", "Szczecin", "Lublin", "Bydgoszcz", "Białystok", "Katowice"]
    elif country == "Germany":
        cities = ["Berlin", "Hamburg", "München", "Köln", "Frankfurt", "Stuttgart", "Düsseldorf", "Leipzig", "Dortmund", "Essen"]
    elif country == "France":
        cities = ["Paris", "Marseille", "Lyon", "Nice", "Nantes", "Montpellier", "Strasbourg", "Bordeaux", "Lille"]
    elif country == "Spain":
        cities = ["Madrid", "Barcelona", "Valencia", "Zaragoza", "Sevilla", "Málaga", "Murcia", "Alicante", "Bilbao"]
    elif country == "Sweden":
        cities = ["Stockholm", "Gothenburg", "Malmö", "Uppsala", "Helsingborg", "Linköping", "Örebro", "Västerås", "Jönköping", "Norrköping"]
    elif country == "Finland":
        cities = ["Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu", "Turku", "Jyväskylä", "Kuopio", "Lahti", "Pori", "Joensuu", "Kouvola"]
    elif country == "Norway":
        cities = ["Oslo", "Bergen", "Trondheim", "Stavanger", "Drammen", "Sarpsborg", "Kristiansand", "Tønsberg", "Skien"]
    elif country == "Ukraine":
        cities = ["Kyiv", "Odesa", "Dnipro", "Lviv", "Zaporizhzhia", "Kryvyi Rih", "Mariupol"]
    elif country == "Italy":
        cities = ["Roma", "Milano", "Napoli", "Torino", "Palermo", "Genova", "Bologna", "Firenze", "Bari", "Catania", "Verona"]
    elif country == "Great Britain":
        cities = ["Birmingham", "Leeds", "Glasgow", "Manchester", "Sheffield", "Edinburgh", "Liverpool", "Bristol", "Cardiff", "London"]
    return cities

def get_data (city: str, token: str) -> dict:
    '''Pobieranie danych ze strony'''
    url = f"https://api.waqi.info/feed/{city}/?token={token}"
    response = requests.get(url, timeout=10, stream=True) #timeout - jeśli uzyskiwanie odpowiedzi potrwa dłużej niż 10 sekund, program wstrzyma swoje działanie
    response.raise_for_status() #sprawdzenie, czy odpowiedź została uzyskana
    data = response.json() #przerobienie pobranych danych na format json
    if data["status"] == "ok":
        return data
        

def adjust_data(city: str, data: dict) -> dict:
    '''Przystosowanie danych'''
    dt = data["data"] #przypisanie, żeby nie powtarzać ciągle długiego zapisu
    d = data["data"].get("iaqi") #tak jak powyżej
    #Nie każda stacja zbiera wszystkie dane, dlatego zastosowano poniżej {}, gdyby dany klucz nie występował
    # oraz "", aby w wypadku braku danych w pliku csv było po prostu puste pole
    return {
            "Data i godzina pomiaru": dt.get("time", {}).get("s", ""), 
            "Miasto": city,
            "Współrzędne geograficzne": dt["city"].get("geo",""),
            "AQI": dt.get("aqi", ""),
            "Główne zanieczyszczenie": dt.get("dominantpol",""),
            "PM2,5 (Pył zawieszony drobny)": d.get("pm25", {}).get("v", ""),
            "PM10 (Pył zawieszony gruby)": d.get("pm10", {}).get("v", ""),
            "Dwutlenek azotu": d.get("no2", {}).get("v", ""),
            "Ozon": d.get("o3", {}).get("v", ""),
            "Dwutlenek siarki": d.get("so2", {}).get("v", ""),
            "Tlenek węgla": d.get("co", {}).get("v", ""),
            "Temperatura": d.get("t", {}).get("v", ""),
            "Wilgotność": d.get("h", {}).get("v", ""),
            "Ciśnienie": d.get("p", {}).get("v", ""),
            "Wiatr": d.get("w", {}).get("v", "")
        }
    
def get_csv(the_data: list[dict], file_name: str = "jakosc_powietrza.csv") -> None:
    '''Uzyskanie pliku csv z danymi'''
    headers: list[str] = [
        "Data i godzina pomiaru",
        "Miasto",
        "Współrzędne geograficzne",
        "AQI",
        "Główne zanieczyszczenie",
        "PM2,5 (Pył zawieszony drobny)",
        "PM10 (Pył zawieszony gruby)",
        "Dwutlenek azotu",
        "Ozon",
        "Dwutlenek siarki",
        "Tlenek węgla",
        "Temperatura",
        "Wilgotność",
        "Ciśnienie",
        "Wiatr"
    ]

    with open(file_name, mode="w", newline="", encoding="utf-8") as csvfile: #tworzenie pliku csv
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader() #nazwy kolumn
        writer.writerows(the_data) #zawartości kolummn

    
def download_country_data(cities: list[str]) -> None:
    '''Pobieranie danych dla kolejnych miast w wybranym kraju'''
    #token znajduje się w osobnym pliku tekstowym, należy go zczytać
    f = open("moj_token.txt")
    token = f.read()
    f.close()

    the_data = []
    print("Trwa pobieranie danych")
    start_time = time.time() #zczytanie godziny, o której rozpoczęło się pobieranie
    for city in cities:
        print("...")
        data = get_data(city, token) #pobieranie danych dla każdego miasta po kolei
        if data:
            row = adjust_data(city, data) #przystosowanie danych dla każdego miasta po kolei
            the_data.append(row) #dodanie danych do listy
        time.sleep(0.01) #spowolnienie pętli, aby na pewno nie przeciążyć serwera
    download_time = time.time()-start_time #obliczenie, jak długo trwało pobieranie danych
    print(f"Pobieranie zakończone, trwało {download_time} sekund.")
    get_csv(the_data) #utworzenie pliku csv zawierającego pobrane dane

