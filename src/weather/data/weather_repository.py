# mock of data create/read to/from a database
import os
import csv
import logging
from ..models.weather_record import WeatherRecord

logger = logging.getLogger('appLogger')
_full_file_path = "src/weather/data/WeatherRecords.csv"

def insert_records(records: list[WeatherRecord]) -> None:
    """Insert list of weather records into database"""
    logger.info("Inserting records into database.")
    try:
        file = open(file=_full_file_path, mode="x")
    except FileExistsError:
        logger.error("Trying to seed a database which has already been seeded.")
        print("Data already seeded.")
        raise
    
    # write headers
    file.write("location_id,date,temperature_2m_min,temperature_2m_max,wind_speed_10m_min,wind_speed_10m_max,rain_sum")

    # write records
    for record in records:
        file.write(f"\n{record.location_id},{record.date},{record.temperature_min},{record.temperature_max},{record.wind_speed_min},{record.wind_speed_max},{record.rain_sum}")

    file.close
    logger.info("Successfully inserted records into database.")

def delete_database() -> None:
    """Completely delete database"""
    if os.path.isfile(_full_file_path):
        os.remove(_full_file_path)


def get_weather_data(location_id: str) -> list[WeatherRecord]:
    """get all weather data for a single location specified by location_id"""
    logger.info("Retrieving records from database.")
    records = list()
    with open(file=_full_file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # do nothing - header row
                line_count += 1
            elif row[0] == location_id:
                records.append(
                    WeatherRecord(
                        location_id=row[0],
                        date=row[1],
                        temperature_min=float(row[2]),
                        temperature_max=float(row[3]),
                        wind_speed_min=float(row[4]),
                        wind_speed_max=float(row[5]),
                        rain_sum=float(row[6])
                    )
                )
                line_count += 1
    
    logger.info("Successfully retrieved records from database.")
    return records