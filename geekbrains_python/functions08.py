def print_card(name, age, city):
    if age % 10 == 0 or age in range(5, 20):
        age_new = str(age)+" лет"
    elif age % 10 == 1:
        age_new = str(age)+" год"
    elif age % 10 in [2, 3, 4]:
        age_new = str(age)+" года"

    print(f'{name}, {age_new}, проживает в городе {city}.')

name = input("Введите имя: ")
age = int(input("Введите возраст: "))
city = input("Введите город: ")

print_card(name, age, city)