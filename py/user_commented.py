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
from numpy import sin, cos, deg2rad, rad2deg, sqrt, arctan

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

def segment_length(p1, p2):
    ''' return length in miles between two lat,lng points '''

    # Convert lat and lng to radians
    lat1_rad = deg2rad(p1[0])
    lat2_rad = deg2rad(p2[0])
    lng1_rad = deg2rad(p1[1])
    lng2_rad = deg2rad(p2[1])

    # Calculate lat and long differences and convert to radians
    delta_lat_rad = lat1_rad - lat2_rad
    delta_lng_rad = lng1_rad - lng2_rad

    # Convert radian differences to miles using haversine formula
    earth_radius_km = 6371

    a = sin(delta_lat_rad / 2)**2 + cos(lat1_rad) * cos(lat2_rad) * sin(delta_lng_rad / 2)**2
    c = 2 * (arctan((sqrt(a) / sqrt(1 - a))))
    distance_km = earth_radius_km * c
    distance_mi = distance_km / 1.609344    

    return distance_mi

print segment_length((lat0, lng0), (lat1, lng1))

def get_length(travel_route):
    ''' return length in miles of total route '''
    route_length = 0

    # Iterate through travel route coordinate list, totaling distances between successive points
    for i in xrange(0, len(travel_route) - 1): 
        route_length += segment_length(travel_route[i], travel_route[i + 1])

    return route_length

print get_length(travel_route)

def fifteen_mile_markers(travel_route):
    ''' return a list of lat,lng every 15 miles of the trip '''
    return






    