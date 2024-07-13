class Location(object):
    def __init__(self, id: str, name: str, latitude: float, longitude: float) -> None:
        self.id = id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude