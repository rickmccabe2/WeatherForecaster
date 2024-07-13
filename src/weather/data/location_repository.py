# mock of data retrieval from a database
import logging
from ..models.location import Location

logger = logging.getLogger('appLogger')

def get_locations() -> dict[str, Location]:
    """Returns a dictionary of Location data keyed on location id"""
    logger.info("Retrieving locations from database.")
    locations = []
    locations.append(
        Location(
            id="1",
            name="Manchester",
            latitude=53.479101,
            longitude=-2.244424
        ))
    locations.append(    
        Location(
            id="2",
            name="London",
            latitude=51.490911,
            longitude=-0.126880 
        ))
    
    location_dictionary = dict()
    for location in locations:
        location_dictionary[location.id] = location
    
    logger.info("Successfully retrieved locations.")

    return location_dictionary