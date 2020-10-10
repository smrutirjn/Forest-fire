import requests
from pprint import pprint

city = input('Enter your city : ')

# url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=ff4acd080dec021d24085ed253cbe509&units=metric'.format(city)
url = 'http://api.openweathermap.org/data/2.5/forecast?q=London,us&mode=xml&appid=ff4acd080dec021d24085ed253cbe509'
res = requests.get(url)

data = res.json()
print (data)
# temp = data['main']['temp']
# hum = data['main']['humidity']
# pressure = data['main']['pressure']
# wind_speed = data['wind']['speed']
# latitude = data['coord']['lat']
# longitude = data['coord']['lon']

# description = data['weather'][0]['description']

# print('Temperature : {} degree celcius'.format(temp))
# print('Humiduty : {}'.format(hum))
# print('Pressure : {}'.format(pressure))
# print('Latitude : {}'.format(latitude))
# print('Longitude : {}'.format(longitude))
# print('Description : {}'.format(description))
