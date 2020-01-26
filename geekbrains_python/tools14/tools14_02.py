import random

num_list =[random.randint(-50,50) for i in range(1,15)]

print(num_list)

result = [num for num in num_list if num%3 == 0 and num > 0 and num%4 != 0]

print(result)