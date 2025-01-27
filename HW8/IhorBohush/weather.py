import requests
from time import ctime

settlement = input('Enter the name of the settlement: ')


def weather(city):
    coordinates = (requests.get(url=f"http://api.openweathermap.org/geo/1.0/direct?q={city},\
                            'uk'&appid=003c91d6031b0ded276bf126ac2c4069")).json()

    data = (requests.get(url=f'https://api.openweathermap.org/data/3.0/onecall?lat={coordinates[0]["lat"]}&lon='
                             f'{coordinates[0]["lon"]}&units=metric&lang=uk&'
                             f'appid=003c91d6031b0ded276bf126ac2c4069')).json()

    print(f'Current temperature: {data["current"]["temp"]}°C',
          f'Temperature fells like: {data["current"]["feels_like"]}°C',
          f'Weather description: {data["current"]["weather"][0]["description"]}',
          f'Sunrise: {ctime(data["current"]["sunrise"])}',
          f'Sunset: {ctime(data["current"]["sunset"])}',
          sep='\n')


weather(settlement)
