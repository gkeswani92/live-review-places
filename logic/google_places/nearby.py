from googleplaces import GooglePlaces
from config import GOOGLE_API_KEY
from logic.nearby_util import address_to_latlng


class NearbySearchGoogle(object):

    def __init__(self):
        self.google_places = GooglePlaces(GOOGLE_API_KEY)

    def find_nearby_places(self, search_keyword, address):
        nearby_places = []
        lat, lng = address_to_latlng(address)
        query_result = self.google_places.nearby_search(
            lat_lng={
                'lat': lat,
                'lng': lng,
            },
            keyword=search_keyword,
            radius=20000,
        )

        for place in query_result.places:
            place.get_details()
            data = {
                'name': place.name,
                'id': place.place_id,
                'phone': place.local_phone_number,
                'website': place.website,
                'rating': place.details.get('rating', None),
                'price_level': place.details.get('price_level', None),
            }
            nearby_places.append(data)

        return nearby_places
