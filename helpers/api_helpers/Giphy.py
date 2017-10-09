import urllib

# function to ping Giphy  api
def fetch_giphy(query):
    api_key = 'qOMNTU8uPW8fGbZlT7L1Ueu9hzXLb6QD'
    url = 'http://api.giphy.com/v1/gifs/search?q={0}&limit=1&api_key={1}'.format(query, api_key)

    # fetches with this url and returns response
    with urllib.request.urlopen(url) as response:
        data = response.read()
        return data
