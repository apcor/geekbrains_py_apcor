input_str = 'кошка собака лошадь хомяк птеродактиль броненосеццццц'

input_list = input_str.split()

for ind, el in enumerate(input_list, 1):
    print(ind, el[:10], end ='\n')


