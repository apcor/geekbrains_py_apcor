import random

min = 1
max = 100
count = 0

num_comp = random.randint(min, max)
print(f"Загадайте число от 0 до 100. Я постараюсь его отгадать! \n \n Если моё число меньше загаданного, введите >. Больше - <. Если угадал - знак равенства =. \n Вы загадали {num_comp}? ")

user_sign = input(">   <   =     ")

while not user_sign == "=":
    if user_sign == ">":
        min = num_comp+1

    elif user_sign == "<":
        max = num_comp-1

    num_comp = random.randint(min, max)
    user_sign = input(f"Вы загадали {num_comp}? ")
    count +=1

print(f"Я угадал загаданное число {num_comp} c {count+1}-ой попытки, ура!")