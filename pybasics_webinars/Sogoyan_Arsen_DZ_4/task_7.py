import math


def fact(n):
    for el in range(1, n+1):
        yield math.factorial(el)


check_int = 15
for idx, i in enumerate(fact(check_int)):
    print(f'Факториал {idx+1} равен {i}')
