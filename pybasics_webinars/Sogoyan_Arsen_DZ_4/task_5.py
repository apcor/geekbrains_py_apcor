from functools import reduce


even_list = [el for el in range(100, 1001) if el % 2 == 0]

product = reduce(lambda x, y: x * y, even_list)
print(product)
