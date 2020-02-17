user_list = [3, 'great', True, 45.4, None, (5,6)]

for el in enumerate(user_list, 1):
    print(*el, type(el))


