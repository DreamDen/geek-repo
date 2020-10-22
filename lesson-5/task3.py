# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open("for_task3.txt", "r+", encoding="utf-8") as bonus:
    content = bonus.read()
    content = content.split()
    print(content)

num = []
name = []
looser = []

for i in content:
    if i.isdigit():
        num.append(int(i))
    elif i.isalpha():
        name.append(i)

sred = (sum(num) / len(name))


for i in content:
    if i.isdigit() and int(i) < 20:
        a = content.index(i)
        looser.append(content[a-1])

print(f"""На предприятии работает {len(name)} человек. 
Средний заработок равен {sred} у.е.""")
print(f"Сотрудники с окладом менее 20 у.е. {len(looser)} человек(а):")
for i, j in enumerate(looser):
    print(f"{i+1} - {j}")

