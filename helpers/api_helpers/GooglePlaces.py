import urllib

# function to ping GooglePlaces api
def fetch_google_places(query):
    api_key = 'AIzaSyDoH3nXDk5CGtBpgjkmuvcCJ1U2EfEixw8'
    url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query={0}&key={1}'.format(query, api_key)

    # fetches with this url and returns response
    with urllib.request.urlopen(url) as response:
        data = response.read()
        return data
