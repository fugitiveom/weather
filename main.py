''' start of program '''
import datetime
from request import Requester

city = input('City or City, Country: ')
units = input('Units - standard, metric or imperial (Enter for metric): ') or 'metric'

requester = Requester(city, units=units)

weather, city_obj = requester.req_whether()

print(f'\n\n\nThe weather in {weather["sys"]["country"]}, {weather["name"]} now is:\n'\
      f'Temperature: {weather["main"]["temp"]}\n'
      f'Feels like: {weather["main"]["feels_like"]}\n'
      f'{weather["weather"][0]["main"]}: {weather["weather"][0]["description"].title()}\n'
      f'Pressure: {weather["main"]["pressure"]}\n'
      f'Humidity: {weather["main"]["humidity"]}\n'
      f'Wind: {weather["wind"]["speed"]}\n'
      f'Day: from {datetime.datetime.fromtimestamp(weather["sys"]["sunrise"]).strftime("%H:%M")} '
      f'to {datetime.datetime.fromtimestamp(weather["sys"]["sunset"]).strftime("%H:%M")}\n'
      )
