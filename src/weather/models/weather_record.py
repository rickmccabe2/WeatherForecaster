import datetime

class WeatherRecord(object):
    def __init__(
            self,
            location_id: str, 
            date: datetime.datetime, 
            temperature_min: float,
            temperature_max: float, 
            wind_speed_min: float, 
            wind_speed_max: float, 
            rain_sum: float) -> None:
        self.location_id = location_id
        self.date = date
        self.temperature_min = temperature_min
        self.temperature_max = temperature_max
        self.wind_speed_min = wind_speed_min
        self.wind_speed_max = wind_speed_max
        self.rain_sum = rain_sum
