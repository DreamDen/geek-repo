my_list = [7, 5, 3, 3, 2]

print('''Сейчас начнётся добавление новых элементов 
в список, для выхода из добавления введите 123''')
num = int(input('Enter num: '))

while num != 123:
    for i in range(len(my_list)):
        if num == my_list[i]:
            my_list.insert(i + 1, num)
            break
        elif my_list[0] < num:
            my_list.insert(0, num)
        elif my_list[-1] > num:
            my_list.append(num)
        elif my_list[i] > num and my_list[i+1] < num:
            my_list.insert(i+1, num)
            break

    print(f'Total list: {my_list}')
    num = int(input('Enter num: '))



