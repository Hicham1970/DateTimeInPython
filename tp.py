from datetime import date, timedelta, time, datetime
from dateutil import tz, zoneinfo


# ?Program pour calculer l ETA :


port_origin = "Syngapore"
time_zone_po = -3
etd = datetime(2023, 11, 2, 12, 00, 00)

dest_port = "Manila"
time_zone_po = -8

distance = 1320
speed = 13

# eta=?


t = int(distance / speed)
vt = time(hour=t, minute=0, second=0, microsecond=0)

print(vt)

# t1= t.strftime("%A-%b-%d-%Y-%I-%M-%p")


# time.struct_time((d.year, d.month, d.day, 0, 0, 0, d.weekday(), yday, -1))

days = t / 24
print(days)

# t = datetime.date(travel_time)
print(travel_time)

t = time(hour=4, minute=22)
print(t)
