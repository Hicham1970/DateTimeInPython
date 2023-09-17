from datetime import date, timedelta, time, datetime
from dateutil import tz, zoneinfo

# pour l exemple 1 , tout les objets etaient Naives
# cad qu on a pas des infos sur the time zone
# pour les rendre Aware cad conscient ou pour tenir conte de la tz
# il faut fournir ces infos
# on a une class datetimezone ds la class module datetime
# mais il faut installer une autre librairie : pip install python-dateutil
# ===> from dateutil import tz

# NB: the datetime AWARE object is always compared with the UTC = Greenwich


# my_tz = tz.UTC

# now = datetime.now(tz=my_tz) #Aware
# print(now)
# 2023-04-26 00:59:43.685282+00:00
# print(now.tzinfo)
# tzutc()
# utcnow = datetime.utcnow() #Naive
# print(utcnow)
# 2023-04-26 00:59:43.686282
# print(utcnow.tzinfo)
# None


zonenames = zoneinfo.get_zonefile_instance().zones
# print(zonenames)

# for region in zonenames:
# print(region)


my_time_zone = tz.gettz("Asia/Dubai")
maintenant = datetime.now(tz=my_time_zone)
print(maintenant)
#2023-04-26 05:30:24.431452+04:00

print(maintenant.strftime("%Y-%m-%d-%I-%M-%p"))
print(maintenant.strftime("%A-%b-%d-%Y-%I-%M-%p"))

#conversio string time type to a datetime object:

dt_string ="Wednesday-Apr-26-2023-05-40-AM"

dt_dt = datetime.strptime(dt_string,"%A-%b-%d-%Y-%I-%M-%p")
print ('dt_dt is :', dt_dt)



#my_time_zone = tz.gettz("Asia/Dubai")
# maintenant = datetime.now(tz=my_time_zone) #Aware
# print(maintenant)
