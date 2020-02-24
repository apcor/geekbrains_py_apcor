class Worker:
    _income = {"wage": 10, "bonus": 5}

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):

    def __init__(self, name, surname):
        super().__init__(name, surname, Worker._income)
        self.wage = Worker._income["wage"]
        self.bonus = Worker._income["bonus"]
        self.position = 'simple worker'

    def get_full_name(self):
        print(f'Полное имя: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Полный доход работника {self.name} {self.surname} '
              f'равен {self.wage + self.bonus}')


manager1 = Position('Иван', 'Иванов')
print(manager1.surname)
print(manager1.position)
manager1.get_full_name()
manager1.get_total_income()