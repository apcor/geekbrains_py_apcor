class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self, mass_m2, thickness):
        total_mass = self._length * self._width * mass_m2 * thickness / 1000
        print(f'Общая масса асфальта для строительства дороги '
              f'{self._length} м на {self._width} м равна {total_mass:.2f} т.')


a = Road(5000, 20)
a.calc_mass(25, 5)