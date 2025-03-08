import pandas as pd
import matplotlib.pyplot as plt

# Generate sample weather data
data = {
    "Date": pd.date_range(start="2024-01-01", periods=30, freq='D'),
    "Temperature": [round(20 + (i % 5) * 1.5, 1) for i in range(30)],
    "Humidity": [round(50 + (i % 3) * 3, 1) for i in range(30)],
    "Pressure": [round(1010 + (i % 4) * 2, 1) for i in range(30)]
}
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("weather_data.csv", index=False)

# Read the dataset
df = pd.read_csv("weather_data.csv", parse_dates=["Date"])

# Basic statistics
print("Average Temperature:", df["Temperature"].mean())
print("Average Humidity:", df["Humidity"].mean())
print("Average Pressure:", df["Pressure"].mean())

# Visualization
def plot_weather_data():
    plt.figure(figsize=(10, 5))
    plt.plot(df["Date"], df["Temperature"], label="Temperature (°C)", marker='o')
    plt.plot(df["Date"], df["Humidity"], label="Humidity (%)", marker='s')
    plt.plot(df["Date"], df["Pressure"], label="Pressure (hPa)", marker='^')
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.title("Weather Trends Over Time")
    plt.legend()
    plt.grid()
    plt.show()

plot_weather_data()