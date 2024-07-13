import datetime
from .models.weather_record import WeatherRecord
from .models.weather_prediction import WeatherPrediction
from .data_service import get_location_data
from .data_service import get_weather_data_for_location

def predict_weather(location_id: str) -> str:
    """Returns the weather prediction for the specidifed location_id"""
    locations = get_location_data()
    selected_location = locations[location_id]

    location_weather_data = get_weather_data_for_location(location_id=location_id)

    prediction = run_weather_analysis(location_name=selected_location.name, weather_data=location_weather_data)

    return str(prediction)

def run_weather_analysis(location_name: str, weather_data: list[WeatherRecord]) -> WeatherPrediction:
    """Runs an analysis on the provided weather records and returns a WeatherPrediction object"""
    min_temps = [record.temperature_min for record in weather_data]
    max_temps = [record.temperature_max for record in weather_data]
    min_wind_speeds = [record.wind_speed_min for record in weather_data]
    max_wind_speeds = [record.wind_speed_max for record in weather_data]
    rain_sums = [record.rain_sum for record in weather_data]

    estimated_temperatures = [estimated_next_float_in_list(min_temps), estimated_next_float_in_list(max_temps)]
    estimated_wind_speeds = [estimated_next_float_in_list(min_wind_speeds), estimated_next_float_in_list(max_wind_speeds)]

    estimated_min_temp = min(estimated_temperatures)
    estimated_max_temp = max(estimated_temperatures)
    estimated_min_wind_speed = min(estimated_wind_speeds)
    estimated_max_wind_speed = max(estimated_wind_speeds)
    estimated_rain_sum = estimated_next_float_in_list(rain_sums)

    return WeatherPrediction(
        location_name=location_name,
        temperature_min=estimated_min_temp,
        temperature_max=estimated_max_temp,
        wind_speed_min=estimated_min_wind_speed,
        wind_speed_max=estimated_max_wind_speed,
        rain_sum=estimated_rain_sum
    )

def estimated_next_float_in_list(float_list: list[float]) -> float:
    """Very basic estimation of the next value in a list based on the general trend over time."""
    trend = 0
    count = 0
    previous_date_min_temp = 0
    temp_difference_sum = 0
    for record in range(0, len(float_list)-1):
        current_date_min_temp = float_list[record]
        if count == 0:
            previous_date_min_temp = current_date_min_temp
            count += 1
            continue

        if current_date_min_temp > previous_date_min_temp:
            trend += 1
        elif current_date_min_temp < previous_date_min_temp:
            trend -= 1

        temp_difference_sum += current_date_min_temp - previous_date_min_temp
        previous_date_min_temp = current_date_min_temp
    
    next_value = 0
    average_temp_difference = temp_difference_sum/len(float_list)
    if trend > 0:
        next_value = previous_date_min_temp + average_temp_difference
    elif trend < 0:
        next_value = previous_date_min_temp - average_temp_difference
    else:
        next_value = previous_date_min_temp
    
    if next_value < 0:
        next_value = 0
    
    return next_value



        
    
