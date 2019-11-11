print("Побєдімська Соня Ігорівна\nЛабораторна робота №3\nВаріант 17\nУпорядкування рядка за спаданням довжини слів.\n")

stop = ""
while stop == "":
    number1 = 0
    number2 = 0
    string = input('Введіть рядок: ').split(' ')
    additional_var = 0
    new_string = ''

    for number1 in range(len(string)-1):
        # порівнюємо значення кожного з елементів списку з усіма,
        # що йдуть після нього у списку
        for number2 in range(number1+1, len(string)):
            if len(string[number1]) < len(string[number2]):
                # якщо довжина іншого слова більша, ніж довжина першого
                # слова, то на місце першого слова ставиться те слово, яке є більшим
                additional_var = string[number1]
                string[number1] =  string[number2]
                string[number2] = additional_var
    for word in string:
        word += ' '
        new_string += word

    print('Перетворений рядок: ' + new_string)
    stop = input("Введіть будь-що для виходу або нажміть ENTER для продовження")