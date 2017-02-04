################################
#
# Avi Schwarzschild, Dan Singer
# DevFest 2017
# Wipr
# Weather module
# for getting foracasts at a time and place.
#
################################



import forecastio
from datetime import datetime, timedelta

api_key = '45cd7693234cd1549f8d103703b7b5da'

def get_weather(lat, lng, time=datetime.now()):
    forecast = forecastio.load_forecast(api_key, lat, lng, time)
    current = forecast.currently()
    # return current.summary, current.temperature
    return current.icon

