import requests

API = '84b66753dae64199592e1bedb91f9b9a'
def get_weather(city: str) -> dict:
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}')
    return response.json()



if __name__ == "__main__":
    data = get_weather(input("Enter a city: "))
    print(get_weather(data))
    print("~"*20)
    print(f"weather: {data['weather'][0]['main']}",
          f"Temp: {data['main']['temp']}",
          f"Wind speed: {data['wind']['speed']}",
          sep = '\n'
        )