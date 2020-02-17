def int_func(text):
    return f'{chr(ord(text[0]) - 32)}{text[1:]}'

print(int_func('test'))

user_line_up = list(map(int_func, input('Введите слова латиницей '
                                        'с мал.буквы через пробел: ').split()))
print(*user_line_up)

