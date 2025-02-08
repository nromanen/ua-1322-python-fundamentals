from pyowm import OWM
from pyowm.commons.exceptions import NotFoundError

def get_weather_api(location: str) -> dict:
    API_KEY = 'ef2206ff5da67de63306d0b143e20872'
    # ---------- FREE API KEY examples ---------------------
    owm = OWM(API_KEY)
    mgr = owm.weather_manager()
    # Search for current weather in London (Great Britain) and get details
    try:
        observation = mgr.weather_at_place(location)
    except NotFoundError:
        return False
    w = observation.weather
    return w





