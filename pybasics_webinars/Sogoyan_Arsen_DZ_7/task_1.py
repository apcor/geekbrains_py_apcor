class Matrix:
    def __init__(self, mx_list):
        self.input_list = mx_list
        self.dim_rows = len(mx_list)
        self.dim_cols = len(mx_list[0])
        self.mx_items = str([el for row in mx_list for el in row])

    def __str__(self):
        return '\n'.join(['\t'.join([str(el) for el in row]) for row in self.input_list]) + '\n'

    def __add__(self, other):
        mtx_sum = [[sum(item) for item in zip(*rows)] for rows in zip(self.input_list,other.input_list)]
        return Matrix(mtx_sum)


a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
c = Matrix([[2, 2, 2], [3, 3, 3], [4, 4, 4]])
print(a)
print(b)
print(c)
d = a + b + c
print(d)


