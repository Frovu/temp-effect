import numpy as np
import proxy

# receives 2d array a[lat][lon]
# returns value approximated for given coords
def _interpolate_coords(data, lat, lon):
    return data[0][0] # TODO

# receives 4d array a[time][level][lat][lon] (raw data)
# returns 2d array a[level][time] (approximated for given coords)
def _approximate_for_point(data, lat, lon):
    return data

# receives 2d array a[level][time]
def _interpolate_time(line, tick_min=60):
    return line

def get(lat, lon, start_time, end_time):
    lat = round(lat, 2)
    lon = round(lon, 2)
    data = proxy.query(lat, lon, start_time, end_time)
    approximated = _approximate_for_point(lat, lon)
    # result = [_interpolate_time(line) for line in approximated]