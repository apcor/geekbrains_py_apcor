user_num = int(input('Введите число от 1 до 100: '))

def check_num(number):
    if number != 13:
        return number**2
    else:
        raise ValueError ('Нельзя вводить 13! ')

try:
    check_num(user_num)
except ValueError as e:
    print('Ошибка во введённом числе: ', e)
else:
    print(check_num(user_num))

