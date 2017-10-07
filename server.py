from flask import Flask
from flask import request
from flask import render_template
import urllib
import json

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def form_posting():
    place = request.form['place']
    print(place)
    return place

def search_google_places(query):
    api_key = 'AIzaSyDoH3nXDk5CGtBpgjkmuvcCJ1U2EfEixw8'
    url = 'https://maps.googleapis.com/maps/api/place/textsearch/xml?key={0}&query={1}'.format(api_key, query)
    
    data = json.loads(urllib.urlopen(url))


if __name__ == '__main__':
    app.debug = True
    app.run()
