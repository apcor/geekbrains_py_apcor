import random

num_list =[random.randint(-100,100) for i in range(1,20)]
print(num_list)

def modify_list(list):
    list = list[:]
    return [element if element<0 else element**2 for element in list]

print(modify_list(num_list))
print(num_list)
