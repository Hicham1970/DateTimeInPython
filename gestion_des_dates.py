from datetime import date, time, datetime
from dateutil import parser
import dateparser


#in the usa on DD-MM-YY

#Norme 8601 YYYY-DDD-DDD

d = date.fromisoformat("2023-12-22")
print(d)
# autre norme


q = datetime.now()
s = q.strftime("%d %B %Y")
print(s)

# parser = analyseur

arrival_time = "24 October 2021 at 9 am and 18 minutes and 45 seconds"
at = parser.parse(arrival_time)
print(at)

# we need to install pip install dateparser externely

depar_time = "aujourd'hui"
at = dateparser.parse(depar_time)

depar_time = "il y ' a un mois"
depar_time = "il y ' a un mois"
