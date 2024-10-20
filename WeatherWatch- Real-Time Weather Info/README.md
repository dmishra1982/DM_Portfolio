# WeatherWatch - Real-Time Weather Info

## Project Overview
<p align="justify">
This Python project leverages the OpenWeatherMap API to fetch and display current weather information based on user input. It supports weather lookup via Zip Code or City Name and State Code combination. Additionally, users can choose temperature units (Fahrenheit, Celsius, or Kelvin) for displaying weather details.
</p>

## Table of Contents
1. [Project Overview](#project-overview)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Data](#data)
5. [Source Data](#source-data)
6. [Results](#results)
7. [Future Work](#future-work)
8. [Contributing](#contributing)
9. [Acknowledgments](#acknowledgments)

## Installation

To run this project, follow the steps below:

1. **Ensure Python 3.8 or above** is installed. You can download it from [python.org](https://www.python.org/downloads/).
2. **Install PyCharm** (recommended IDE for development) or another preferred IDE.
3. **Install the required Python packages**: If the import step fails, install any missing packages using `pip install`.

## Usage

To use the Weather App, follow these steps:

1. **Run the application** from your IDE or command line.
2. Choose from the following options:
   - Enter `1` to lookup weather by **Zip Code**.
   - Enter `2` to lookup weather by **City Name** and **State Code**.
   - Enter `3` to **exit** the application.
3. **Follow the prompts** to enter the required information (Zip Code, City Name, State Code).
4. **Select temperature units** (F, C, K) when prompted to view weather details in Fahrenheit, Celsius, or Kelvin.
5. The application will display current weather conditions such as temperature, pressure, humidity, cloud cover, and more.

## Data

The weather data is fetched in real-time from the **OpenWeatherMap API**. The data includes:
- Temperature (current, minimum, and maximum)
- Pressure
- Humidity
- Cloud cover description
- City and country name

### Source Data

Ensure you replace the `<api_key>` in the `weather_app.py` file with your **OpenWeatherMap API key**. You can obtain this API key by signing up at [OpenWeatherMap API](https://openweathermap.org/api).

## Results

The application provides real-time, accurate weather information based on the user's input. It supports:
- **Multiple temperature units** (Fahrenheit, Celsius, Kelvin)
- Comprehensive weather details including:
   - Current temperature, pressure, and humidity
   - Minimum and maximum temperatures
   - Cloud cover description
   - Location details (city and country)

## Future Work

Potential improvements for future versions include:
- Adding a **graphical user interface (GUI)** for enhanced user interaction.
- Allowing users to **save favorite locations** for easy access.
- **Weather forecasting** for upcoming days.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with any proposed changes or enhancements.

## Acknowledgments

Special thanks to:
- **Python** community for the amazing libraries used in this project.
- **OpenWeatherMap** for providing access to their API.

