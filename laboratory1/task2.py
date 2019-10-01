t1 = int(input("Введіть бали Іванова у першому турі: "))
t2 = int(input("Введіть бали Петрова у першому турі: "))
t3 = int(input("Введіть бали Сидорова у першому турі: "))

n1 = int(input("Введіть бали Іванова у другому турі: "))
n2 = int(input("Введіть бали Петрова у другому турі: "))
n3 = int(input("Введіть бали Сидорова у другому турі: "))

p1 = int(input("Введіть бали Іванова у третьому турі: "))
p2 = int(input("Введіть бали Петрова у третьому турі: "))
p3 = int(input("Введіть бали Сидорова у третьому турі: "))

i=t1+n1+p1
p=t2+n2+p2
s=t3+n3+p3

surname = ""
result = 0

if i>p:
    if i>s:
        surname = "Іванов"
        result = i
    else:
        surname = "Сідорова"
        result = s
elif p>s:
    surname = "Петров"
    result = p
else:
    surname = "Сідорова"
    result = s

print("Переможцем є ", surname, "із загальною сумою баллів: ", str(result))
exit = input("Натисніть Enter для завершення")
