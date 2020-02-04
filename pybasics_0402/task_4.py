# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.


# user_inp = int(input('Введите целое положительное число: '))
user_inp = 13764328761308748231

max_digit = user_inp % 10

while not user_inp == 0:
    if user_inp % 10 >= max_digit:
        max_digit = user_inp % 10
    user_inp //= 10

print(max_digit)
