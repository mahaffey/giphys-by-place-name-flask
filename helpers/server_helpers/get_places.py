from helpers.api_helpers.Giphy import fetch_giphy
from helpers.api_helpers.GooglePlaces import fetch_google_places
from flask import jsonify
import json
import random

# helper function to format JSON and to call GooglePlaces and Giphy functions
def get_places(query, search_type):
    encoded_query = '+'.join(query.split()).encode('utf-8').strip()
    data = fetch_google_places(encoded_query)
    to_json = json.loads(data)
    places = to_json['results']

    # check what type of search user is performing
    if search_type == 'one':
        # get 'random' place from search query (max 20 results)
        length = len(places)
        index = random.randrange(0,length)
        place = places[index]

        # name of place used to ping giphy api
        name = place['name']
        encoded_name = '+'.join(name.split()).encode('utf-8').strip()

        # calls fetch_giphy function
        giphy_data = json.loads(fetch_giphy(encoded_name))
        place['giphy'] = giphy_data
        return jsonify(place)

    elif search_type == 'many':
        for place in places:
            # name of place used to ping giphy api
            name = place['name']
            encoded_name = '+'.join(name.split()).encode('utf-8').strip()

            # calls fetch_giphy function
            giphy_data = json.loads(fetch_giphy(encoded_name))
            place['giphy'] = giphy_data

        return jsonify(places)
