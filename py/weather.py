################################
#
# Avi Schwarzschild, Dan Singer
# DevFest 2017
# Wipr
#
################################


# weather api testing
import forecastio

api_key = '9191e5943e8edbb7e275b0193a7f53cf'

lat = 40.80827 
lng = -73.965998

forecast = forecastio.load_forecast(api_key, lat, lng)

byHour = forecast.hourly()
print byHour.summary
print byHour.icon

print ''
print ''

for i, hourlyData in enumerate(byHour.data):
    print i
    print hourlyData.temperature
    print ''

