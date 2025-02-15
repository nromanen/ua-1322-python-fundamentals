import requests
from time import ctime


def weather(city):
    coordinates = (requests.get(url=f"http://api.openweathermap.org/geo/1.0/direct?q={city},\
                            'uk'&appid=003c91d6031b0ded276bf126ac2c4069")).json()

    data = (requests.get(url=f'https://api.openweathermap.org/data/3.0/onecall?lat={coordinates[0]["lat"]}&lon='
                             f'{coordinates[0]["lon"]}&units=metric&lang=uk&'
                             f'appid=003c91d6031b0ded276bf126ac2c4069')).json()

    return (f'Current temperature: {data["current"]["temp"]}°C \n'
            f'Temperature fells like: {data["current"]["feels_like"]}°C \n'
            f'Weather description: {data["current"]["weather"][0]["description"]} \n'
            f'Sunrise: {ctime(data["current"]["sunrise"])} \n'
            f'Sunset: {ctime(data["current"]["sunset"])}')


if __name__ == '__main__':
    settlement = input('Enter the name of the settlement: ')
    print(weather(settlement))
