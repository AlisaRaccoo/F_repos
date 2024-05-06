from datetime import datetime
string_date = "1987-09-24"
datetime_date = datetime.strptime(string_date, "%Y-%m-%d").date()
print(datetime_date)
datetime_today = datetime.today().date()
print(datetime_today)
number_day = (datetime_today - datetime_date).days
print(number_day)


import random


def get_numbers_ticket(min:int, max:int, quantity:int):
    if min < 1 or max > 1000 or min > max or quantity > (max - min):
        return []
    result = set()
    while len(result) < quantity:
        result.add(random.randint(min,max))
        return sorted(result)
     
