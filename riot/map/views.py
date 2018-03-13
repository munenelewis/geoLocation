from django.shortcuts import render
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyCbFEOjUqV0K96fr4OPieyEDI-BjwwluZY')


def home(request):
    geocode_result = gmaps.geocode('mombasa')
    geo = geocode_result[0]['geometry']
    location=geo['location']
    lat = location.get(lat)

    print(lat)
    

    # print(geocode_result)

    return render(request, 'home.html',{'geocode_result':geocode_result})