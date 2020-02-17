def get_user_info(**kwargs):
    my_list = []
    for args in kwargs.values():
        my_list.append(str(args))
    return ' '.join(my_list)


print(get_user_info(surname = 'Петров', name = 'Михаил', city = 'Москва',year = 1985, email = 'm@pet.ru'))
