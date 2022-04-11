import requests

class Weather():
    
    def getWeather(city_name):
        api_key = "f91fa0205e7baf9a0bbeca8a3ccc6976"
        base_url = "http://api.openweathermap.org/data/2.5/weather?lang=tr&"
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            feels_like = y["feels_like"]
            z = x["weather"]
            weather_description = z[0]["description"]
            min_temp = y["temp_min"]
            max_temp = y["temp_max"]
            value = [current_temperature,feels_like,weather_description,min_temp,max_temp]
            return value
        else:
            return "404"