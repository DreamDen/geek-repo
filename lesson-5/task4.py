# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
from googletrans import Translator
traslator = Translator()

with open("for_task4.txt", "r", encoding="utf-8") as file:
    content = file.readlines()
    res = traslator.translate(content, dest="ru")


with open("for_task4_translate.txt", "w", encoding="utf-8") as file:
    for trans in res:
        file.write(trans.text + "\n")



