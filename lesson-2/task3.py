# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.

month = int(input("Введите число, номер месяца: "))

if month > 1 and month < 12:
    season_list = ["Winter", "Spring", "Summer", "Fall"]
    season_dict = {1 : "Winter", 2 : "Spring", 3 : "Summer", 4 : "Fall"}
    if month == 1 or month == 2 or month == 12:
        print(season_list[0])
        print(season_dict.get(1))
    elif month >= 3 and month <= 5:
        print(season_list[1])
        print(season_dict.get(2))
    elif month >= 5 and month <= 8:
        print(season_list[2])
        print(season_dict.get(3))
    elif month >= 9 and month <= 11:
        print(season_list[3])
        print(season_dict.get(4))
else:
    print("Такого месяца не существует!")


