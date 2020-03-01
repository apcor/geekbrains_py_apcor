class Cell:

    def __init__(self, unit_num):
        try:
            if unit_num > 0:
                self.unit_num = unit_num
            else:
                raise Exception('Отрицательное кол-во ячеек!')
        except Exception as e:
            print(e)

    def __str__(self):
        return f'Клетка  [{"*" * self.unit_num}]'

    def __add__(self, other):
        sum_units = self.unit_num + other.unit_num
        return Cell(sum_units)

    def __sub__(self, other):
        try:
            dif_units = self.unit_num - other.unit_num
            return Cell(dif_units)
        except Exception as e:
            print('Нельзя вычесть клетки!', e)

    def __mul__(self, other):
        mul_units = self.unit_num * other.unit_num
        return Cell(mul_units)

    def __truediv__(self, other):
        div_units = self.unit_num // other.unit_num
        return Cell(div_units)

    def make_order(self, row_units):
        print(f'[', end='')
        for idx in range(self.unit_num // row_units):
            print(f'{"*" * row_units}')
        print(f'{"*" * (self.unit_num % row_units)}]')


if __name__ == '__main__':
    cell_1 = Cell(27)
    cell_1.make_order(11)


