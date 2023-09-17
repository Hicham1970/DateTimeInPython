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


print(voyage_time)
print(start_time)
print(arrival_time)
