list_1 = ['бананы', 'яблоки', 'киви', 'апельсины', 'манго']
list_2 = ['манго', 'мандарины', 'виноград', 'гранаты','киви']

result = [fruit for fruit in list_1 if fruit in list_2]

print(result)