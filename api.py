import requests
import datetime
import math

# Function to calculate dew point temperature
def calculate_dew_point(temperature, humidity):
    a = 17.27
    b = 237.7
    alpha = ((a * temperature) / (b + temperature)) + math.log(humidity / 100.0)
    dew_point = (b * alpha) / (a - alpha)
    return dew_point

api_key = '115ad0877b727154a241670068d5a70e'
city_name = input("Enter the city name: ")  

url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

req = requests.get(url)
data = req.json()

name = data['name']
lon = data['coord']['lon']
lat = data['coord']['lat']

print(f"City: {name}, Longitude: {lon}, Latitude: {lat}")

url2 = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&units=metric&cnt=16&appid={api_key}'

req2 = requests.get(url2)
data2 = req2.json()

dates = []
temperatures = []
wind_speeds = []
dew_points = []
precipitation_levels = []
descr = []

if 'list' in data2:
    for item in data2['list']:
        date = datetime.datetime.utcfromtimestamp(item['dt'])
        date_str = date.strftime('%Y-%m-%d %H:%M:%S')
        temperature = item['main']['temp']
        wind_speed = item['wind']['speed']

        # Dew Point Temperature
        humidity = item['main']['humidity']
        dew_point = calculate_dew_point(temperature, humidity)

        condition = item['weather'][0]['main'] + ": " + item['weather'][0]['description']

        # Check if precipitation data is available
        if 'rain' in item:
            precipitation = item['rain']['3h']
        else:
            precipitation = 0

        dates.append(date_str)
        temperatures.append(temperature)
        wind_speeds.append(wind_speed)
        dew_points.append(dew_point)
        precipitation_levels.append(precipitation)
        descr.append(condition)
'''
    string = f'[ {name} - 3-Hourly Forecast for the next 2 days]\n'

    for i in range(len(dates)):
        string += f'\nDate: {dates[i]}\n'
        string += 'Temperature: ' + str(temperatures[i]) + '°C\n'
        string += 'Wind Speed: ' + str(wind_speeds[i]) + ' m/s\n'
        string += 'Dew Point Temperature: ' + str(dew_points[i]) + '°C\n'
        string += 'Precipitation: ' + str(precipitation_levels[i]) + ' mm\n'
        string += 'Conditions: ' + descr[i] + '\n'

    print(string)
else:
    print("No 3-hourly forecast data available.")

'''

