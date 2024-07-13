import logging
from .process_base import ProcessBase
from .constants.titles import main_title
from .weather.data_service import seed_database
from .weather.data_service import delete_database
from .weather.data_service import get_location_list
from .weather.weather_prediction_service import predict_weather
from .output.file_writer import write_to_file

logger = logging.getLogger('appLogger')

class WeatherForecastingProcess(ProcessBase):

    def __init__(self) -> None:
        super().__init__()
        self._user_options = {
            "1": {
                    "description": "Seed Database",
                    "function":  self._seed_database
            },
            "2": {
                    "description": "Delete Database",
                    "function":  self._delete_database
            },
            "3": {
                    "description": "Predict Weather",
                    "function":  self._predict_weather
            },
            "q": {
                    "description": "Quit"
            }
        }


    def run(self) -> None:
        """Entry point for process."""
        print(main_title)
        request_user_input = True
        while request_user_input:
            self._display_main_menu()
            user_choice = input("Please select an option from the list: ").lower()
            
            #validate
            if user_choice not in self._user_options:
                print("Invalid option, please choose again.")
                continue
            
            #end process
            if user_choice == "q":
                request_user_input = False
                break

            #execute selected function
            self._user_options[user_choice]["function"]()

    
    def _seed_database(self) -> None:
        """Populate an empty weather database with data"""
        logger.info("Starting database seeding.")
        seed_database()
        logger.info("Database seeded successfully.")
        print("Seeding complete")

    
    def _delete_database(self) -> None:
        """Delete database completely"""
        logger.info("Starting database deletion.")
        delete_database()
        logger.info("Database deleted successfully.")
        print("Database deleted")


    def _predict_weather(self) -> None:
        """Predict weather using parameters entered by user at runtime"""
        logger.info("Starting weather prediction process.")
        locations = get_location_list()
        for location in locations:
            print(f"{location} - {locations[location]}")
        selected_location = input("Please select a location from the list: ")
        weather_prediction = predict_weather(location_id = selected_location)
        print(weather_prediction)
        #write to file
        filepath = write_to_file(weather_prediction)
        print(f"Weather predition also written to {filepath}")
        logger.info("Completed weather prediction process.")

        
    def _display_main_menu(self) -> None:
        """Displays the main menu items to the user"""
        print()
        for option in self._user_options:
            print(f"{option} - {self._user_options[option]["description"]}")
        print()


    