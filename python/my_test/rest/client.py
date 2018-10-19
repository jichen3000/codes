import requests


headers = {'content-type' : 'application/json'}
data = {"user":"admin","password":""}
response = requests.post('https://10.160.16.12/api/user/login',
                         params=data, headers=headers)
data = response.json()
