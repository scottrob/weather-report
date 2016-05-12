import requests

def data():
    zipcode = input('zipcode?: ')
    r = requests.get('http://api.wunderground.com/weather/api/604ecfa5d8c4adc5/alerts/geolookup/astronomy/conditions/forecast10day/currenthurricane/pws:0/q/{}.json'.format(base_url, zipcode))
    data = r.json()
    return data
