time = int(input("Введите время в секундах - "))
hour = time // 3600
minutes = time // 60
sec = time - minutes*60

print(f"{hour} : {minutes} : {sec}")
