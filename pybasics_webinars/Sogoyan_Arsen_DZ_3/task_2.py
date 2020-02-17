def get_user_info(name, surname, y_o_b, city, email):
    return f'{name} {surname} живет в городе {city}, ' \
           f'год рождения - {y_o_b}, email - {email}.'


print(get_user_info(surname = 'Петров', city = 'Москва',
                    y_o_b = 1985, name = 'Михаил', email = 'm@pet.ru'))
