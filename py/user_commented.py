###################################
#
# Avi Schwarzschild, Dan singer
# DevFest 2017
# Wipr App
#
###################################

# Google Maps Api user input
# This version is commented for educational purposes

# Import statements, for modules to get Google Maps data and plotting
from googlemaps import Client
import gmplot
from numpy import sin, cos, deg2rad, rad2deg

# API keys, issued to us from Google to access the API
api_key_route = 'AIzaSyDJJGsUGU96GMLYUdeOdufkoIG-x2Soo9s'
api_key_maps = 'AIzaSyDg-yjmIEndzcGRaHxH8-Jx2UNAerk7430'

# Initialize the API object
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
    ''' return length in miles of total route '''
    return

def segment_length(p1, p2):
    ''' return length in miles between two lat,lng points '''

    # Calculate lat and long differences and convert to radians
    delta_lat = deg2rad(p1[0] - p2[0])
    delta_lng = deg2rad(p1[1] - p2[1])


    earth_radius_km = 6371
    

    return rad2deg(delta_lng), rad2deg(delta_lat)

print segment_length((lat0, lng0),(lat1, lng1))

def fifteen_mile_markers(travel_route):
    ''' return a list of lat,lng every 15 miles of the trip '''
    return






    