# 🌍 App analyzing air quality and weather

**Project Description**
A Python desktop app for fetching, analyzing, and visualizing air quality and weather data for European cities using the WAQI API.

## **📌 Features**

### **🔹 Choosing country**
<img width="361" height="182" alt="image" src="https://github.com/user-attachments/assets/ec92621e-d24e-4952-b951-bb5b759e0791" />

### **🔹 Data Fetching**
- Automatically assigns major cities for the selected country.
- Fetches real-time air quality data for those cities
- Saves data to `jakosc_powietrza.csv`.

### **🔹 Analysis & Visualization**
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









Data source: https://waqi.info/.
