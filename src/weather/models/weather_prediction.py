import datetime

class WeatherPrediction(object):
    def __init__(
            self,
            location_name: str, 
            temperature_min: float,
            temperature_max: float, 
            wind_speed_min: float, 
            wind_speed_max: float, 
            rain_sum: float) -> None:
        self.location_name = location_name
        self.temperature_min = temperature_min
        self.temperature_max = temperature_max
        self.wind_speed_min = wind_speed_min
        self.wind_speed_max = wind_speed_max
        self.rain_sum = rain_sum

    def __str__(self) -> str:
        min_temp = "{:.2f}".format(self.temperature_min) + f"{chr(176)}C"
        max_temp = "{:.2f}".format(self.temperature_max) + f"{chr(176)}C"
        min_wind = "{:.2f}".format(self.wind_speed_min) + "km/h"
        max_wind = "{:.2f}".format(self.wind_speed_max) + "km/h"
        rain = "{:.2f}".format(self.rain_sum) + "mm"

        return (
            f"Tomorrow's weather for {self.location_name} will have a minimum temperature of {min_temp} and a maximun temperature of {max_temp}.\n"
            f"The wind speed will be between {min_wind} and {max_wind}.\n"
            f"We expect {rain} of rain."
            )