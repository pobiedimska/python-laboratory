print("Побєдімська Соня Ігорівна\nЛабораторна робота №2\nВаріант 17\nОбчислення сумми\n")

import re

float_pattern = re.compile("^\d*(\.\d+)?$")
limit_pattern = re.compile("^\d*$")

#validator for x
def validate_float(pattern):
	value = input("Введіть x: ")
	while not bool(pattern.match(value)):
		value = input("Для такого значення обчислення неможливі, спробуйте ще раз.\nВведіть х: ")
	value = float(value)
	return value
	
#validator for sum limit
def validate_integer(pattern):
	value = input("Введіть значення верхньої межі сумування: ")
	while not bool(pattern.match(value)):
		value = input("Верхня межа сумування повинна бути додатньою та цілою, а також у числовому форматі. Введіть інше значення: ")
	value = int(value)
	return value

def validate_limit(pattern):
    number = validator_integer(pattern)
    while number<=0:
		print("Верхня межа сумування повинна бути додатньою та цілою. Спробуйте ще раз.")
        number = validator_integer(pattern)
    return number
	
exit = ""
while exit == "":
	x = validate_float(float_pattern)
    n = validate_limit(limit_pattern)
    s = 0
    for i in range(n):
        s += x/(2**(i+1))
    print("Сумма дорівнює ", str(round(s, 2)))
    exit = input("Введіть будь-що для виходу або нажміть ENTER для продовження")