# giphys-by-place-name-flask
Code Challenge using Python and Flask to find related gifs when searching for place names

### Built with:
1. Python
* Flask
* GooglePlaces api
* Giphy api


### File Structure

```
giphys-by-place-name-flask/           Top-level folder
    helpers/                          Package for api fetches and server helpers
            __init__.py               Initialize helpers package
            api_helpers               Subpackage for 3rd party api fetches
                    __init__.py       Initialize api_helpers subpackage
                    Giphy.py          Function to hit Giphy api
                    GooglePlaces.py   Function to hit GooglePlaces api
                    ...
            server_helpers            Subpackage for server helpers
                    __init__.py       Initialize server_helpers subpackage
                    get_places.py     Function to manipulate search query
                    ...
            ...
    templates/                        Views for simple front-end
            index.html                Home page
            ...
    README.md                         Readme
    server.py                         Main, run this to start server

```

### Usage and Installation


### Simple Front End


### Using Bash

##
```bash
curl -H "Content-Type: application/json" -X POST -d '{"query":"pizza","type":"one"}' http://localhost:5000


curl -H "Content-Type: application/json" -X POST -d '{"query":"tasty food in nyc","type":"many"}' http://localhost:5000
```
