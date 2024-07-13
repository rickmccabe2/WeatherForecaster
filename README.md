# Weather Forcaster

## Summary

This application can be used to predict tomorrow's weather in a select set of locations:

1. Manchester
1. London

The application uses data from the open-source weather API [Open Meteo](https://open-meteo.com/). *Open Meteo has the capability to predict the weather, but we have intentionally disregarded this feature for the purposes of this application*.


> Open-Meteo partners with national weather services to bring you open data with high resolution, ranging from 1 to 11 kilometers. Our powerful APIs intelligently select the most suitable weather models for your specific location, ensuring accurate and reliable forecasts.

The data from Open Meteo is used to determine a pattern in historical weather data to build up a prediction of tomorrow's weather.

**Calls to Open Meteo do not need authenticating. This application will run without having to set up an account or generate an API key.**


## Set up

- If you don't already have Python installed, you can download the latest version for Windows from the official site [python.org](https://www.python.org/downloads/)

- Clone this repo to your local machine and using your favour CLI cd into the root directory

- Create a new virtual environment and activate it using the CLI commands below:

```
python -m venv env

source env/Scripts/activate
```

- Install the require packages as listed in the requirements.txt file using the command below:

```
pip install -r requirements.txt
```
## Unit Tests
Unit tests use the [unittest](https://docs.python.org/3/library/unittest.html) testing framework and the [unittest.mock](https://docs.python.org/3/library/unittest.mock.html) object library.

In your CLI, enter the following command to run the unit tests for the entire solution:

```
py -m unittest
```
You should see a confirmation that all tests ran successfully:
> Ran 11 tests in 0.013s  
> OK



 
## Running the Application
In the following text, the term "database" is used but in reality we're mocking database functionality by using a csv file for the weather data and an in memory data structure for the location data.

Activate your virtual environment and run the application by running the following commands:

```
source env/Scripts/activate

py __main__.py
```
You will be greeted with the main menu which contains the following options. Input the number of the option you wish to select, or `q` to quit.

> **1 - Seed Database** *Use this option if it's the first run - the "database" will be seeded with 10 days worth of data for London and Manchester*  
**2 - Delete Database** *This option will delete all of the seeded data should you need to start again*  
**3 - Predict Weather** *Select this option and you'll be presented with a list of locations you can get weather predictions for*  
**q - Quit** *Select this option to quit the application*



## Logging
Application logging is configured in the `logging.conf` file which is located in the root directory.

In the default set up, the majority of the logs will appear in the app.log file, this is to reduce noise in the console which is used for user interaction. Exceptions will however, also be displayed in the console.

Example of logging:

> 2024-07-14 18:45:06 - appLogger - INFO - Transformation complete.  
2024-07-14 18:45:06 - appLogger - INFO - Inserting records into database.  
2024-07-14 18:45:06 - appLogger - ERROR - Trying to seed a database which has already been seeded.


