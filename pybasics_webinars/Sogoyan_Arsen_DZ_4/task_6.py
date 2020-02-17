from itertools import count, cycle

start_int = 8
end_int = 25

for el in count(start_int):
    if el > end_int:
        break
    else:
        print(el, end = ' ')
print()

counter = 0
for el in cycle('geekbrains'):
    if counter > end_int:
        break
    else:
        print(el, end = '_')
        counter += 1


