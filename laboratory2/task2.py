"""
2)	Дано ціле число N(>0). Знайти найбільше ціле число K, 
квадрат якого не перевищує N: K2≤N. Функцію добування 
квадратного кореня не використовувати.
"""

import re

limit_pattern = re.compile("^\d*$")

#validator for sum limit
def validate_integer(pattern):
	value = input("Будь ласка, введіть додатнє N: ")
	while not bool(pattern.match(value)):
		value = input("Для такого значення неможливо вирішити задачу, спробуйте щось інше.")
	value = int(value)
	return value

def validate_limit(pattern):
    number = validator_integer(pattern)
    while number<=0:
		print("N повинно бути додатнім.")
        number = validator_integer(pattern)
    return number

	
i = 0
max_int = 0

exit = ""
while exit == "":
n = validate_limit(limit_pattern)

 while i <= n:
     if i**2 <= n:
         max_int = i
         i += 1
     else:
         break

 print("\nНайбільше число, квадрат якого менше або дорівнює "+str(n)+" це", str(max_int))
 exit = input("Введіть будь-що для виходу або нажміть ENTER для продовження")
