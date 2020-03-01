class Clothes():

    def __init__(self):
        self.name = None
        self._usage = None

    def calc_usage(self):
        return self._usage

    def __str__(self):
        return f'Экземпляр {self.name} класса Clothes, расход ткани - {self._usage} кв.м.'

    def __add__(self, other):
        sum_clothes = Clothes()
        sum_clothes._usage = self.calc_usage + other.calc_usage
        sum_clothes.name = f'сумма {self.name} и {other.name}'
        return sum_clothes


class Coat(Clothes):

    def __init__(self, size):
        super().__init__()
        self.name = 'Пальто'
        self.size = size
        self._usage = self.calc_usage

    @property
    def calc_usage(self):
        self._usage = self.size / 6.5 + 0.5
        return self._usage


class Suit(Clothes):

    def __init__(self, height):
        super().__init__()
        self.name = 'Костюм'
        self.height = height
        self._usage = self.calc_usage

    @property
    def calc_usage(self):
        self._usage = self.height * 2 + 0.3
        return self._usage


if __name__ == '__main__':

    obj_1 = Coat(13)
    obj_2 = Suit(5)
    print(obj_1)
    print(obj_2)

    obj_3 = obj_1 + obj_2
    print(obj_3)






