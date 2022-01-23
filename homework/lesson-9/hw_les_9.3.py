class Worker():
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(f'Total income is {self._income["wage"] + self._income["bonus"]}')


first_worker = Position('Max', 'Loren', 'manager', {'wage': 1000, 'bonus': 500})

first_worker.get_full_name()
first_worker.get_total_income()
