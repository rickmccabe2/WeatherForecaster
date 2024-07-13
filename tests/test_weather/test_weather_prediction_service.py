import unittest
from unittest.mock import patch
from src.weather.weather_prediction_service import *
from src.weather.models.location import Location


class TestWeatherPredictionService(unittest.TestCase):

    @patch('src.weather.weather_prediction_service.run_weather_analysis')
    @patch('src.weather.weather_prediction_service.get_weather_data_for_location')    
    @patch('src.weather.weather_prediction_service.get_location_data')
    def test_predict_weather_calls_expected_functions(self, mock_get_location_data, mock_get_weather_data_for_location, mock_run_weather_analysis) -> None:
        # Arrange
        location_id = "1"
        city_name = "City1"
        mock_location = Location(location_id, city_name, 123, 456)
        mock_data = {
            location_id: mock_location
        }

        mock_get_location_data.return_value = mock_data

        # Act
        _ = predict_weather(location_id)

        # Assert
        mock_get_location_data.assert_called_once()
        mock_get_weather_data_for_location.assert_called_once_with(location_id=location_id)
        mock_run_weather_analysis.assert_called_once_with(location_name=city_name, weather_data=mock_get_weather_data_for_location.return_value)


    @patch('src.weather.weather_prediction_service.run_weather_analysis')
    @patch('src.weather.weather_prediction_service.get_weather_data_for_location')    
    @patch('src.weather.weather_prediction_service.get_location_data')
    def test_predict_weather_returns_expected_result(self, mock_get_location_data, mock_get_weather_data_for_location, mock_run_weather_analysis) -> None:
        # Arrange
        location_id = "1"
        mock_prediction = WeatherPrediction(
            location_name="name",
            temperature_min=12.3,
            temperature_max=16.6,
            wind_speed_min=4.5,
            wind_speed_max=15.9,
            rain_sum=1.2
        )
        mock_run_weather_analysis.return_value = mock_prediction

        # Act
        result = predict_weather(location_id)

        # Assert
        assert result == str(mock_prediction)

