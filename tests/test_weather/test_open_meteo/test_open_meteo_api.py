import unittest
from unittest.mock import patch
from src.weather.open_meteo.open_meteo_api import *
from src.weather.open_meteo.open_meteo_api import _build_forecast_url


class TestOpenMeteoApi(unittest.TestCase):

    @patch('src.weather.open_meteo.open_meteo_api._get_location_weather')
    @patch('src.weather.data.location_repository.get_locations')
    def test_get_meteo_weather_data_returns_expected_data(self, mock_get_locations, mock_get_location_weather) -> None:
        # Arrange done by patch  
        mock_locations = {
            "1": Location("1", "City1", 123, 456),
            "2": Location("2", "City2", 999, 444)
        }
        mock_get_locations.return_value = mock_locations

        mock_location_weather = OpenMeteoDaily(time=["2024-07-04"], temperature_2m_min=[10.7], temperature_2m_max=[17.8], wind_speed_10m_min=[11.7], wind_speed_10m_max=[27.0], rain_sum=[0.40])
        mock_get_location_weather.return_value = mock_location_weather

        # Act
        result = get_meteo_weather_data()

        # Assert
        assert mock_get_location_weather.call_count == 2
        assert len(result) == 2
        assert result["1"] == mock_location_weather
        assert result["2"] == mock_location_weather
    
    def test_build_forecast_url_returns_expected_data(self) -> None:
        # Arrange done by patch  
        latitude = 1.23
        longitude = 2.34
        domain = "https://api.open-meteo.com/"
        path = "v1/forecast"
        number_of_days = 10
        data_points = "temperature_2m_min,temperature_2m_max,wind_speed_10m_min,wind_speed_10m_max,rain_sum"
        query = f"?latitude={latitude}&longitude={longitude}&past_days={number_of_days}&daily={data_points}&forecast_days=0"
        expected_url = f"{domain}{path}{query}"

        # Act
        result = _build_forecast_url(latitude, longitude)

        # Assert
        assert result == expected_url