"""
Обчислити функцію в точці
"""
import re

float_pattern = re.compile("^\d*(\.\d+)?$")

#validator
def validate_arg(pattern):
	arg = input("Введіть x: ")
	while not bool(pattern.match(arg)):
		arg = input("Для значень неможливо обчислити функцію, спробуйте ще раз.\nВведіть х: ")
	arg = float(arg)
	return arg

x = validate_arg(float_pattern)
f = 0
if x > 3:
    f = 1.2*(x**2)-3*x-9
else:
    f = 12.1/(2*(x**2)+1)

print('F(x) = ', str(round(f,2)))
exit = input('Натисніть Enter для завершення')
