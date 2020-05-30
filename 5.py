class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск программы")


class Pen(Stationery):
    def draw(self):
        print("Ручка")


class Pencil(Stationery):
    def draw(self):
        print("Карандаш")


class Handle(Stationery):
    def draw(self):
        print("Маркер")


letter = Stationery("Привет!")
letter.draw()
letter_1 = Pen("Привет!")
letter_1.draw()
letter_2 = Pencil("Привет!")
letter_2.draw()
letter_3 = Handle("Привет!")
letter_3.draw()