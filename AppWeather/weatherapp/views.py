from django.shortcuts import render
import requests

def  homeview(request):
	city = request.GET.get('city' , 'Angul')
	url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID=c288d478e51787960092b5acd79f4576'
	data = requests.get(url).json()
	payload = {
				'city': data['name'],
				'weather':data['weather'][0]['main'],
				'icon':data['weather'][0]['icon'],
				'kelvin_temparature':data['main']['temp'],
				'celcius_temparature':int(data['main']['temp'] - 273),
	            'pressure':data['main']['pressure'],
	            'humidity':data['main']['humidity'],
	            'description':data['weather'][0]['description']}
	context = {'data':payload} 
	print(context)           

	return render (request,'ui/home.html',context)

