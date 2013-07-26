from pprint import pprint as pp
import requests

url = 'http://localhost:9999/hello/colin'
response=requests.get(url)

print dir(response)
pp(response.content)