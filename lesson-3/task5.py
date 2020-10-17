def summa():


    print("Вводите цифры через пробел. Для выхода нажмите Q")
    x = True
    result = 0
    while x == True:
        try:
            while x == True:
                numbers = input("Введите цифры: ").split()
                res_line = 0
                for num in numbers:
                    if "q" in num or "Q" in num:
                        x = False
                        break
                    res_line += int(num)
                result += res_line
                print(f"Сумма = {result}")
            return result
        except ValueError:
            print("Вы ввели некорректный символ")

print(summa())

