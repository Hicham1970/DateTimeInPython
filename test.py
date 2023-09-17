from geopy.geocoders import Nominatim
import distance
from datetime import date, time, datetime , timedelta
from zoneinfo import ZoneInfo

#####################################################
#This code calculates the voyage time in hours by dividing the distance by the speed.
#It then creates a timedelta object using the hours parameter and the calculated voyage time.

#A starting datetime object is defined using the datetime.
#now() function, which returns the current date and time.
#The timedelta object is added to the starting datetime object using the + operator
#to obtain the arrival datetime object.

#Finally, the arrival datetime object is printed to the console.
#This will output the date and time when the voyage is expected to arrive,
#based on the distance and speed provided.
#####################################################


# Define the distance and speed
dist = 10000  # kilometers
speed = 80  # kilometers per hour

# Calculate the voyage time in hours
voyage_time = dist / speed  # hours

# Create a timedelta object with the voyage time
delta = timedelta(hours=voyage_time)

# Define the starting datetime object
start_time = datetime.now()

# Add the timedelta to the starting datetime object to get the arrival datetime object
arrival_time = start_time + delta

# Print the arrival datetime object
print(arrival_time)









# input

dist = 1000
speed = 80

hours_traveled = dist / speed

ht_rounded = round(hours_traveled)

days = int(round((hours_traveled / 24),2))

mn = (round((hours_traveled / 24) * 60,0))

declaration = f"The total voyage trip will be : {days} days, {hours_traveled} hours, {mn} minutes"

# Print the result
print(f"{hours_traveled} hours is equal to {days} days {ht_rounded} hours and {mn} minutes")
print(declaration)

#***********************Geolocalisation***********************************************/

# initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")

# place input

Input_place1 = input('Write Departure port :')
Input_place2 = input('Write Arrival port :')


# Get location of the input strings
place1 = geolocator.geocode(Input_place1)
place2 = geolocator.geocode(Input_place2)

# Get latitude and longitude
Loc1_lat, Loc1_lon = (place1.latitude), (place1.longitude)
Loc2_lat, Loc2_lon = (place2.latitude), (place2.longitude)

location1 = (Loc1_lat, Loc1_lon)
location2 = (Loc2_lat, Loc2_lon)


# display the distance
trajet = distance.distance(location1, location2).


#***********************ETA Calculation***********************************************/

Input_place1 = input('Write Departure port :')
Input_place2 = input('Write Arrival port :')

# on veut calculer le temps d'arriver estimé du navire :
# input
# depart zone :dz

dp = Input_place1
dt = f"The total voyage trip will be : {days} days, {hours_traveled} hours, {mn} minutes"
now_in_Casablanca = datetime.now(tz=ZoneInfo("Africa/Casablanca"))

print(dp)
print(dt)
print(now_in_Casablanca)
