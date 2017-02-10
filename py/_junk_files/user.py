###################################
#
# Avi Schwarzschild
#
###################################

# Google Maps Api user input

from googlemaps import Client
import gmplot

api_key_route = 'AIzaSyDJJGsUGU96GMLYUdeOdufkoIG-x2Soo9s'
api_key_maps = 'AIzaSyDg-yjmIEndzcGRaHxH8-Jx2UNAerk7430'
gmaps = Client(api_key_maps)
route_map = Client(api_key_route)


origin = raw_input('Where are you starting? (please enter a valid address) ')
dest = raw_input('Where are you going? (please enter a valid address) ')

lat0, lng0 = gmaps.geocode(origin)[0]['geometry']['location'].values()
print lat0, lng0

lat1, lng1 = gmaps.geocode(dest)[0]['geometry']['location'].values()
print lat1, lng1

routes = route_map.directions(origin, dest)

lats = []
longs = []

for i, step in enumerate(routes[0]['legs'][0]['steps']):
    lats.append(step['start_location']['lat'])
    longs.append(step['start_location']['lng'])
    lats.append(step['end_location']['lat'])
    longs.append(step['end_location']['lng'])

travel_route = zip(lats, longs)

gmap_plt = gmplot.GoogleMapPlotter((lat0 + lat1) / 2.0, (lng0 + lng1) / 2.0, 16)

gmap_plt.plot(lats, longs)
gmap_plt.draw("mymap.html")

def get_length(travel_route):
    ''' return length in miles of total route'''
    return

def segment_length(p1, p2):
    ''' return length in miles between two lat,lng points '''
    return

def fifteen_mile_markers(travel_route):
    ''' return a list of lat,lng every 15 miles of the trip '''
    return






    