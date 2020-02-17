def my_func(x, y):
    pow = 1
    for i in range(0, abs(y)):
        pow /= x
    return pow


num1 = 9
num2 = -3

print(my_func(num1, num2))
