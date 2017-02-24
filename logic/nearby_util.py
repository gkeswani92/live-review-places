import geocoder

from models.database_setup import SQLAlchemyService

db = SQLAlchemyService().get_instance()


def meters_to_walking_time(meters):
    """
    Finds the walking time for the given distance
    """
    # 80 meters is one minute walking time
    if meters:
        return int(meters / 80)
    return -1


def address_to_latlng(address):
    """
    Finds the latitude and longitude of the address
    """
    g = geocoder.google(address)
    return g.lat, g.lng


