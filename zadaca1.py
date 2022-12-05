import requests


url='https://api.v2.emissions-api.org'
endpoint1 = '/api/v2/countries.json'

url_endpoint1 = f'{url}{endpoint1}'
print(url_endpoint1)

headers = {
    'Acceppt': 'application/json'
}


response1 = requests.get(url=url_endpoint1, headers=headers)
print(response1.status_code)
