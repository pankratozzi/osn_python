from time import sleep
from itertools import cycle
from random import randint

"""
не до конца понял смысл проверки последовательности переключения,
если в задании стоит жесткое условие на переключение
"""


class TrafficLight:
    __cnt = 0
    __color = [['red', 7], ['yellow', 2], ['green', 3]]

    def __init__(self, stop=randint(5, 25)):  # may define local var stop in running
        self.stop = stop

    @property
    def stop(self):
        return self.__stop

    @stop.setter
    def stop(self, stop):
        if stop > 25 or stop <= 0:
            self.__stop = 25
        else:
            self.__stop = stop

    def running(self):
        print('Battery charge: %.2f%%' % ((self.stop / 25) * 100))
        try:
            for x in cycle(TrafficLight.__color):
                print('The traffic light is: %s' % x[0])
                sleep(x[1])
                TrafficLight.__cnt += 1
                if TrafficLight.__cnt == self.stop:
                    raise StopIteration
        except StopIteration:
            print('Low battery!')
            return


class TrafficLightN:
    __color = None

    def __init__(self):
        self.__history = ['start']  # PyCharm raises warning if define self.list outside __init__

    def running(self, color):
        TrafficLightN.__color = color
        try:
            if TrafficLightN.__color == 'red' and self.__history[-1] not in ('yellow', 'red'):
                print('The traffic light is: %s' % self.__color)
                sleep(7)
            elif TrafficLightN.__color == 'yellow' and self.__history[-1] not in ('yellow', 'green'):
                print('The traffic light is: %s' % self.__color)
                sleep(2)
            elif TrafficLightN.__color == 'green' and self.__history[-1] not in ('green', 'red'):
                print('The traffic light is: %s' % self.__color)
                sleep(2)
            else:
                raise ValueError
        except ValueError:
            print('%s is Wrong color!' % TrafficLightN.__color)
            return
        else:
            self.__history.append(TrafficLightN.__color)
            self.__history.pop(0)


class TrafficLightA:
    def __init__(self):
        self.history = ['start']
        self.__color = None

    def running(self, color):
        self.__color = color
        try:
            if self.__color == 'red' and self.history[-1] not in ('yellow', 'red'):
                print('The traffic light is: %s' % self.__color)
                sleep(7)
            elif self.__color == 'yellow' and self.history[-1] not in ('yellow', 'green'):
                print('The traffic light is: %s' % self.__color)
                sleep(2)
            elif self.__color == 'green' and self.history[-1] not in ('green', 'red'):
                print('The traffic light is: %s' % self.__color)
                sleep(2)
            else:
                raise ValueError
        except ValueError:
            print('%s is Wrong color!' % self.__color)
            return
        else:
            self.history.append(self.__color)
            self.history.pop(0)


t_light = TrafficLight(6)
t_light.running()

new_t_light = TrafficLightN()
new_t_light.running('red')
new_t_light.running('yellow')
new_t_light.running('green')
new_t_light.running('red')
new_t_light.running('green')

new_t_light_v2 = TrafficLightA()
new_t_light_v2.running('red')
new_t_light_v2.running('yellow')
TrafficLightA.running(new_t_light_v2, 'red')
# new_t_light_v2.running('red')
new_t_light_v2.running('green')
