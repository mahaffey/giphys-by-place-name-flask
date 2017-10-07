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
        return get_one_place(query)
    elif request.form['submit'] == 'Search for many Gifs':
        return get_many_places(query)

def curl_json_submition(request):
    # decode Byte object to JSON string then convert to JSON object
    json_data = json.loads(request.data.decode('utf8'))
    # set query from JSON data
    query = json_data['query']
    # get search request type ('one' or 'many')
    request_type = json_data['type']

    # check to see what type of search user is performing
    if request_type == 'one':
        return get_one_place(query)
    elif request_type == 'many':
        return get_many_places(query)

# method to hit google places api
def search_google_places(query):
    api_key = 'AIzaSyDoH3nXDk5CGtBpgjkmuvcCJ1U2EfEixw8'
    url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query={0}&key={1}'.format(query, api_key)

    # fetches with this url and sets response as response
    with urllib.request.urlopen(url) as response:
        data = response.read()
        return data

def get_one_place(query):
    data = search_google_places(query)
    to_json = json.loads(data)
    # create random number to select a place from places search result
    # make sure we can't go over the index size by using len
    length = len(to_json['results'])
    index = random.randrange(0,length)
    place = to_json['results'][index]

    # the code below formats all json in easy to read fashion to see printout in console
    # pretty_json = json.dumps(to_json, sort_keys=True, indent=4)
    # print(pretty_json)

    return jsonify(place)

def get_many_places(query):
    data = search_google_places(query)
    to_json = json.loads(data)
    places = to_json['results']

    # the code below formats all json in easy to read fashion to see printout in console
    # pretty_json = json.dumps(to_json, sort_keys=True, indent=4)
    # print(pretty_json)

    return jsonify(places)

def get_giphy(query):
    api_key = 'qOMNTU8uPW8fGbZlT7L1Ueu9hzXLb6QD'
    url = 'http://api.giphy.com/v1/gifs/search?q={0}&limit=3&api_key={1}'.format(query, api_key)

if __name__ == '__main__':
    app.debug = True
    # start dev server
    app.run()

# curl -H "Content-Type: application/json" -X POST -d '{"query":"pizza","type":"one"}' http://localhost:5000
