from googleplaces import GooglePlaces, types

YOUR_API_KEY = 'AIzaSyBqmCaoDZTKOtvpIcSPvGCn5_0pYIz-cD0'

google_places = GooglePlaces(YOUR_API_KEY)

# You may prefer to use the text_search API, instead.
query_result = google_places.nearby_search(
    location='London, England',
    keyword='Fish and Chips',
    radius=20000,
    types=[types.TYPE_FOOD]
)

# If types param contains only 1 item the request to Google Places API
# will be send as type param to fulfill:
# http://googlegeodevelopers.blogspot.com.au/2016/02/changes-and-quality-improvements-in_16.html

if query_result.has_attributions:
    print query_result.html_attributions

for place in query_result.places:
    # Returned places from a query are place summaries.
    print place.name
    print place.geo_location
    print place.place_id

    # The following method has to make a further API call.
    place.get_details()
    # Referencing any of the attributes below, prior to making a call to
    # get_details() will raise a googleplaces.GooglePlacesAttributeError.
    print place.details # A dict matching the JSON response from Google.
    print place.local_phone_number
    print place.international_phone_number
    print place.website
    print place.url

    # Getting place photos
    for photo in place.photos:
        # 'maxheight' or 'maxwidth' is required
        photo.get(maxheight=500, maxwidth=500)
        # MIME-type, e.g. 'image/jpeg'
        print photo.mimetype
        # Image URL
        print photo.url
        # Original filename (optional)
        print photo.filename
        # Raw image data
        print photo.data


# Are there any additional pages of results?
if query_result.has_next_page_token:
    query_result_next_page = google_places.nearby_search(
            pagetoken=query_result.next_page_token)
