import logging
from marshmallow import Schema, fields, post_load
from .open_meteo_daily import OpenMeteoDaily

logger = logging.getLogger('appLogger')

class OpenMeteoDailySchema(Schema):
    time = fields.List(fields.Str)
    temperature_2m_min = fields.List(fields.Float())
    temperature_2m_max = fields.List(fields.Float())
    wind_speed_10m_min = fields.List(fields.Float())
    wind_speed_10m_max = fields.List(fields.Float())
    rain_sum = fields.List(fields.Float())

    @post_load
    def make_open_meteo_daily(self, data, **kwargs) -> OpenMeteoDaily:
        """Takes Open Meteo API response data in the json format and returns an OpenMeteoDaily object containing that data."""
        try:
            data_record = OpenMeteoDaily(**data)
            return data_record
        except:
            logger.info("Failure to transform data using OpenMeteoDailySchema.")