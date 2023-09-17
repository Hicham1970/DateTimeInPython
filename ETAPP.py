import tkinter as tk
from tkinter import messagebox
from geopy.distance import geodesic
from datetime import datetime, timedelta
import datetime as dt
from geopy.geocoders import Nominatim
import time

# Initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")


def calculate_eta():
    # Get user inputs
    departure_datetime = departure_entry.get()
    speed_knots = speed_entry.get()
    departure_port = departure_port_entry.get()
    arrival_port = arrival_port_entry.get()

    try:
        # Parse departure datetime
        departure_time = datetime.strptime(departure_datetime, "%Y-%m-%d %H:%M:%S")

        # Geocode departure and arrival ports
        place1 = geolocator.geocode(departure_port)
        place2 = geolocator.geocode(arrival_port)

        if not place1 or not place2:
            messagebox.showerror("Error", "Could not find location information for one or both ports.")
            return

        loc1_lat, loc1_lon = place1.latitude, place1.longitude
        loc2_lat, loc2_lon = place2.latitude, place2.longitude

        location1_coords = (loc1_lat, loc1_lon)
        location2_coords = (loc2_lat, loc2_lon)

        # Calculate distance between ports
        dist = geodesic(location1_coords, location2_coords).kilometers

        # Calculate estimated time of arrival
        speed = float(speed_knots)
        travelling_time = dist / speed
        eta = departure_time + timedelta(hours=travelling_time)

        # Adjust for time zone difference
        timezone = dt.timezone(timedelta(hours=1))  # UTC+1
        eta = eta.astimezone(timezone)

        # Adjust for daylight saving time
        if time.localtime().tm_isdst:
            eta = eta + timedelta(hours=1)

        # Display ETA
        eta_label.config(text="Estimated time of arrival: " + eta.strftime("%Y-%m-%d %H:%M:%S %Z%z"))

    except ValueError:
        messagebox.showerror("Error", "Invalid input format for departure date and time.")


# Create the main window
root = tk.Tk()
root.title("ETA Calculator")

# Create input fields
departure_label = tk.Label(root, text="Departure Date and Time (YYYY-MM-DD HH:MM:SS):")
departure_label.pack()
departure_entry = tk.Entry(root)
departure_entry.pack()

speed_label = tk.Label(root, text="Speed (knots):")
speed_label.pack()
speed_entry = tk.Entry(root)
speed_entry.pack()

departure_port_label = tk.Label(root, text="Port of Departure:")
departure_port_label.pack()
departure_port_entry = tk.Entry(root)
departure_port_entry.pack()

arrival_port_label = tk.Label(root, text="Port of Arrival:")
arrival_port_label.pack()
arrival_port_entry = tk.Entry(root)
arrival_port_entry.pack()

# Create Calculate ETA button
calculate_button = tk.Button(root, text="Calculate ETA", command=calculate_eta)
calculate_button.pack()

# Create output label for ETA
eta_label = tk.Label(root, text="")
eta_label.pack()

# Run the Tkinter main loop
root.mainloop()
