from datetime import datetime
string_date = "1987-09-24"
datetime_date = datetime.strptime(string_date, "%Y-%m-%d").date()
print(datetime_date)
datetime_today = datetime.today().date()
print(datetime_today)
number_day = (datetime_today - datetime_date).days
print(number_day)

def get_days_from_today(date_str):
    given_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    current_date = datetime.now().date()
    delta_days = (current_date - given_date).days
    return delta_days

date = "1987-09-24"
days_difference = get_days_from_today(date)
#print("Days from", date, "to today:", days_difference)


import random


def get_numbers_ticket(min:int, max:int, quantity:int):
    if min < 1 or max > 1000 or min > max or quantity > (max - min):
        return []
    result = random.sample(range(min, max +1), quantity)
    result.sort()
    return result
    
     
