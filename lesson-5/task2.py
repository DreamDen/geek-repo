# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

with open ("for_task_1&2.txt", "r+", encoding="utf-8") as file:
    for line, words in enumerate(file):
        words = words.split()
        print(f"{line+1} строка - {len(words)} слово(а)")


