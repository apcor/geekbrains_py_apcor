import sys

def income_calc(hours, wage, *args):
        income = float(hours) * float(wage) + float(*args)
        print(income)


try:
    income_calc(*sys.argv[1:])
except TypeError as e:
    print('Enter at least hours and wage as parameters, bonus is optional ', e)

