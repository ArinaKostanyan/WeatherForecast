# Weather Forecast Application

This is a simple command-line-based weather forecast application written in Python. It allows users to get the current weather conditions for a given location by entering a city name or ZIP code.

## Features

- Retrieve weather data for any city or ZIP code using the WeatherAPI.
- Display current temperature, weather description, humidity, and wind speed.
- Choose between Celsius and Fahrenheit for temperature display.
- Handles errors for invalid inputs or API request failures gracefully.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ArinaKostanyan/WeatherForecast.git
   cd WeatherForecast
   pip install -r requirements.txt

## Configuration

To use the WeatherAPI for fetching weather data, you'll need to set up an API key:

1. **Get an API Key**:
   - Visit [WeatherAPI](https://www.weatherapi.com/) and sign up to get your free API key.

2. **Create a `.env` File**:
   - In the root directory of the project, create a file named `.env`.

3. **Add Your API Key**:
   - Open the `.env` file and add your API key in the following format:
     ```
     WEATHER_API_KEY=your_api_key_here
     ```

4. **Ensure `.env` is Loaded**:
   - The application will automatically read the `.env` file to get your API key, so make sure it’s properly formatted and saved.

By following these steps, your application will have access to the WeatherAPI for retrieving weather data.


## Usage

1. Run the application:
    ```bash
    python weather_app.py
2. Enter a city name or ZIP code when prompted to get the weather forecast.
3. Choose the preferred temperature unit (Celsius or Fahrenheit).

## Error Handling

* If the user provides an invalid city or ZIP code, the application will display an appropriate error message.
* If the API request fails, the application will inform the user and suggest corrective actions.

