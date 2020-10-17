# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def my_div(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("Delenie na 0")
        except TypeError:
            print("Try again")


count = 0
while count < 10:
    a = input("Enter first num ")
    b = input("Enter second num ")
    try:
        a, b = int(a), int(b)
    except ValueError:
        print("invalid literal")
    except TypeError:
        print("Enter natural num")
    finally:
        print(my_div(a, b))
    count += 1






















