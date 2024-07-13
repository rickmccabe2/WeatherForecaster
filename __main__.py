import logging.config
from src.weather_forecasting_process import WeatherForecastingProcess

def main():
    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger('appLogger')
    process = WeatherForecastingProcess()
    try:
        process.run()
    except Exception  as e:
        logger.error("Unhandled Exception", e)
        raise


if __name__ == '__main__':
    main()