import json
from unittest import TestCase

import geocoder
import urllib2

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


class NearbyWikipedia(object):

    @staticmethod
    def wiki_path(place):
        """
        Creates the wikipedia link for the place
        """
        return urllib2.urlparse.urljoin("http://en.wikipedia.org/wiki/", place.replace(' ', '_'))

    @staticmethod
    def find_nearby_places(address):
        """
        Finds near by places for the given address by using wikipedia's api
        :param address:
        :return:
        """
        latitude, longitude = address_to_latlng(address)

        api_url = 'https://en.wikipedia.org/w/api.php?action=query&list=geosearch&gsradius=5000&gscoord={0}%7C{1}&gslimit=20&format=json'
        query_url = api_url.format(latitude, longitude)

        query = urllib2.urlopen(query_url)
        results = query.read()
        query.close()

        data = json.loads(results)

        places = []
        for place in data['query']['geosearch']:
            name = place['title']
            meters = place['dist']
            latitude = place['lat']
            longitude = place['lon']

            wiki_url = NearbyWikipedia.wiki_path(name)
            walking_time = meters_to_walking_time(meters)

            place_info = {
                'name': name,
                'url': wiki_url,
                'time': walking_time,
                'latitude': latitude,
                'longitude': longitude
            }

            places.append(place_info)

        return places



