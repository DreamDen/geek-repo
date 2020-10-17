num = int(input("Введите целое число - "))
print(num)
a = None
max_a = 0

while num != 0:
	a = num % 10
	num = num // 10
	if a > max_a:
		max_a = a
	
print("Cамая большая цифра в Вашем числе:", max_a)

