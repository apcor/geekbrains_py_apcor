# t_sec = int(input('Введите время в секундах: '))
t_inp = 71251
t_h = t_inp // 3600
t_m = (t_inp % 3600) // 60
t_s = t_inp % 60

print(f'{t_inp} секунд - это {t_h}:{t_m}:{t_s}')
