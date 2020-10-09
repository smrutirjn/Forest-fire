from flask import Flask,request, url_for, redirect, render_template
import requests
from pprint import pprint

app = Flask(__name__)
url = 'http://api.openweathermap.org/data/2.5/weather?q=Bhubaneswar&appid=ff4acd080dec021d24085ed253cbe509&units=metric'
res = requests.get(url)
data = res.json()
temp = data['main']['temp']
hum = data['main']['humidity']
pressure = data['main']['pressure']
wind_speed = data['wind']['speed']
latitude = data['coord']['lat']
longitude = data['coord']['lon']
location={'Chandaka':{'lat':20.21 , 'lon': 85.40}}
description = data['weather'][0]['description']
a = {'temp': temp,'hum':hum,'pressure':pressure,'wind_speed':wind_speed}
@app.route("/",methods=['POST','GET'])
def hello():
    return render_template('index.html', tem=a)
@app.route("/predict",methods=['POST','GET'])
def predic():
	if request.method == 'POST':	
		select = request.form.get('Forest')
		return(data)


if __name__ == '__main__':
    app.run(debug=True)