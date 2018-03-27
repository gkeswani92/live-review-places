import json
import urllib3

from logic.nearby_util import address_to_latlng
from logic.nearby_util import meters_to_walking_time


class NearbySearchWikipedia(object):

    @staticmethod
    def wiki_path(place):
        """
        Creates the wikipedia link for the place
        """
        return urllib3.urlparse.urljoin("http://en.wikipedia.org/wiki/", place.replace(' ', '_'))

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

        query = urllib3.urlopen(query_url)
        results = query.read()
        query.close()

        data = json.loads(results)

        places = []
        for place in data['query']['geosearch']:
            name = place['title']
            meters = place['dist']
            latitude = place['lat']
            longitude = place['lon']

            wiki_url = NearbySearchWikipedia.wiki_path(name)
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
