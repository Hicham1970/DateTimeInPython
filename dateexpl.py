from datetime import date, timedelta, time, datetime

d= date(2021,11,3)
tday = date.today() # NAIVE
now = datetime.now() #AWARE
utcnow = datetime.utcnow()



print (utcnow)
print (utcnow.tzinfo)
#utcnow.tzinfo give None, cad it is Naive
# utc c'est le grinitch, naive car il ne prends pas en conte tzone
# si on utilise .now(vide), on aura le même resultat que .today()
# .now a un attribute tz=none optionel = naive , donne le local time
# sans prendre en consideration le time zone
 
new_year = date(2024, 1, 1)
delta = new_year - tday

t = time(11, 23, 30, 99999)
dt = datetime(2023, 11, 2, 11, 20, 33, 9999)





print(now)
print(tday)
print(delta.days)
print(delta.total_seconds())
print('Hours :', t.hour)
print('Minutes :', t.minute)
print('MicroSeconds :', t.microsecond)
print('MicroSeconds :', t.microsecond)


print('Years :', dt.year)
print('Days :', dt.day)
print('Month :', dt.month)
print('Hours :', dt.hour)
print('Minutes :', dt.minute)
print('Seconds :', dt.second)

print("30 days ago the date was :", d - delta) 
print("30 days into the future the date will be :", d + delta) 
print("day :", d.day) 
print("day :", d.weekday()) 
print("day :", d.isoweekday())
print("month :", d.month)
print("year :", d.year) 

