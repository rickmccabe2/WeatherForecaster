import unittest
from unittest.mock import patch
from src.weather.data_service import *


class TestDataService(unittest.TestCase):

    @patch('src.weather.data_service.insert_records')
    @patch('src.weather.data_service.transform_to_weather_records')    
    @patch('src.weather.data_service.get_meteo_weather_data')
    def test_seed_database_calls_expected_functions(self, mock_get_meteo_weather_data, mock_transform_to_weather_records, mock_insert_records) -> None:
        # Arrange done by patch  
        
        # Act
        seed_database()

        # Assert
        mock_get_meteo_weather_data.assert_called_once()
        mock_transform_to_weather_records.assert_called_once_with(meteo_data=mock_get_meteo_weather_data.return_value)
        mock_insert_records.assert_called_once_with(mock_transform_to_weather_records.return_value)
    
    
    @patch('src.weather.data_service.delete')
    def test_delete_database_calls_expected_functions(self, mock_delete) -> None:
        # Arrange done by patch  
        
        # Act
        delete_database()

        # Assert
        mock_delete.assert_called_once()

        
    @patch('src.weather.data_service.get_location_data')
    def test_get_location_list_returns_expected_data(self, mock_get_location_data) -> None:
        # Arrange
        mock_data = {
            "1": Location("1", "City1", 123, 456),
            "2": Location("2", "City2", 999, 444)
        }

        mock_get_location_data.return_value = mock_data

        # Act
        result = get_location_list()

        # Assert
        assert len(result) == 2
        assert result["1"] == "City1"
        assert result["2"] == "City2"

        
    @patch('src.weather.data_service.get_location_data')
    def test_get_locations_returns_expected_data(self, mock_get_location_data) -> None:
        # Arrange done by patch  
        

        # Act
        result = get_locations()

        # Assert
        assert result == mock_get_location_data.return_value

        
    @patch('src.weather.data_service.get_weather_data')
    def test_get_weather_data_for_location_returns_expected_data(self, mock_get_weather_data) -> None:
        # Arrange done by patch  
        location_id = "234"

        # Act
        result = get_weather_data_for_location(location_id)

        # Assert        
        mock_get_weather_data.assert_called_once_with(location_id=location_id)
        assert result == mock_get_weather_data.return_value

        
    def test_transform_to_weather_records_returns_expected_data(self) -> None:
        # Arrange
        mock_daily_record = OpenMeteoDaily(["2024-05-12","2024-05-13"],[1.2, 3.4],[3.4, 5.6],[4.3, 4.0],[2.3, 2.5],[7.3, 7.4])
        mock_data = {
            "1": mock_daily_record
        }

        # Act
        result = transform_to_weather_records(mock_data)

        # Assert
        print(len(result))
        assert len(result) == 2
        assert result[0].location_id == "1"
        assert result[0].temperature_min == mock_daily_record.temperature_2m_min[0]
        assert result[0].temperature_max == mock_daily_record.temperature_2m_max[0]
        assert result[0].wind_speed_min == mock_daily_record.wind_speed_10m_min[0]
        assert result[0].wind_speed_max == mock_daily_record.wind_speed_10m_max[0]
        assert result[0].rain_sum == mock_daily_record.rain_sum[0]

