str_num = []
while True:
    str_num.extend(input('Введите числа через пробел: ').split())
    if 'q' in str_num:
        print(sum(map(int, str_num[:str_num.index('q')])))
        break
    else:
        print(sum(map(int, str_num)))






