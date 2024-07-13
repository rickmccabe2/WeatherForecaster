import datetime

class OpenMeteoDaily:
    def __init__(
            self, 
            time: list[datetime.datetime], 
            temperature_2m_min: list[float], 
            temperature_2m_max: list[float], 
            wind_speed_10m_min: list[float], 
            wind_speed_10m_max: list[float], 
            rain_sum: list[float]) -> None:
        self.time = time
        self.temperature_2m_min = temperature_2m_min
        self.temperature_2m_max = temperature_2m_max
        self.wind_speed_10m_min = wind_speed_10m_min
        self.wind_speed_10m_max = wind_speed_10m_max
        self.rain_sum = rain_sum