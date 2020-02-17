def get_div(num1, num2):
    """
    Returns result of division of 2 numbers

    :param num1: number
    :param num2: divisor of the number
    :return: result of division of num1 by num2 with check for division by zero
    """
    try:
        return num1 / num2
    except ZeroDivisionError as e:
        print('Zero division attempt: ', e)


# user_num1 = int(input('Введите первое число: '))
# user_num2 = int(input('Введите второе число: '))

user_num1 = 5
user_num2 = 0
print(get_div(user_num1, user_num2))