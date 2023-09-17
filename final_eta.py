from geopy.distance import geodesic
from datetime import datetime, timedelta
import datetime as dt
from geopy import distance
from geopy.geocoders import Nominatim

############################
# initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")

Input_place1 = input("Enter departure port : ")
Input_place2 = input("Enter port of arrival : ")

# Get location of the input strings
place1 = geolocator.geocode(Input_place1)
place2 = geolocator.geocode(Input_place2)

# Get latitude and longitude
Loc1_lat, Loc1_lon = (place1.latitude), (place1.longitude)
Loc2_lat, Loc2_lon = (place2.latitude), (place2.longitude)

# Define the coordinates of the departure and arrival ports
location1_coords = (Loc1_lat, Loc1_lon)
location2_coords = (Loc2_lat, Loc2_lon)

# Calculate the distance between the two ports
dist = geodesic(location1_coords, location2_coords).kilometers

# Define the departure time in UTC
departure_time = datetime(2023, 4, 25, 16, 9, 10, tzinfo=dt.timezone.utc)

# Define the speed of the vessel in knots
speed = 13

# Calculate the estimated time of arrival
travelling_time = dist / speed
eta = departure_time + timedelta(hours=travelling_time)

# Adjust the ETA for the time zone difference
timezone = dt.timezone(timedelta(hours=1))  # UTC+1
eta = eta.astimezone(timezone)

# Adjust the ETA for any daylight time difference
# If the crossing occurs during daylight saving time, adjust the ETA by one hour
if timezone.dst(eta):
    eta = eta + timedelta(hours=1)

# Print the ETA
print("Estimated time of arrival:", eta.strftime("%Y-%m-%d %H:%M:%S %Z%z"))
