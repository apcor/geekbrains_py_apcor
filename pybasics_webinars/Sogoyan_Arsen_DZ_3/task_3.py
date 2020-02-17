def my_func(num1, num2, num3):
    return sum(sorted([num1, num2, num3], reverse = True)[:2])


print(my_func(4,7,3))