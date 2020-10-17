profit = int(input("Введите выручку Вашей фирмы за год: "))
loss = int(input("Введите издержки фирмы: "))
rent = (profit-loss) / profit
manager = 0
profit_man = 0

if profit > loss:
	print(f"Ваша компания работает в плюс. Прибыль составляет {profit-loss:.2f} руб.")
	print(f"Рентабельность: {rent}")
	manager = int(input("Сколько сотрудников работает в Вашей компании: "))
	profit_man = (profit - loss) / manager
	print(f"Каждый сотрудник приносит Вам: {profit_man:.2f} руб.")
elif profit < loss:
	print(f"Ваша компания работает в минус. Чтобы из него выйти подумайте как заработать {loss-profit:.2f} руб.")
elif profit == loss:
	print("Вы работаете в ноль. Разработайте план по увеличению прибыли")
else:
	print("Error") # не выводит если пишу строку. методами не пройденными в первом уроке пользоваться не стал. 

