'''
Created on 2021-05-31

@author: Bartosz Walewski
'''
from datetime import datetime
import unicodedata


def week_day(day, plus=0):
    day_number = datetime.strptime(day, '%d.%m.%Y').weekday()
    day_number += plus
    day_number %= 7
    if day_number == 0:
        return "Poniedziałek"
    elif day_number == 1:
        return "Wtorek"
    elif day_number == 2:
        return "Środa"
    elif day_number == 3:
        return "Czwartek"
    elif day_number == 4:
        return "Piątek"
    elif day_number == 5:
        return "Sobota"
    elif day_number == 6:
        return "Niedziela"


def query_normalize(query):
    query = unicodedata.normalize("NFD", query).replace(u'ł', 'l').replace(u'Ł', 'L').encode("ascii", "ignore")
    query = query.decode('utf-8')
    return query
