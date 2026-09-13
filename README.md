# 🌍 App analyzing air quality and weather

**Project Description**
A Python desktop app for fetching, analyzing, and visualizing air quality and weather data for European cities using the WAQI API.

## **📌 Features**

### **🔹 Data Fetching**
- Fetches real-time air quality data for **10 European countries**.
- Automatically assigns major cities for the selected country.
- Saves data to `jakosc_powietrza.csv`.

### **🔹 Analysis & Visualization**
#### **City Comparison Mode**
- AQI bar chart for comparing pollution levels.
- Stacked bar chart for PM2.5 and PM10.
- Weather condition charts (temperature, humidity, wind, pressure).
- Full data table with scrollable view.
- AQI statistics (min, max, mean, standard deviation, variance).

#### **Single City Mode**
- Pie chart of air composition (NO₂, O₃, SO₂, CO).
- Weather conditions display.

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
