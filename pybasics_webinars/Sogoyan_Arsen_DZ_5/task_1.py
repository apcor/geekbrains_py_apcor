with open('task_1_file.txt', 'w', encoding = 'utf-8') as my_file:
    while True:
        user_str = input('Введите строку: ')
        my_file.writelines(f'{user_str} \n')
        if user_str == '':
            break

