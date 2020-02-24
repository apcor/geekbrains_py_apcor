class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки: ручка {self.title}')


class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки: карандаш {self.title}')


class Handle(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки: маркер {self.title}')


one = Stationery('принадлежность')
one.draw()

two = Pen('шариковая')
two.draw()

three = Pencil('серый')
three.draw()

four = Handle('несмываемый')
four.draw()
