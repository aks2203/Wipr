
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

def intermediate_point(p, q, delta):
    phi1, lam1 = deg2rad(p)
    phi2, lam2 = deg2rad(q)


    a = sin((1 - f) * delta) / sin(delta)
    b = sin(f * delta) / sin(delta)
    x = a * cos(phi1) * cos(lam1) + b * cos(phi1) * cos(lam2)
    y = a * cos(phi1) * sin(lam1) + b * cos(phi1) * sin(lam2)
    z = a * sin(phi1) + b * sin(phi2)
    phi_int = arctan(z / sqrt(x**2 + y**2))
    lam_int = arctan(y, x)
    return rad2deg(phi_int), rad2deg(lam_int)



def point_on_line(p, q, d): 
    ''' return a point d units from p on the line connecting p and q'''
    delta = d / segment_length(p, q)
    return intermediate_point(p, q, delta)


    

def fifteen_mile_markers(travel_route, d=15):
    ''' return a list of lat,lng every 15 miles of the trip '''
    temp = 0

    travel_route.append(travel_route[-1])
    points = travel_route
    points.reverse()
    current = points.pop()
    next = points.pop()
    output = [current]

    while points:
        seg_len = segment_length(next, current)
        print points
        print current, next, temp
       
        if (seg_len == d - temp):
            output.append(next)
            temp = 0
            current = next
            next = points.pop()

        elif (seg_len > d - temp):
            p = point_on_line(current, next, d - temp)
            output.append(p)
            temp = 0
            current = p

        elif (seg_len < d - temp):
            temp += seg_len
            current = next
            next = points.pop()

    output.append(current)
    if output[-1] == output[-2]: output.pop()

return output
