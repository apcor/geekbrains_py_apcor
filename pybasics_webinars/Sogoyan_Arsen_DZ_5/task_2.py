with open('task_2_file.txt', 'r', encoding = 'utf-8') as my_file:
    qty_lines = len(my_file.readlines())
    print(f'Количество строк в файле {my_file.name} - {qty_lines}.')
    my_file.seek(0)
    for _ in range(qty_lines):
        print(f'В строке №{_+1}  -  {len(my_file.readline().split())} слов.')

# Insert a line and reset the cursor
    print('\n')
    my_file.seek(0)


# Alternative solution

    test = my_file.read().splitlines()
    for _ in range(len(test)):
        print(f'В строке №{_+1}  -  {len(test[_].split())} слов.')
    print(f'Количество строк в файле {my_file.name} - {len(test)}.')


