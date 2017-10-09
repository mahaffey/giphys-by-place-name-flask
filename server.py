from flask import Flask, request, render_template, jsonify
from helpers.server_helpers.get_places import get_places
import json

# initialize app variable using the __name__ attribute
app = Flask(__name__)

# set routes and the functions called when server is pinged at these routes
# decorator calls this function when at this route
@app.route('/')
def initialize_home_page():
    return render_template('index.html')

# gets search query from html form or cURL script using request from Flask
@app.route('/', methods=['POST'])
def form_posting():
    # check to see if request is coming from the HTML form or cURL script
    if request.form: # HTML form
        return web_page_form_submition(request)

    elif request.data: # cURL JSON
        return cURL_json_submition(request)

# helper functions to call get_places function with proper parameters
# if request is from web form
def web_page_form_submition(request):
    # set query from form data
    query = request.form['query']

    # check to see what type of search user is performing
    if request.form['submit'] == 'Search for a Gif':
        return get_places(query, 'one')
    elif request.form['submit'] == 'Search for many Gifs':
        return get_places(query, 'many')

# if request is from cURL script
def cURL_json_submition(request):
    # decode Byte object to JSON string then convert to JSON object
    json_data = json.loads(request.data.decode('utf-8'))
    # set query from JSON data
    query = json_data['query']
    # get search request type (should be 'one' or 'many')
    request_type = json_data['type']

    # throw user an error if request type is not either 'one' or 'many'
    if request_type == 'one' or request_type == 'many':
        return get_places(query, request_type)
    else:
        return '\n\nERROR: The "type" attribute in your JSON POST request may only be either "one" or "many". Please try again.\n\n\n'

# starts dev server if on path
if __name__ == '__main__':
    app.debug = True
    app.run()
