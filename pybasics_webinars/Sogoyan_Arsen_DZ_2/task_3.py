# user_num = int(input('Введите номер месяца'))

user_num = 8

seasons_list = [[12, 1, 2, 'зима'], [3, 4, 5, 'весна'], [6, 7, 8, 'лето'], [9, 10, 11, 'осень']]
seasons_dict = {
    (12, 1, 2): 'зима',
    (3, 4, 5): 'весна',
    (6, 7, 8): 'лето',
    (9, 10, 11): 'осень',
}

for el in seasons_list:
    if user_num in el:
        print(el[3])

for el in seasons_dict.keys():
    if user_num in el:
        print(seasons_dict[el])

