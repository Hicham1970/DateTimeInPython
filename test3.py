import math
from datetime import datetime, timedelta

# Define the coordinates of Casablanca and Glom fjord
casablanca_lat, casablanca_lon = 33.5731, -7.5898
glom_fjord_lat, glom_fjord_lon = 70.7367, 29.8367

# Define the speed of the vessel in knots
speed = 13  # knots

# Calculate the distance between the two ports using the haversine formula
earth_radius = 6371  # kilometers
lat1, lon1, lat2, lon2 = map(math.radians, [casablanca_lat, casablanca_lon, glom_fjord_lat, glom_fjord_lon])
delta_lat = lat2 - lat1
delta_lon = lon2 - lon1
a = math.sin(delta_lat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(delta_lon / 2) ** 2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
distance = earth_radius * c  # kilometers

# Calculate the travelling time based on the distance and the speed of the vessel
travelling_time = distance / (speed * 1.852)  # hours

# Define the starting time and time zone
starting_time = datetime(2023, 1, 25, 16, 9, 10)
starting_timezone = timedelta(hours=0)

# Add the travelling time to the starting time to obtain the estimated time of arrival
arrival_time = starting_time + timedelta(hours=travelling_time)

# Adjust the estimated time of arrival for the time zone difference and the crossing international daylight time difference
arrival_timezone = timedelta(hours=1)  # Glom fjord time zone is GMT+1
departure_daylight_saving_time = False  # Casablanca does not observe daylight saving time
arrival_daylight_saving_time = True  # Glom fjord observes daylight saving time
if departure_daylight_saving_time and not arrival_daylight_saving_time:
    arrival_time -= timedelta(hours=1)  # adjust for loss of 1 hour
if not departure_daylight_saving_time and arrival_daylight_saving_time:
    arrival_time += timedelta(hours=1)  # adjust for gain of 1 hour
arrival_time += arrival_timezone - starting_timezone  # adjust for time zone difference

# Print the estimated time of arrival
print(arrival_time)
