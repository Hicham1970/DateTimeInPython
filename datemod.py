from pystyle import *
from datetime import datetime, timedelta, time


print(Box.Lines('[+] Special Module datetime [+] '))
Write.Print("[+] Ce module comporte 4 grandes classes : date, time, datetime et timedelta [+]\n",
            Colors.blue_to_green)
Write.Print(
    "[+] Class: date contient les objets: year, month and day  [+]\n\n", Colors.blue_to_green)
Write.Print(
    "[+] Class: time contient les objets: hour, minutes, seconds & microseconds  [+]\n\n", Colors.blue_to_green)
Write.Print(
    "[+] Class: datetime contient les objets des 2 1eres class  [+]\n\n", Colors.blue_to_green)
Write.Print(
    "[+] Class: timedelta donne la difference entre 2 dates  [+]\n\n", Colors.blue_to_green)
print(Box.DoubleCube("Exemple [7]"))




d = datetime.today()
print(d)







input('\n press any key to exit....')
