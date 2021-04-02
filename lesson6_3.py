"""
В задании говорится об атрибутах класса, но они общие для всех экземпляров,
логика получается странной. Делал через инициализацию атрибутов экземпляров
Куратор указал, что реализация должна быть такой
"""


class Worker:
    def __init__(self, name, surname, position, wage=100, bonus=50):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': int(wage), 'bonus': int(bonus)}

    def _inc(self):
        return self._income


class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        dictionary = super()._inc()  # equal Worker._inc(self)
        return dictionary['wage'] + dictionary['bonus']


person = Position('Bob', 'Marley', 'musician')
person_id = person.get_full_name()
income = person.get_total_income()
print('Worker %s has position %s and income: %s$' % (person_id, person.position, income))

pers = Position('Mark', 'Soul', 'broker', 500, 1000)
pers_id = pers.get_full_name()
pers_inc = Position.get_total_income(pers)
print('Worker %s has position %s and income: %s$' % (pers_id, pers.position, pers_inc))
