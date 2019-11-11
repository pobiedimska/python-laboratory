"""
Уводяться два числа в двійковій системі числення. 
Потрібно виконати над ними побітові операції І, АБО і виключення АБО. 
В кінці вивести результат операцій також в двійковому поданні. 
"""
import re

integer_pattern = re.compile("^[-+]{0,1}[0,1]+$")

#validator
def input_number(pattern, n):
	number = input("Введіть " + str(n) + " число у двійковій системі числення: ")
	while not bool(pattern.match(number)):
        number = input("З таким значенням неможливо виконати задачу. Спробуйте ще раз.\nВведіть " + str(n) + " число: ")
	return number
	
#convertion to decimal number system
def convert_to_dec(n):
    number = int(input_number(integer_pattern, n), 2)
    return number
	
a = convert_to_dec(1)
b = convert_to_dec(2)

print("Результат побітовою операці І:", str(bin(a&b)))
print("Результат побітовою операці АБО:", str(bin(a|b)))
print("Результат побітовою операці ВИКЛЮЧЕННЯ АБО: ", str(bin(a^b)))

exit = input()
