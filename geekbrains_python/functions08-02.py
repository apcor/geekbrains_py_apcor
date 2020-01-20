def calc_max(numbers):
    return max(numbers)
num = []
i = 1
while i<4:
    number = int(input(f"Введите {i}-ое число: "))
    num.append(number)
    i+=1
print(calc_max(num))
