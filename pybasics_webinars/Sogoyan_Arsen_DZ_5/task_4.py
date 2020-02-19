with open('task_4_file.txt', 'r', encoding='utf-8') as source_file:
    ref_dict = {
        'One': 'Один',
        'Two': 'Два',
        'Three': 'Три',
        'Four': 'Четыре',
        'Five': 'Пять',
        'Six': 'Шесть',
        'Seven': 'Семь',
        'Eight': 'Восемь',
        'Nine': 'Девять',
        'Ten': 'Десять',
    }
    source_data = source_file.read().splitlines()
    new_data = []
    for i in ref_dict.keys():
        for n in source_data:
            if i in n:
                new_data.append(n.replace(i, ref_dict[i]))


with open('task_4_file_new.txt', 'w', encoding='utf-8') as end_file:
    for el in new_data:
        end_file.writelines(f'{el}\n')

