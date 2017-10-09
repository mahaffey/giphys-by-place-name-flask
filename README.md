# giphys-by-place-name-flask
Code Challenge using Python and Flask to find related gifs when searching for place names

## Disclaimer
Yes I left my API keys intact in their respective files. This is for easy code review/start up, they will be deactivated after some time.

### Built with:
1. Python 3
2. Flask
3. GooglePlaces api
4. Giphy api

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

### Installation
User must have Python 3 and Flask installed.

### Usage
1. Navigate to project root folder.
2. In terminal:
  ```bash
  > giphys-by-place-name-flask
  $ python3 server.py
  ```
3. From here, the user has two options

#### Simple Front End Form
1. Navigate to localhost:5000
2. Fill out form with a place name, ie "pizza in New Orleans"
3. Click either
    * "Search for one" (will return JSON response of one place with associated gif)
    * "Search for many" (will return JSON response of up to twenty places with their associated gifs)
4. The JSON response will show in your browser (a JSON viewer is recommended)

#### Using cURL with BASH
1. In terminal type in your cURL command and the response should follow.
2. For the "type" attribute only "one" or "many" will work, otherwise an error message will display.
    * "one" (will return JSON response of one place with associated gif)
    * "many" (will return JSON response of up to twenty places with their associated gifs)

```bash
curl -H "Content-Type: application/json" -X POST -d '{"query":"pizza","type":"one"}' http://localhost:5000


curl -H "Content-Type: application/json" -X POST -d '{"query":"tasty food in nyc","type":"many"}' http://localhost:5000
```

### Example JSON Output for cURL request

```bash
curl -H "Content-Type: application/json" -X POST -d '{"query":"pizza","type":"one"}' http://localhost:5000

{
  "formatted_address": "23 S Haddon Ave, Haddonfield, NJ 08033, United States",
  "geometry": {
    "location": {
      "lat": 39.8977566,
      "lng": -75.0309193
    },
    "viewport": {
      "northeast": {
        "lat": 39.8990590302915,
        "lng": -75.02963696970849
      },
      "southwest": {
        "lat": 39.8963610697085,
        "lng": -75.0323349302915
      }
    }
  },
  "giphy": {
    "data": [
      {
        "bitly_gif_url": "http://gph.is/2dtg7T2",
        "bitly_url": "http://gph.is/2dtg7T2",
        "content_url": "",
        "embed_url": "https://giphy.com/embed/YPlmbMKmn8nUA",
        "id": "YPlmbMKmn8nUA",
        "images": {
          "480w_still": {
            "height": "480",
            "url": "https://media2.giphy.com/media/YPlmbMKmn8nUA/480w_s.jpg",
            "width": "480"
          },
          "downsized": {
            "height": "360",
            "size": "1670492",
            "url": "https://media0.giphy.com/media/YPlmbMKmn8nUA/giphy-downsized.gif",
            "width": "360"
          },
          "downsized_large": {
            "height": "360",
            "size": "1670492",
            "url": "https://media0.giphy.com/media/YPlmbMKmn8nUA/giphy.gif",
            "width": "360"
          },
          "downsized_medium": {
            "height": "360",
            "size": "1670492",
            "url": "https://media0.giphy.com/media/YPlmbMKmn8nUA/giphy.gif",
            "width": "360"
          },
          "downsized_small": {
            "height": "180",
            "mp4": "https://media0.giphy.com/media/YPlmbMKmn8nUA/giphy-downsized-small.mp4",
            "mp4_size": "93674",
            "width": "180"
          },
          "downsized_still": {
            "height": "360",
            "size": "49876",
            "url": "https://media0.giphy.com/media/YPlmbMKmn8nUA/giphy-downsized_s.gif",
            "width": "360"
          },
          "fixed_height": {
            "height": "200",
            "mp4": "https://media0.giphy.com/media/YPlmbMKmn8nUA/200.mp4",
            "mp4_size": "90487",
            "size": "509345",
            "url": "https://media0.giphy.com/media/YPlmbMKmn8nUA/200.gif",
            "webp": "https://media0.giphy.com/media/YPlmbMKmn8nUA/200.webp",
            "webp_size": "609668",
            "width": "200"
          },
          "fixed_height_downsampled": {
            "height": "200",
            "size": "87064",
            "url": "https://media0.giphy.com/media/YPlmbMKmn8nUA/200_d.gif",
            "webp": "https://media0.giphy.com/media/YPlmbMKmn8nUA/200_d.webp",
            "webp_size": "87158",
            "width": "200"
          },
          "fixed_height_small": {
            "height": "100",
            "mp4": "https://media0.giphy.com/media/YPlmbMKmn8nUA/100.mp4",
            "mp4_size": "33585",
            "size": "150425",
            "url": "https://media0.giphy.com/media/YPlmbMKmn8nUA/100.gif",
            "webp": "https://media0.giphy.com/media/YPlmbMKmn8nUA/100.webp",
            "webp_size": "189928",
            "width": "100"
          },
          "fixed_height_small_still": {
            "height": "100",
            "size": "5065",
            "url": "https://media0.giphy.com/media/YPlmbMKmn8nUA/100_s.gif",
            "width": "100"
          },
          "fixed_height_still": {
            "height": "200",
            "size": "15889",
            "url": "https://media0.giphy.com/media/YPlmbMKmn8nUA/200_s.gif",
            "width": "200"
          },
          "fixed_width": {
            "height": "200",
            "mp4": "https://media0.giphy.com/media/YPlmbMKmn8nUA/200w.mp4",
            "mp4_size": "90487",
            "size": "509345",
            "url": "https://media0.giphy.com/media/YPlmbMKmn8nUA/200w.gif",
            "webp": "https://media0.giphy.com/media/YPlmbMKmn8nUA/200w.webp",
            "webp_size": "609668",
            "width": "200"
          },
          "fixed_width_downsampled": {
            "height": "200",
            "size": "87064",
            "url": "https://media0.giphy.com/media/YPlmbMKmn8nUA/200w_d.gif",
            "webp": "https://media0.giphy.com/media/YPlmbMKmn8nUA/200w_d.webp",
            "webp_size": "87158",
            "width": "200"
          },
          "fixed_width_small": {
            "height": "100",
            "mp4": "https://media0.giphy.com/media/YPlmbMKmn8nUA/100w.mp4",
            "mp4_size": "33585",
            "size": "150425",
            "url": "https://media0.giphy.com/media/YPlmbMKmn8nUA/100w.gif",
            "webp": "https://media0.giphy.com/media/YPlmbMKmn8nUA/100w.webp",
            "webp_size": "189928",
            "width": "100"
          },
          "fixed_width_small_still": {
            "height": "100",
            "size": "5065",
            "url": "https://media0.giphy.com/media/YPlmbMKmn8nUA/100w_s.gif",
            "width": "100"
          },
          "fixed_width_still": {
            "height": "200",
            "size": "15889",
            "url": "https://media0.giphy.com/media/YPlmbMKmn8nUA/200w_s.gif",
            "width": "200"
          },
          "looping": {
            "mp4": "https://media0.giphy.com/media/YPlmbMKmn8nUA/giphy-loop.mp4",
            "mp4_size": "2445503"
          },
          "original": {
            "frames": "43",
            "hash": "8b11c3e1ee52bdd7db9984e29a45d995",
            "height": "360",
            "mp4": "https://media0.giphy.com/media/YPlmbMKmn8nUA/giphy.mp4",
            "mp4_size": "778832",
            "size": "1670492",
            "url": "https://media0.giphy.com/media/YPlmbMKmn8nUA/giphy.gif",
            "webp": "https://media0.giphy.com/media/YPlmbMKmn8nUA/giphy.webp",
            "webp_size": "2030974",
            "width": "360"
          },
          "original_mp4": {
            "height": "480",
            "mp4": "https://media0.giphy.com/media/YPlmbMKmn8nUA/giphy.mp4",
            "mp4_size": "778832",
            "width": "480"
          },
          "original_still": {
            "height": "360",
            "size": "49876",
            "url": "https://media0.giphy.com/media/YPlmbMKmn8nUA/giphy_s.gif",
            "width": "360"
          },
          "preview": {
            "height": "150",
            "mp4": "https://media0.giphy.com/media/YPlmbMKmn8nUA/giphy-preview.mp4",
            "mp4_size": "44053",
            "width": "150"
          },
          "preview_gif": {
            "height": "130",
            "size": "49887",
            "url": "https://media0.giphy.com/media/YPlmbMKmn8nUA/giphy-preview.gif",
            "width": "130"
          },
          "preview_webp": {
            "height": "138",
            "size": "49158",
            "url": "https://media0.giphy.com/media/YPlmbMKmn8nUA/giphy-preview.webp",
            "width": "138"
          }
        },
        "import_datetime": "2016-09-26 11:49:55",
        "is_indexable": 0,
        "rating": "r",
        "slug": "bs-YPlmbMKmn8nUA",
        "source": "https://www.tacomaworld.com/threads/locos-brack-burrito-build-bs-thread-with-some-build-mostly-bs.376639/page-160",
        "source_post_url": "https://www.tacomaworld.com/threads/locos-brack-burrito-build-bs-thread-with-some-build-mostly-bs.376639/page-160",
        "source_tld": "www.tacomaworld.com",
        "trending_datetime": "0001-12-30 00:00:00",
        "type": "gif",
        "url": "https://giphy.com/gifs/bs-YPlmbMKmn8nUA",
        "username": ""
      }
    ],
    "meta": {
      "msg": "OK",
      "response_id": "59db372d4746633649106acc",
      "status": 200
    },
    "pagination": {
      "count": 1,
      "offset": 0,
      "total_count": 32904
    }
  },
  "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/restaurant-71.png",
  "id": "cdc43ae19e4c2c5c9019810a929f8bbc8097fd34",
  "name": "Nicky B's Pizza",
  "opening_hours": {
    "open_now": false,
    "weekday_text": []
  },
  "photos": [
    {
      "height": 1836,
      "html_attributions": [
        "<a href=\"https://maps.google.com/maps/contrib/109910220150842646697/photos\">Julia Chin</a>"
      ],
      "photo_reference": "CmRaAAAACXHEql9iIC74U4cl8E6VzckYVpeldzERO68cQEbR_3MuKgC6hi--M_plTwYi5WWfORenK9bggZSqoIbh2B4N62DPJ9FE-CKqBGxRb91uyypK9wxWDOQM0FTtgxWI5SDWEhBc5xm5MaH2Gb3zyTdf2fFuGhSaE2JhAx24DjXMUBLBWjASTTKiTw",
      "width": 3264
    }
  ],
  "place_id": "ChIJFxD8vHbMxokRcVvB_kxthFE",
  "price_level": 1,
  "rating": 4.3,
  "reference": "CmRRAAAAKN1WLomr4RiW0o4wUWogHAmKmCsR7tCHw-ZINe6D9WwvASp9NZjZfNVoPXKY6997tjPQbIQu8-tY9Jna3RGcv9BpQ4UN-KmPwEImaRqRxmz7rGA6TjYT-9cbzXT_NIAzEhCUg81sANtOGeQBEzJRN3gTGhRxr3QiPwHRnrTea2WPv_DtbWMPzg",
  "types": [
    "meal_delivery",
    "meal_takeaway",
    "restaurant",
    "food",
    "point_of_interest",
    "establishment"
  ]
}

```
