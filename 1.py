from time import sleep
from itertools import cycle


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        z = 0
        for el in cycle("1"):
            if z > 0:
                break
            print(self.__color[0])
            sleep(7)
            print(self.__color[1])
            sleep(2)
            print(self.__color[2])
            sleep(7)
            print(self.__color[1])
            sleep(2)
            print(self.__color[0])
            z += 1
            continue


start = TrafficLight(["красный", "желтый", "зеленый"])
start.running()
