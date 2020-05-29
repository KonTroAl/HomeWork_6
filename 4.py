class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("go")

    def stop(self):
        print("stop")

    def turn(self, direction):
        print(direction)

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(self.name)

    def show_speed(self):
        if self.speed > 60:
            print("too much!")
        else:
            print(self.speed)


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(self.name)

    def show_speed(self):
        print(self.speed)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(self.name)

    def show_speed(self):
        if self.speed > 40:
            print("too much!")
        else:
            print(self.speed)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(self.name)

        if self.is_police == True:
            print("It's a police car")


camaro = SportCar(300, "Yellow", "Camaro", False)
camaro.go()
camaro.turn("Right")
camaro.show_speed()
camaro.stop()
lada = WorkCar(60, "green", "bread", False)
lada.go()
lada.turn("Right")
lada.show_speed()
lada.stop()
patriot = PoliceCar(120, "Blue", "Patriot", True)
patriot.go()
patriot.turn("Right")
patriot.show_speed()
patriot.stop()
rio = TownCar(90, "Red", "Rio", False)
rio.go()
rio.turn("Right")
rio.show_speed()
rio.stop()
