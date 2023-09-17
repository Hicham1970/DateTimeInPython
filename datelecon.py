from datetime import date, time, datetime


d = date(year=2023,month=12, day=22)
print(d)

t = time(hour=13, minute=34, second=12, microsecond=999898)

tr = datetime(year=2023, month=12, day=22, hour=13, minute=34, second=12, microsecond=999898)

print(t)
print(tr)
print(type(t))
print(type(tr))
# method now et today

n = datetime.now()
l = n.hour
print(l)
m = datetime.today()
k = date.today()

alyawm = datetime.today()
radane =alyawm.replace(day=alyawm.day + 1)

print(n)
print(m)
print(k)
print(alyawm)
print(radane)
