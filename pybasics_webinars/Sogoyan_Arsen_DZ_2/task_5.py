my_list = [7, 5, 3, 3, 2]

user_num = 1

for i in range(len(my_list[:])):
    if user_num >= my_list[i]:
        my_list.insert(i, user_num)
        break
    elif user_num <= my_list[-1]:
        my_list.append(user_num)
        break
    else:
        continue

print(my_list)