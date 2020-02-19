import sys


def income_calc(hours, wage, bonus = 0):
    income = float(hours) * float(wage) + float(bonus)
    print(income)


try:
    income_calc(*sys.argv[1:])
except TypeError as e:
    print('Enter at least hours and wage as parameters, bonus is optional ', e)

