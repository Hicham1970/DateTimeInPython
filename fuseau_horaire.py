from datetime import date, time, datetime
from dateutil import parser
from zoneinfo import ZoneInfo



# Objets datetime Aware
now_in_Casablanca = datetime.now(tz=ZoneInfo("Africa/Casablanca"))
print(now_in_Casablanca)

now_in_Montreal = datetime.now(tz=ZoneInfo("America/Montreal"))
print(now_in_Montreal)

# Objets datetime Naive

now_in_Casa = datetime.now()
print(now_in_Casa)

now_in_Paris = now_in_Montreal.astimezone(ZoneInfo("Europe/Paris"))

print(now_in_Paris)


