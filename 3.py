class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        print(f"Сотрудника данной фирмы зовут: {self.name} {self.surname}!")

    def get_total_income(self):
        result = self._income["Оклад"] + self._income["Премия"]
        print(f"Суммарная заработная плата сотрудника с учетом премии: {result} рублей!")


geolog = Position("Константин", "Трошенькин", "Геолог-програмист", {"Оклад": 200000, "Премия": 5000000})
geolog.get_full_name()
geolog.get_total_income()
