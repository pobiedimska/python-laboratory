def StrSpn(main_string: str, string_chars: str):
    main_string = main_string.split(' ')
    string_chars.replace(" ", "")
    for string in main_string:
        good_string = True
        for char in string:
            if not string_chars.__contains__(char):
                # символ зі слова не знаходиться у рядку із символами
                good_string = False
        if good_string:
            return "Довжина першого слова, усі символи якого містяться у рядочку з символами: " + str(len(string))
    return 'У рядочку s немає таких слів, які б містили тільки символи з рядка s1 '


print("Побєдімська Соня Ігорівна\nЛабораторна робота №4\nВаріант 17\nВизначення довжини тієї частини рядка s, "
      "яка містить тільки символи з рядка s1\n")
end = ""
while end == "":
    s = input('Введіть рядок, якій будемо перевіряти: ')
    s1 = input("Введіть рядок з символами: ")
    print(StrSpn(s, s1))
    end = input("Введіть будь-що для завершення або ENTER для продовження ")
