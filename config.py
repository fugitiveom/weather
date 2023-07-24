''' config file '''
API_KEY = '7bbaee423589b9ffd0e0beb90238712c'

service_geo_url = f'http://api.openweathermap.org/geo/1.0/direct?appid={API_KEY}'
service_whether_url = f'https://api.openweathermap.org/data/2.5/weather?appid={API_KEY}'
GET_TIMEOUT = 10 # timeout in seconds for get request
