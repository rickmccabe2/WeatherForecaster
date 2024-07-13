import requests
import json
import logging
from .config import open_meteo_config
from ..data.location_repository import get_locations
from ..models.location import Location
from .open_meteo_daily_schema import OpenMeteoDailySchema
from .open_meteo_daily import OpenMeteoDaily

logger = logging.getLogger('appLogger')

def get_meteo_weather_data() -> dict[str, OpenMeteoDaily]:
    """Retrieves weather data from Meteo API for all locations in the database and returns the data in a dictionary keyed on location_id"""
    locations = get_locations()
    data = dict()
    for key in locations:
        location = locations[key]
        data[key] = _get_location_weather(location=location)
    return data


def _get_location_weather(location: Location) -> OpenMeteoDaily:
    """Retrieves weather data from Meteo API for a single location as specified"""
    logger.info("Retrieving data from Meteo API")
    url = _build_forecast_url(latitude=location.latitude, longitude=location.longitude)
    response = requests.get(url)

    required_json = json.loads(response.text)["daily"]

    schema = OpenMeteoDailySchema()
    result = schema.load(required_json)
    logger.info("Successfully retrieved data from Meteo API")
    return result


def _build_forecast_url(latitude: float, longitude: float) -> str:
    """Builds up the URL in a format expected by the Meteo API"""
    number_of_days = 10
    data_points = "temperature_2m_min,temperature_2m_max,wind_speed_10m_min,wind_speed_10m_max,rain_sum"
    query = f"?latitude={latitude}&longitude={longitude}&past_days={number_of_days}&daily={data_points}&forecast_days=0" #this api can do forecasting but we don't want that in this project.

    url = f"{open_meteo_config["domain"]}{open_meteo_config["forecast_path"]}{query}" 
    
    return url