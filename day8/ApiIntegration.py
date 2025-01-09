import requests

base_url = 'https://api.open-meteo.com/v1/forecast?'

params ={
        'latitude' : 52.52,
        'longitude':13.41,
        'current':'temperature_2m,wind_speed_10m'
        }
response = requests.get(base_url, params= params)


if response.status_code == 200:
    print(response.url)
    print(response.json())
else:
    print('Some Error Occord',response.status_code)