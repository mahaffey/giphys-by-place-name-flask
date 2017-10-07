from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
import urllib
import json
import random
from IPython import embed

# initialize app variable using the __name__ attribute
app = Flask(__name__)

#################################################################
# set routes
#################################################################

# decorator to call this method when at this route
@app.route('/')
def home_page():
    return render_template('index.html')

# gets search query from html form using request module from Flask
@app.route('/', methods=['POST'])
def form_posting():
    # check to see if request is coming from HTML form or cURL
    if request.form: # HTML form
        return web_page_form_submition(request)

    elif request.data: # cURL JSON
        return curl_json_submition(request)

#################################################################
# helper methods
#################################################################
def web_page_form_submition(request):
    # set query from form data
    query = request.form['query']

    # check to see what type of search user is performing
    if request.form['submit'] == 'Search for a Gif':
        return get_places(query, 'one')
    elif request.form['submit'] == 'Search for many Gifs':
        return get_places(query, 'many')

def curl_json_submition(request):
    # decode Byte object to JSON string then convert to JSON object
    json_data = json.loads(request.data.decode('utf-8'))
    # set query from JSON data
    query = json_data['query']
    # get search request type ('one' or 'many')
    request_type = json_data['type']

    return get_places(query, request_type)


# method to hit google places api
def fetch_google_places_api(query):
    api_key = 'AIzaSyDoH3nXDk5CGtBpgjkmuvcCJ1U2EfEixw8'
    url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query={0}&key={1}'.format(query, api_key)
    # embed()
    # fetches with this url and sets response as response
    with urllib.request.urlopen(url) as response:
        data = response.read()
        return data

def get_places(query, search_type):
    encoded_query = '+'.join(query.split()).encode('utf-8').strip()
    data = fetch_google_places_api(encoded_query)
    to_json = json.loads(data)
    results = to_json['results']

    # check what type of search user is performing
    if search_type == 'one':
        length = len(results)
        index = random.randrange(0,length)
        place = results[index]
        name = place['name']
        encoded_name = '+'.join(name.split()).encode('utf-8').strip()

        giphy_data = json.loads(fetch_giphy(encoded_name))
        place['giphy'] = giphy_data
        return jsonify(place)

    elif search_type == 'many':
        places = results
        for place in places:
            name = place['name']
            encoded_name = '+'.join(name.split()).encode('utf-8').strip()
            
            giphy_data = json.loads(fetch_giphy(encoded_name))
            place['giphy'] = giphy_data

        return jsonify(places)

def fetch_giphy(query):
    api_key = 'qOMNTU8uPW8fGbZlT7L1Ueu9hzXLb6QD'
    url = 'http://api.giphy.com/v1/gifs/search?q={0}&limit=1&api_key={1}'.format(query, api_key)

    # fetches with this url and sets response as response
    with urllib.request.urlopen(url) as response:
        data = response.read()
        return data

if __name__ == '__main__':
    app.debug = True
    # start dev server
    app.run()

# curl -H "Content-Type: application/json" -X POST -d '{"query":"pizza","type":"one"}' http://localhost:5000
