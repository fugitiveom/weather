''' start of program '''
from request import Requester

city = input('City: ')

requester = Requester(city)

whether = requester.req_whether()
print(whether)
