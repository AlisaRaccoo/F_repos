import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r'\b\d+(\.\d+)?\b'
    for match in re.finditer(pattern, text):
        yield float(match.group())  

def sum_profit(text: str, func: Callable):
    total_sum = 0
    for num in func(text):
        total_sum += num 
    
    return total_sum
text = "The income for this month is 1000 and the planned income for next month is 900.25."
total_income = sum_profit(text, generator_numbers)
print("Total income:", total_income)
