import json


with open('task_7_file.txt', 'r', encoding='utf-8') as source_file:
    firms_data = source_file.read().splitlines()

# generate respective lists for each piece of data
firm_names = [el.split()[0] for el in firms_data]
firm_forms = [el.split()[1] for el in firms_data]
firm_profits = [int(el.split()[2]) - int(el.split()[3]) for el in firms_data]

# print out a column of profit statements
for i in range(len(firms_data)):
    print(f'Прибыль фирмы {firm_forms[i]} {firm_names[i]} '
          f'равна {firm_profits[i]}')

# calculate average positive profits
pos_profits = [el for el in firm_profits if el >= 0]
average_profits = sum(pos_profits) / len(pos_profits)

# print out average profits
print(f'\nСредняя прибыль безубыточных фирм равна {average_profits:.2f}')

# create a list with two dicts inside
res_list = []
res_list.append({key: value for key, value in zip(firm_names, firm_profits)})
res_list.append({'average_profit': average_profits})

# create and open a new json file and write the list
with open('task_7_file.json', 'w', encoding='utf-8') as end_file:
    json.dump(res_list, end_file)




