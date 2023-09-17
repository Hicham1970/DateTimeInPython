from pystyle import *
from datetime import datetime, timedelta, date
from geopy.distance import geodesic
from geopy import distance
from geopy.geocoders import Nominatim

print(Box.Lines('[+] Estimated travel Time and ETA [+] '))
Write.Print("[+] This program for ETA [+]\n", Colors.blue_to_cyan)
Write.Print("[+] n is the road steps  [+]\n\n", Colors.blue_to_cyan)
print(Box.DoubleCube("Exemple [7]"))


# Estimation du templs d'attente des navires en rade :

def estim_wait_time(red_time, green_time):
    total_time = red_time + green_time
    total_wait_time = red_time * (red_time + 1) / 2
    return total_wait_time / total_time


n = int(Write.Input("Number of road steps : ",
                    Colors.black_to_white, interval=0.1))

# input steps info:

print(Box.DoubleCube("Road steps Info Or Segments"))

steps = []
for i in range(n):
    print(f"steps{i + 1}")
    distance = float(Write.Input(" - Distance (Km):  ",
                                 Colors.blue_to_cyan, interval=0.1))
    speed = int(Write.Input(" - Speed (Km/h):  ",
                            Colors.blue_to_cyan, interval=0.1))
    steps.append((distance, speed))

print(Box.DoubleCube("Traffic Light Info Or Delays"))

traffic_lights = []
for i in range(n - 1):
    print(f"traffic_lights{i + 1}:")
    red_time = int(Write.Input(" - Red Light Time (hours):  ",
                               Colors.blue_to_cyan, interval=0.1))
    green_time = int(Write.Input(" - Green Light Time (hours):  ",
                                 Colors.blue_to_cyan, interval=0.1))
    traffic_lights.append((red_time, green_time))

# Estimation of the travel time, we look for the wait time first
# Estimation of the average waiting time, we just need to average the wait time for every moment
# la fonction estim_wait_time(): prends 2 arguments: red_time et green_time
# pour chaque etape le temps (entre etapes) total est red_time + green_time


# Calculate total wait time at all traffic lights:
total_wait_time_traffic_light = sum(estim_wait_time(
    light[0], light[1]) for light in traffic_lights)

# Calculate total moving time on all steps:
total_moving_time = sum(step[0] / step[1] for step in steps)

# Estimated total traveling time:
estimated_traveled_time = round(
    total_wait_time_traffic_light + total_moving_time)

# Conversion of the output, if the input is in second, we have to * 3600 the estimated_traveled_time

day = estimated_traveled_time % 60 // 24
hour = estimated_traveled_time
minute = estimated_traveled_time % 3600 // 60
second = estimated_traveled_time % 60

print(
    f"Estimated traveling time to destination is :{day:02}:{hour:02}:{minute:02}:{second:02}")

# output current time and ETA:

departure_time = datetime(2023, 1, 12, 12, 12, 31)

current_time = datetime.now()
eta = current_time + timedelta(days=day, hours=hour,
                               minutes=minute)
eta_str = eta.strftime("%I:%M%p")

print(
    f"Current time is {current_time.strftime('%I:%M%p')}. If you start driving now , you will get there around {eta_str}")

# *************************************************************************************/
# geolocalisation par l API

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

#Create geopy location objects:
location1 = (Loc1_lat, Loc1_lon)
location2 = (Loc2_lat, Loc2_lon)
#Calculate the distance between the 2 locations:
distance_km = geodesic(location1, location2).kilometers

# display the distance
print(distance_km, "kms")

# *************************************************************************************/
''' for step in steps: '''
'''     print(step[0]) '''
'''  '''
''' for light in traffi c_lights:"""
print(light[0]) '''

input('\n press any key to exit....')
