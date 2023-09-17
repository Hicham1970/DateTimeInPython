from geopy.distance import geodesic
from datetime import datetime, timedelta
import datetime as dt
from geopy.geocoders import Nominatim
import time  # Import the time module

# Initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")

# Input validation for departure and arrival ports
while True:
    input_place1 = input("Enter departure port: ")
    input_place2 = input("Enter port of arrival: ")

    if input_place1.strip() and input_place2.strip():
        break
    else:
        print("Please provide valid input for departure and arrival ports.")

# Get location of the input strings
place1 = geolocator.geocode(input_place1)
place2 = geolocator.geocode(input_place2)

# Error handling for geocoding results
if not place1 or not place2:
    print("Error: Could not find location information for one or both ports.")
    exit()

# Get latitude and longitude
loc1_lat, loc1_lon = place1.latitude, place1.longitude
loc2_lat, loc2_lon = place2.latitude, place2.longitude

# Define the coordinates of the departure and arrival ports
location1_coords = (loc1_lat, loc1_lon)
location2_coords = (loc2_lat, loc2_lon)

# Calculate the distance between the two ports
dist = geodesic(location1_coords, location2_coords).kilometers

# Define the departure time in a specific time zone (e.g., UTC)
departure_time = datetime(2023, 9, 16, 20, 9, 10, tzinfo=dt.timezone.utc)

# Define the speed of the vessel in knots
speed = 13

# Calculate the estimated time of arrival
travelling_time = dist / speed
eta = departure_time + timedelta(hours=travelling_time)

# Adjust the ETA for the time zone difference
# Assuming departure is in UTC
timezone = dt.timezone(timedelta(hours=1))  # UTC+1
eta = eta.astimezone(timezone)

# Adjust the ETA for daylight saving time
# Check if daylight saving time is in effect
if time.localtime().tm_isdst:
    eta = eta + timedelta(hours=1)

# Print the ETA
print("Estimated time of arrival:", eta.strftime("%Y-%m-%d %H:%M:%S %Z%z"))
