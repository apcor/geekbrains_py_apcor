# word = 'слово'
# result = []
# for i in range(len(word)):
# #     if i % 2 != 0:
# #         result.append(word[i].lower())
# #     else:
# #         result.append(word[i].upper())
#
#     letter = result.append(word[i].lower()) if i%2!=0 else result.append(word[i].upper())
#
# print(''.join(result))
#-------------------------------------------------

# password = input('Введите пароль: ')
# print('Войти' if password == 'secret' else 'Вход запрещён')
#-------------------------------------------------

#numbers = [1, 2, 3, 4, 5, -1, -2, -3]

#классический способ
# result = []
# for number in numbers:
#     if number > 0:
#         result.append(number)
# print(result)

#через функцию filter
# result = filter(lambda number: number > 0, numbers)
# print(list(result))
#-------------------------------------------------

#через генератор
# result = [number for number in numbers if number > 0]
# print(result)

#-------------------------------------------------
#-------------------------------------------------


# pairs = [(1, 'a'), (2,'b'), (3, 'c')]

#классический способ
# result = {}
# for pair in pairs:
#     key = pair[0]
#     val = pair[1]
#     result[key] = val
# print(result)
#-------------------------------------------------

#через генератор
# result = {pair[0]:pair[1] for pair in pairs}
# print(result)

#Пример 1. Создать список случайных чисел от 1 до 100
# import random
# list100 = [random.randint(1, 100) for i in range(10)]
# print(list100)

#Пример 2. Создать список из квадратов чисел
# numbers = [1, 2, 3, -4]
#
# numbersq = [number**2 for number in numbers]
# print(numbersq)

# #Пример 3. Создать список имен на букву А
# names = ['Руслан','Дмитрий', 'Алексей', 'Андрей']
#
# names_a = [name for name in names if name[0] == 'А']
# print(names_a)

#-------------------------------------------------
#-------------------------------------------------


