# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func()

def my_func(words):
    for i in words:
        if 97 <= ord(i) <= 122 or ord(i) == 32:
            pass
        else:
            words = words.replace(i, "", 1)
    words = words.split()
    for num, word in enumerate(words):
        words[num] = word.capitalize()
    words = " ".join(words)

    return words

print(my_func(input("Введите предложение: ")))