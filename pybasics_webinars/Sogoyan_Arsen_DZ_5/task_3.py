with open('task_3_file.txt', 'r', encoding='utf-8') as my_file:
    w_data = my_file.read().split()

# generate a list of surnames of workers whose wages < 20000
wages_filtered = [w_data[i-1]
                    for i in range(1, len(w_data), 2)
                    if float(w_data[i]) < 20000]

# print out these surnames (comma-separated)
print(f'У следующих сотрудников зарплата меньше 20000:\n'
    f'{", ".join(wages_filtered)}.\n')

# generate a list with all the wages
all_wages = [float(w_data[i])
                    for i in range(1, len(w_data), 2)]

# calculate and print out average wage
print(f'Средняя зарплата на предприятии - '
    f'{sum(all_wages) / len(all_wages):.2f}')





