import math


def fact(n):
    y = 1
    for el in range(1, n+1):
        y *= el
        yield y


check_int = 15
for idx, i in enumerate(fact(check_int)):
    print(f'Факториал {idx+1} равен {i}')
