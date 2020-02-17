inventory = []
item_keys = ['название', 'цена', 'количество', 'ед.']
line_limit = int(input('Сколько позиций планируете внести в базу? '))
i = 1
item_vals = []
while i <= line_limit:
    item_vals.append(input('Название товара: '))
    item_vals.append(int(input('Цена товара: ')))
    item_vals.append(int(input('Количество: ')))
    item_vals.append(input('Единицы: '))
    item_dict = {el_i:el_v for el_i, el_v in zip(item_keys, item_vals)}
    inventory.append((i, item_dict))
    i += 1
    item_vals.clear()
print(inventory)

new_inventory = {el_i:[] for el_i in item_keys}
for item in inventory:
    for key in new_inventory.keys():
        new_inventory[key].append(item[1].get(key))

print(new_inventory)





