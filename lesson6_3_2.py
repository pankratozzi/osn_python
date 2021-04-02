"""
с использованием атрибутов класса, доступных для всех экземпляров
"""


class Worker:
    name = 'default'
    surname = 'default'
    position = 'janitor'
    _income = {'wage': 1000, 'bonus': 500}


class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname, Position.name + " " + Position.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


pex = Position()
pex.name = 'Bob'  # define exemplar's attr on place
pex.surname = 'Marley'
pex.position = 'musician'
bex = Position()
bex.name = 'Bill'
bex.surname = 'Murray'
bex.position = 'actor'
b_full_name = bex.get_full_name()
full_pex = pex.get_full_name()
inc_pex = Position.get_total_income(pex)
bex._income['wage'] = 2000  # warning! access to protected attr; change Worker._income - same for all exemplars
bex._income['bonus'] = 5000  # warning! access to protected attr; change Worker._income - same for all exemplars
bex_inc = bex.get_total_income()
print('%s has position %s and income: %d' % (b_full_name, bex.position, bex_inc))
print('%s has position %s and income: %d' % (full_pex, pex.position, inc_pex))
