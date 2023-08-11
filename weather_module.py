import numpy as np
from geopy.geocoders import Nominatim as Nom
import requests


# Creating function that can give the info of longitude and latitude of given location using geopy
def getCoordinates(location):
    nom = Nom(user_agent="JV_Tech")
    data = nom.geocode(location)
    return data


def getWeatherInfo(location):
    #api key of openweathermap
    api_key = "ae25746d86454ae3e667957b4b7c1cde"

    # Finding coordinates for the given location
    details = getCoordinates(location)
    lat = details.latitude
    lon = details.longitude
    
    part = 'current'

    #url to fetch weatehr data
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"


    response = requests.get(url)
    data = response.json()

    result = {}

    if data["cod"] != "404":
 
        # store the value of "main"
        # key in variable y
        y = data["main"]
 
        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"]
    
        temp_celcius = round(current_temperature - 273.15,2)
    
        temp_farenheat = temp_celcius*9/5 + 32
        result['temperature'] = [temp_celcius, temp_farenheat, current_temperature]
        
        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]
        result['pressure'] = current_pressure
 
        # store the value corresponding
        # to the "humidity" key of y
        current_humidity = y["humidity"]
        result['humidity'] = current_humidity
 
        # store the value of "weather"
        # key in variable z
        z = data["weather"]
 
        # store the value corresponding
        # to the "description" key at
        # the 0th index of z
        weather_description = z[0]["description"]
        result['weather'] = weather_description
        result['loc'] = details.address

    return result

def getForecast(location):
    api_key = "ae25746d86454ae3e667957b4b7c1cde"
    city_data = getCoordinates(location)
    lat= city_data.latitude
    lon = city_data.longitude
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data



