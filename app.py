from flask import Flask,request, url_for, redirect, render_template
import requests
from pprint import pprint
import numpy as np
import datetime 
import pickle
import pyrebase
import random
config = {
	"apiKey": "AIzaSyB-TwUgMZvF_77H5nTECl4FsvgBqmSCLFE",
    "authDomain": "forest-a09b2.firebaseapp.com",
    "databaseURL": "https://forest-a09b2.firebaseio.com",
    "projectId": "forest-a09b2",
    "storageBucket": "forest-a09b2.appspot.com",
    "messagingSenderId": "153873115235",
    "appId": "1:153873115235:web:aa76783b1a052946b9f056",
    "measurementId": "G-SGH661GNBZ"
}
model=pickle.load(open('model.pkl','rb'))
app = Flask(__name__)
url = 'http://api.openweathermap.org/data/2.5/weather?q=Bhubaneswar&appid=ff4acd080dec021d24085ed253cbe509&units=metric'
res = requests.get(url)
data = res.json()
temp = abs(data['main']['temp']-5.3)/20
hum = abs(data['main']['humidity']-20)/80
pressure = abs(data['main']['pressure']-5.3)/20
wind_speed = abs(data['wind']['speed']-0.9)/7.2
latitude = data['coord']['lat']
longitude = data['coord']['lon']
FFMC=0.77
x=0.5
y=0.5
dmc=0.48
dc=0.6
isi=0.49
time=datetime.datetime.now()
day = abs(int(time.strftime("%w"))-1)/6
mon = abs(int(time.strftime("%m"))-1)/11
rain=0
area= 0.4
b={'tempr':data['main']['temp'],'hum':data['main']['humidity'],'pressure':data['main']['pressure'],'wind_speed':data['wind']['speed']}
location={'Chandaka':{'lat':20.21 , 'lon': 85.40}}
description = data['weather'][0]['description']
a = {'x':x,'y':y,'mon':mon,'day':day,'ffmc':FFMC,'dmc':dmc,'dc':dc,'isi':isi, 'temp':temp,'hum':hum,'wind_speed':wind_speed,'rain':rain,'area':area}
res=model.predict([[a['x'],a['y'],a['mon'],a['day'],a['ffmc'],a['dmc'],a['dc'],a['isi'],a['temp'],a['hum'],a['wind_speed'] ,a['rain']]])
res=res/2

@app.route("/",methods=['POST','GET'])
def cover():
	# res=model.predict([[a['x'],a['y'],a['mon'],a['day'],a['ffmc'],a['dmc'],a['dc'],a['isi'],0.35,0.100,0,a['rain']]])
    return render_template('bjb.html')

@app.route("/dashboard",methods=['POST','GET'])
def hello():
	# res=model.predict([[a['x'],a['y'],a['mon'],a['day'],a['ffmc'],a['dmc'],a['dc'],a['isi'],0.35,0.100,0,a['rain']]])
    return render_template('index.html', tem=b, dat =str(res[0]))
    
    # return(str(res[0]))
    # return ([a.values()])
    # # return model.predict([int(a.values())])
    # output='{0:.{1}f}'.format(prediction[0][1], 2)
# @app.route("/predict",methods=['POST','GET'])
# def predic():
# 	if request.method == 'POST':	
# 		select = request.form.get('Forest')
# 		return(data)

@app.route("/predict",methods=['POST','GET'])
def predict():
	if request.method == 'POST':
		features=[int(x) for x in request.form.values()]
		temp2 = (abs(features[0]-5.3)/20)
		hum2 = (abs(features[1]-20)/80)
		wind_speed2 = (abs(features[2]-0.9)/7.2)
		res2=model.predict([[a['x'],a['y'],a['mon'],a['day'],a['ffmc'],a['dmc'],a['dc'],a['isi'],temp2,hum2,wind_speed2 ,a['rain']]])
		res2=res2
		return render_template('index.html', tem=b, dat =str(res[0]),dat2=str(res2[0]))
    # print(final)
    # prediction=model.predict_proba(final)
    # output='{0:.{1}f}'.format(prediction[0][1], 2)

    # if output>str(35):
    #     return render_template('forest_fire.html',pred='Your Forest is in Danger.\nProbability of fire occuring is {}'.format(output),bhai="kuch karna hain iska ab?")
    # else:
    #     return render_template('forest_fire.html',pred='Your Forest is safe.\n Probability of fire occuring is {}'.format(output),bhai="Your Forest is Safe for now")

# @app.route("/modules",methods=['POST','GET'])
# def detect(x):
# 	t=x['sensor1']['temp']
# 	if t>28:
# 		t1=(t-28)*2
# 	h=x['sensor1']['hum']
# 	if h<80:
# 		h1=(80-h)
# 	h=x['sensor1']['smoke']
# 	if (h>100):
# 		s1=40
# 	sum = t1+h1+s1
# 	if sum>99:
# 		sum = 99
# 	sum = int(sum/10)
# 	sum = (sum*10)+(random.random()*10)
# 	return sum
@app.route("/modules",methods=['POST','GET'])
def hardware():
	firebase = pyrebase.initialize_app(config)
	db = firebase.database()
	sens= db.get().val()
	s = dict(sens)	
	
	sum=0
	t1=h1=s1=0
	t=s['sensor1']['temp']
	if t>28:
		t1=(t-28)*2
	h=s['sensor1']['hum']
	if h<80:
		h1=(80-h)
	k=int(s['sensor1']['smoke'])
	if (k>100):
		s1=40
	su = t1+h1+s1
	if su>99:
		su = 99
	su = int(su/10)
	su = (su*10)+(random.random()*10)
	su = str(su)

	sum=0
	t1=h1=s1=0
	t=s['sensor2']['temp']
	if t>28:
		t1=(t-28)*2
	h=s['sensor2']['hum']
	if h<80:
		h1=(80-h)
	k=int(s['sensor2']['smoke'])
	if (k>100):
		s1=40
	sv = t1+h1+s1
	if sv>99:
		sv = 99
	sv = int(sv/10)
	sv = (sv*10)+(random.random()*10)
	sv = str(sv)
	det = {"sen1":su , "sen2": sv}
	
	return render_template('modules.html',vals=s,sm=det)
	# return render_template('modules.html',vals=sens)
	

if __name__ == '__main__':
    app.run(debug=True)