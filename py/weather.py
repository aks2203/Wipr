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

api_key = '9191e5943e8edbb7e275b0193a7f53cf'

def get_weather(lat, lng, time):
    forecast = forecastio.load_forecast(api_key, lat, lng, time)
    current = forecast.currently()
    return current.summary, current.temperature

