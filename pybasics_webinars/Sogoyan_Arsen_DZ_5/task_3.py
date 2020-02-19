with open('task_3_file.txt', 'r', encoding='utf-8') as my_file:
    w_data = my_file.read().split()
    wages_filtered = [w_data[i-1]
                      for i in range(1, len(w_data), 2)
                      if int(w_data[i]) < 20000]
    print(f'У следующих сотрудников зарплата меньше 20000:\n'
          f'{", ".join(wages_filtered)}.')

    all_wages = [int(w_data[i])
                      for i in range(1, len(w_data), 2)]
    print(f'Средняя зарплата на предприятии - '
          f'{sum(all_wages) / len(all_wages):.2f}')





