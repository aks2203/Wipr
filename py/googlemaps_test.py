###################################
#
# Avi Schwarzschild
#
###################################

# Google Maps Api testing 
from googlemaps import Client
import gmplot

api_key_route = 'AIzaSyDJJGsUGU96GMLYUdeOdufkoIG-x2Soo9s'

api_key_maps = 'AIzaSyDg-yjmIEndzcGRaHxH8-Jx2UNAerk7430'
gmaps = Client(api_key_maps)


address = '431 Riverside Drive, New York, NY 10027'
lat, lng = gmaps.geocode(address)[0]['geometry']['location'].values()
print lat, lng

route_map = Client(api_key_route)
routes = route_map.directions('330 West 72, New York 10023', '3198 Old Post Drive, Baltimore, 21208')


lats = []
longs = []

for i, step in enumerate(routes[0]['legs'][0]['steps']):
    lats.append(step['start_location']['lat'])
    longs.append(step['start_location']['lng'])
    lats.append(step['end_location']['lat'])
    longs.append(step['end_location']['lng'])

gmap_plt = gmplot.GoogleMapPlotter(lat, lng, 16)

gmap_plt.plot(lats, longs)
gmap_plt.draw("mymap.html")