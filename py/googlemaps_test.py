###################################
#
# Avi Schwarzschild
#
###################################

# Google Maps Api testing 
from googlemaps import Client

# api_key = 'AIzaSyDJJGsUGU96GMLYUdeOdufkoIG-x2Soo9s'
api_key = 'AIzaSyDg-yjmIEndzcGRaHxH8-Jx2UNAerk7430'
gmaps = Client(api_key)

address = '431 Riverside Drive, New York, NY 10027'
lat, lng = gmaps.geocode(address)[0]['geometry']['location'].values()
print lat, lng

# dest = gmaps.reverse_geocode([lat, lng])[0]['geometry']['formatted_address'].values()
# print dest

one = gmaps.reverse_geocode([lat, lng])[0].keys()
print one
