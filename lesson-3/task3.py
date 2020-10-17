# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(x, y, z):
    my_list = [x, y, z]
    min_1 = min(my_list)
    my_list.remove(min_1)
    print(sum(my_list))


my_func(22, 2, 3)


# my_list = []
# min_num = 0
# num = 0
# count = int(input("Сколько чисел Вы введёте? - "))
# while count != 0:
#     count -= 1
#     num = int(input("Введите число: "))
#     my_list.append(num)
#
# min_num = min(my_list)
# my_list.remove(min_num)
# print(sum(my_list))






