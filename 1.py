from time import sleep
from itertools import cycle


class bcolors:
    red = '\033[91m'
    yellow = '\033[93m'
    green = '\033[92m'


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        z = 0
        while True:
            if z < 3:
                print(bcolors.red + self.__color[0])
                sleep(7)
                print(bcolors.yellow + self.__color[1])
                sleep(2)
                print(bcolors.green + self.__color[2])
                sleep(7)
                new_list = [i for i in self.__color[::-1]]
                for el in range(1, 2):
                    print(bcolors.yellow + new_list[el])
                    sleep(2)
                z += 1
            else:
                print(bcolors.red + self.__color[0])
                break


start = TrafficLight(["красный", "желтый", "зеленый"])
start.running()
