import logging
from .open_meteo.open_meteo_api import get_meteo_weather_data
from .models.weather_record import WeatherRecord
from .open_meteo.open_meteo_daily import OpenMeteoDaily
from .data.weather_repository import insert_records
from .data.weather_repository import delete_database as delete
from .data.weather_repository import get_weather_data
from .data.location_repository import Location
from .data.location_repository import get_locations  as get_location_data

logger = logging.getLogger('appLogger')

def seed_database() -> None:
    # Populate an empty database with data from the meteo API
    meteo_data = get_meteo_weather_data()
    transformed_data = transform_to_weather_records(meteo_data=meteo_data)
    insert_records(transformed_data)

def transform_to_weather_records(meteo_data: dict[str, OpenMeteoDaily]) -> list[WeatherRecord]:
    """Transform Meteo data into a structure which can be used by the rest of the process"""
    logger.info("Transforming Open Meteo data to weather records.")
    weather_records = []
    for location in meteo_data:
        count = 0
        while count < len(meteo_data[location].time):
            weather_records.append(
                WeatherRecord(
                    location_id = location,
                    date = meteo_data[location].time[count],
                    temperature_min = meteo_data[location].temperature_2m_min[count],
                    temperature_max = meteo_data[location].temperature_2m_max[count],
                    wind_speed_min = meteo_data[location].wind_speed_10m_min[count],
                    wind_speed_max = meteo_data[location].wind_speed_10m_max[count],
                    rain_sum = meteo_data[location].rain_sum[count]                    
                ))
            count += 1
    
    logger.info("Transformation complete.")
    return weather_records


def delete_database() -> None:
    """Delete database completely"""
    delete()

def get_location_list() -> dict[str, str]:
    """Returns the location name data in a dictionary keyed on location_id"""
    locations = get_location_data()
    location_list = dict()
    for location in locations:
        location_list[location] = locations[location].name
    
    return location_list

def get_locations() -> dict[str, Location]:
    """Returns the full set of location data in a dictionary keyed on location_id"""
    return get_location_data()

def get_weather_data_for_location(location_id: str) -> list[WeatherRecord]:
    """Returns the WeatherRecords for the specified location_id"""
    return get_weather_data(location_id=location_id)