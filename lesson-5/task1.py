# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open("for_task_1&2.txt", "w+", encoding="utf-8") as file:
    file.write(input("Enter anything: \n") + "\n")
    while file.write(input()):
        file.write("\n")
    file.seek(0)
    content = file.read()
    print(content)

file.close() # почему он не закрыл файл без этой команды? Без неё значение - Ложь
print(file.closed)










