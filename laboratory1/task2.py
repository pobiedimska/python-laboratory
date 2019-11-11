"""
До фіналу конкурсу кращого за професією «Спеціаліст електронного офісу» 
були допущені троє: Іванов, Петров, Сидоров. Змагання проходили в три тури. 
Іванов в першому турі набрав t1 балів, у другому - n1, в третьому - p1. 
Петров - t2, n2, p2 відповідно; Сидоров - t3, n3, p3. Скласти програму, 
що визначає, скільки балів набрав переможець (бали вводити з клавіатури). 
"""

import re
import math

points_pattern = re.match("^\d*(\.\d+)?$")

#validator
def validate_points(pattern, surname, tournament):
	points = input("Введіть бали " + surname + " у " + tournament + " турі: ")
	while not re.match(pattern, points):
		points = input("Для таких балів неможливо обчислити задачу, спробуйте ще раз.\nВведіть бали " + surname + " у " + tournament + " турі: ")
	points = float(points)
	return points


surnames = ["Іванова", "Петрова", "Сидорова"]
tournaments = ["першому", "другому", "третьому"]
results = {surnames[0]:"", surnames[1]:"", surnames[2]:""}

for surname in surnames:
	sum = 0
	for tournament in tournaments:
		sum += validate_points(points_pattern, surname, tournament)
	results[surname] = sum

maximum = 0
winner = ""
for name, point in results.items():
	if point > maximum:
		maximum = point
		winner = name
		
print("Переможцем є " + winner + "із загальною суммою баллів: " + point)
exit = input("Натисніть Enter для завершення")
