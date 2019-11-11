print("Лабораторна робота №1 Варіант 24")
print("Виконав студент групи КМ-93")
print("Яровий Данило Євгенійович")
print("Завдання 3")

end = ""
while end != "1":
    n = 0
    x = 0
    while n < 1:
        try:
            print("Введіть значення верхньої межі сумування: ")
            n = int(input())
            break
        except ValueError:
            print("Верхня межа сумування повинна бути додатньою та цілою.")
            print("Введіть інше значення: ")
            n = int(input())
    while 1:
         try:
             print("Введіть значення x: ")
             x = float(input())
             break
         except ValueError:
             print("Введіть числове значення x: ")
             x = float(input())
    sum = 0
    for i in range(n):
        sum = sum + (x**(i+1)+n)/(x-n)
    print("Сумма дорівнює " + str(sum))
    end = input("Введіть 1 для завершення або будь-що інше для продовження")