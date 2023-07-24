''' requests '''
import requests
from config import service_geo_url, service_whether_url, GET_TIMEOUT

class Requester():
    ''' requests the whether '''
    def __init__(self, city, **kwargs):
        self.geo_url = self._build_url(service_geo_url, q=city)
        self.weather_url = self._build_url(service_whether_url, **kwargs)

    def req_whether(self):
        ''' get the whether from api'''
        city_obj = requests.get(self.geo_url, timeout = GET_TIMEOUT)
        city_obj_json = city_obj.json()
        lat = city_obj_json[0]['lat']
        lon = city_obj_json[0]['lon']
        self.weather_url = self._build_url(self.weather_url, lat = lat, lon = lon)
        weather = requests.get(self.weather_url, timeout = GET_TIMEOUT)
        weather_json = weather.json()
        return weather_json, city_obj_json

    def _build_url(self, url, **kwargs):
        for key, value in kwargs.items():
            url += f'&{key}={value}'
        return url
