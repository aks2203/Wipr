################################
#
# Avi Schwarzschild, Dan Singer
# DevFest 2017
# Wipr
#
################################


# weather api testing
import forecastio
from datetime import datetime, timedelta

api_key = '9191e5943e8edbb7e275b0193a7f53cf'

lat = 40.80827 
lng = -73.965998
# time = datetime.datetime()

forecast = forecastio.load_forecast(api_key, lat, lng, datetime.now() + timedelta(hours=6))

current = forecast.currently()
print current.summary
print current.icon
print current.temperature

# print ''
# print ''

# for i, hourlyData in enumerate(byHour.data):
#     print i
#     print hourlyData.temperature
#     print ''

