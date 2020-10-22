# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open("for_task5.txt", "w", encoding="utf-8") as file:
    file.write(input("Введите числа через пробел: "))

with open("for_task5.txt", "r", encoding="utf-8") as file:
    summa = file.read()
    res = 0
    for i in summa:
        if i.isdigit():
            res += int(i)
    print(res)




