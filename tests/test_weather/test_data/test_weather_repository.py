import unittest
from unittest.mock import patch, mock_open
from src.weather.data.weather_repository import *


class TestWeatherRespository(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="data")
    def test_insert_records_calls_expected_functions(self, mock_file) -> None:
        # Arrange done by patch
        records = [WeatherRecord(
                        location_id="1",
                        date="2024-07-05",
                        temperature_min=1.2,
                        temperature_max=2.4,
                        wind_speed_min=3.5,
                        wind_speed_max=3.5,
                        rain_sum=1.1
                    )]

        full_file_path = "src/weather/data/WeatherRecords.csv"

        # Act
        insert_records(records)

        # Assert
        mock_file.assert_called_once_with(file=full_file_path, mode="x")
        mock_file().write.call_count == 2
        mock_file().write.assert_any_call("location_id,date,temperature_2m_min,temperature_2m_max,wind_speed_10m_min,wind_speed_10m_max,rain_sum")
        mock_file().write.assert_any_call("\n1,2024-07-05,1.2,2.4,3.5,3.5,1.1")