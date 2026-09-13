# 🌍 App analyzing air quality and weather

## Project Description
A Python desktop app for fetching, analyzing, and visualizing air quality and weather data for European cities using the WAQI API (https://waqi.info/).

## **📌 Features**

### **🔹 Choosing country**
<img width="351" height="172" alt="image" src="https://github.com/user-attachments/assets/ec92621e-d24e-4952-b951-bb5b759e0791" />

### **🔹 Data Fetching**
- Automatically assigns major cities for the selected country.
- Fetches real-time air quality data for those cities
- Saves data to `jakosc_powietrza.csv`.

### **🔹 Analysis & Visualization**
<img width="861" height="270" alt="image" src="https://github.com/user-attachments/assets/1100b8fd-42a0-4bcd-98d7-6f899c3bcbef" />

#### **City Comparison Mode**
- AQI bar chart for comparing pollution levels.
- Stacked bar chart for PM2.5 and PM10.
- Weather condition charts (temperature, humidity, wind, pressure).
- Full data table with scrollable view.
- AQI statistics (min, max, mean, standard deviation, variance).
<img width="1377" height="910" alt="image" src="https://github.com/user-attachments/assets/8e564223-df5e-4893-a8b9-cf9c4c4bd60d" />


#### **Single City Mode**
- Pie chart of air composition (NO₂, O₃, SO₂, CO).
- Weather conditions display.
<img width="1362" height="897" alt="image" src="https://github.com/user-attachments/assets/41e48113-4142-4aa9-985d-e84a237c160f" />


## **📦 Requirements**
   Tool | Version | Notes |
 |------|---------|-------|
 | Python | 3.8+ | Recommended: 3.10+ |
 | pip | - | Package manager |

### **Python Dependencies**
```text
customtkinter==5.2.0
pandas==2.0.0+
numpy==1.24.0+
matplotlib==3.7.0+
requests==2.31.0+
```

## ⚙️ Installation
### 1. Clone the Repository
```bash
git clone https://github.com/your-username/air-quality-analyzer.git
cd air-quality-analyzer
```
### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up WAQI API Token
1. Register at https://waqi.info/ and get free API token.
2. Create a file `moj_token.txt` in the project rooot.
3. Paste your token in the file.

## 🚀 Usage

### Run the Application
```bash
python main.py
```

### Instructions
1. Select a country from the dropdown.
2. Click **OK** to fetch data.
3. Choose:
- **Porównanie miast** to view charts and statistics comparing cities
- **dane dla wybranego miasta** to explore detailed data for one city.
4. Click **Cofnij** to return to the previous window.

## 🗂️ Project structure
```text
ir-quality-analyzer/
├── main.py
├── gui/
│   ├── window_first.py
│   ├── window_choosing.py
│   ├── window_chosen_city.py
│   └── window_comparing_cities.py
├── data_download_and_analysis/
│   ├── create_csv.py
│   ├── data_analysis_chosen_city.py
│   └── data_analysis_comparing_cities.py
├── moj_token.txt
└── jakosc_powietrza.csv
```

## 🎨 Technologies
* **Python** - core language
* **CustomTkinter** - GUI library
* **Pandas** - data manipulation
* **Matplotlib** - visualization
* **WAQI API** - air quality data source

