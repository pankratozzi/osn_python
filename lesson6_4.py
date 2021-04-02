class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print('The %s moves with speed %s.' % (self.name, self.speed))

    def stop(self):
        print('The %s stops.' % self.name)

    def turn(self, direction):
        print('The %s turns %s' % (self.name, direction))

    def show_speed(self):
        print('The %s has speed %s' % (self.name, self.speed))

    def show(self):
        for key, value in sorted(self.__dict__.items()):
            print('%s = %s' % (key, getattr(self, key)), end='; ')
        print('', end='\n')

    def __str__(self):
        return '%s, %s, %s' % (self.__class__.__name__, self.__class__.__bases__, id(self))


class TownCar(Car):
    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 60:
            print('WARNING: speed limit of 60!')


class SportCar(Car):
    def accelerate(self, acs):
        self.speed += acs
        print('New speed of %s is %d' % (self.name, self.speed))


class WorkCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name)
        self.weight = 0

    def __add__(self, other):
        if isinstance(other, WorkCar):
            other = other.weight
        self.weight += other
        print('%s loaded with %d tonnes' % (self.name, other))
        return self

    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 40:
            print('WARNING: speed limit of 40!')


class PoliceCar(Car):
    cnt = 0

    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name)
        self.is_police = True
        PoliceCar.cnt += 1
        print('Number of police cars active: %s' % PoliceCar.cnt)

    @staticmethod
    def init_strike(*objects):
        for obj in objects:
            if obj.speed > 60:
                print('%s - slow down!' % obj.name)
            elif 'WorkCar' in str(type(obj)) and obj.speed > 40:
                print('Police calls: %s - slow down!' % obj.name)


t_car_1 = TownCar(50, 'black', 'KIA')
t_car_1.show()
t_car_2 = TownCar(70, 'rose', 'Ford')
t_car_2.show()
w_car_1 = WorkCar(30, 'blue', 'VW caddy')
w_car_1.show()
w_car_2 = WorkCar(50, 'white', 'Ford Transit')
w_car_2.show()
s_car = SportCar(100, 'red', 'Ferrari')
s_car.show()
p_car = PoliceCar(120, 'blue', 'BMW')
p_car.show()
t_car_2.go()
t_car_2.show_speed()
t_car_2.turn('left')
t_car_2.stop()
s_car.accelerate(50)
w_car_1 += 100
w_car_2 = w_car_2 + 50
p_car.init_strike(w_car_1, w_car_2, t_car_1, t_car_2, s_car)
print(p_car.name, p_car)
w_car_2.show()
