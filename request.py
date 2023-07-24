''' requests '''
import requests
from config import service_geo_url, service_whether_url, GET_TIMEOUT

class Requester():
    ''' requests the whether '''
    def __init__(self, city, **kwargs):
        self.geo_url = self._build_url(service_geo_url, q=city)
        self.whether_url = self._build_url(service_whether_url, **kwargs)

    def req_whether(self):
        ''' get the whether from api'''
        city_obj = requests.get(self.geo_url, timeout = GET_TIMEOUT)
        city_obj_json = city_obj.json()
        lat = city_obj_json[0]['lat']
        lon = city_obj_json[0]['lon']
        self.whether_url = self._build_url(self.whether_url, lat = lat, lon = lon)
        whether = requests.get(self.whether_url, timeout = GET_TIMEOUT)
        return whether

    def _build_url(self, url, **kwargs):
        for key, value in kwargs.items():
            url += f'&{key}={value}'
        return url
