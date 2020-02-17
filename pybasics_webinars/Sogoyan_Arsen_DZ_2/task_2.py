user_list = [3, 'great', True, 45.4, None, (5,6), 'seven']

# for el_1, el_2 in zip(user_list[::2], user_list[1::2]):
#
#     el_1, el_2 = el_2, el_1
#     user_list[user_list.index(el_1)] = el_2
#     user_list[user_list.index(el_2)] = el_1

for i in range(1, len(user_list),2):
    user_list[i], user_list[i-1] = user_list[i-1], user_list[i]


print(user_list)
