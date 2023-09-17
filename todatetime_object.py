from datetime import datetime, timedelta



###########################################################
###Starting datetime is now :

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
print('the arrival time is:' + f'{arrival_time}')

##############################################################"

###########################################################
###Starting datetime is  :21/01/2023 @ 12:25:53

from datetime import datetime, timedelta

# Define the distance and speed
distance = 10000  # kilometers
speed = 80  # kilometers per hour

# Calculate the voyage time in hours
voyage_time = distance / speed  # hours

# Create a timedelta object with the voyage time
delta = timedelta(hours=voyage_time)

# Define the starting datetime object as January 21, 2023 at 12:25:53
start_time = datetime(2023, 1, 21, 12, 25, 53)

# Add the timedelta to the starting datetime object to get the arrival datetime object
arrival_time = start_time + delta

# Print the arrival datetime object
print(arrival_time)



##############################################################"
# Define the input string
input_str = "2 days 12 hours 31 minutes"

# Split the input string into individual components
components = input_str.split()
days = int(components[0])
hours = int(components[2])
minutes = int(components[4])

# Create a timedelta object with the specified components
delta = timedelta(days=days, hours=hours, minutes=minutes)

# Get the current date and time
now = datetime.now()

# Add the timedelta to the current datetime to get the desired datetime object
result = now + delta

# Print the result
print(result)
