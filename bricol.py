from geopy import distance
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import pytz
from pystyle import *
import math
from datetime import datetime, timedelta
import datetime as dt

print(Box.Lines("[+] Programme pour determiner l ETA [+] "))
Write.Print("[+] This program for mariners [+]\n", Colors.purple_to_red)
Write.Print("[+]distance entre 2 ports et eta [+]\n\n",
            Colors.purple_to_red)
print(Box.DoubleCube("Exemple [x]"))

# initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")

# place input

Input_place1 = Write.Input(
    'Write place 1 :', Colors.blue_to_green, interval=0.1)
Input_place2 = Write.Input(
    'Write place 2 :', Colors.blue_to_green, interval=0.1)

Write.Print("[+] La distance entre :" + Input_place1 + " " + "et " + " " + Input_place2 + " est de :",
            Colors.blue, interval=0.1)

# Get location of the input strings
place1 = geolocator.geocode(Input_place1)
place2 = geolocator.geocode(Input_place2)

# Get latitude and longitude
Loc1_lat, Loc1_lon = (place1.latitude), (place1.longitude)
Loc2_lat, Loc2_lon = (place2.latitude), (place2.longitude)

location1 = (Loc1_lat, Loc1_lon)
location2 = (Loc2_lat, Loc2_lon)
# Distance between ports:
# dist = distance.distance(location1, location2).nm
dist = geodesic(location1, location2).kilometers

print(distance.distance(location1, location2).km, " kms")

# Define the departure time in UTC
# departure_time = datetime(2023, 1, 25, 16, 9, 10, tzinfo=dt.timezone.utc)


#
# Speed input:
speed_str = Write.Input(
    'Average travelling speed :', Colors.blue_to_green, interval=0.1)

speed = float(speed_str)  # convert the string to a float

# Calculate the travelling time based on the distance and the speed of the vessel
travelling_time = dist / speed

# Define the starting time and time zone(tz=0 pour casa)
starting_time = datetime(Write.Input(
    'Give the starting date: y, m, d, h, mn, sc :', Colors.blue_to_green, interval=0.1, tzinfo=dt.timezone.utc))

eta = starting_time + timedelta(hours=travelling_time)

# Adjust the ETA for any daylight time difference
# If the crossing occurs during daylight saving time, adjust the ETA by one hour
if dt.timezone.dst(eta):
    eta = eta + timedelta(hours=1)

# Print the ETA
print("Estimated time of arrival:", eta.strftime("%Y-%m-%d %H:%M:%S %Z%z"))

input('\n press any key to exit....')
