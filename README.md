# Weather Application

This project is a weather forecasting web application built with Django and the OpenWeatherMap API. Users can input a city name to retrieve current weather information, including temperature, weather description, and more. The app also supports displaying error messages for invalid cities.

## Features

- **Search Weather by City**: Users can input any city name to get real-time weather details.
- **Weather Data Display**:
  - Temperature (in Celsius).
  - Weather description (e.g., "clear sky").
  - Weather icon.
  - Current time of the searched city.
- **Error Handling**: Displays a notification when the user enters an invalid city name.
- **Responsive Design**: The user interface is styled using the Bulma CSS framework for responsiveness and aesthetics.

## Technologies Used

### Backend
- **Django**: Python-based web framework used for handling server-side logic.
- **OpenWeatherMap API**: Third-party API used to fetch weather data.

### Frontend
- **Bulma CSS Framework**: For responsive and clean UI design.
- **HTML**: To structure the application.

## Prerequisites

1. Python 3.6 or higher installed on your system.
2. API Key from [OpenWeatherMap](https://openweathermap.org/).
3. Basic knowledge of Django and Python.

## Installation Guide

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd weather-app
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   Create a `.env` file in the project root directory and add your OpenWeatherMap API key:
   ```
   OPENWEATHER_API_KEY=your_api_key_here
   ```

5. **Run Database Migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Run the Server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**:
   Open your browser and navigate to `http://127.0.0.1:8000`.

## Usage

1. Enter a city name in the input field and click "إضافة المدينة" ("Add City").
2. The weather details of the city will be displayed.
3. If an invalid city is entered, an error notification will appear.

## Project Structure

- `weatherapi/views.py`: Contains the logic for fetching and displaying weather data.
- `templates/weatherapi/index.html`: The main HTML template for the user interface.
- `static/`: Contains static files like CSS, JS, and images.

## API Usage

The application uses the OpenWeatherMap API for retrieving weather data. Example API request:
```
https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric
```

## Example Response
```json
{
  "coord": {"lon": 31.2497, "lat": 30.0626},
  "weather": [{"id": 800, "main": "Clear", "description": "clear sky", "icon": "01d"}],
  "main": {"temp": 25, "humidity": 50},
  "wind": {"speed": 3.1},
  "name": "Cairo"
}
```

## Future Enhancements

- **Multi-language Support**: Allow users to view weather descriptions in various languages.
- **Forecasting**: Add a feature to display 7-day weather forecasts.
- **Map Integration**: Display the searched city on an interactive map.

## Author

- **Name**: Mahmoud Siad
- **Contact**: +201028006657

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Feel free to contribute to the project or raise issues if you encounter any problems!

