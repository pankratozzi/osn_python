from abc import ABC, abstractmethod
import sys


class OwnException(Exception):

    def __init__(self, text, arg):
        self.text = text
        self.arg = arg

    def check_init(self):
        if self.arg.amortisation < 10:
            sys.stderr.write(str(self.text))
            return 0


class WareHouse:

    def __init__(self, name):
        self.name = name
        self.database_store = {}
        self.database_given = {}

    def get_item_store(self, *items):
        for item in items:
            self.database_store.update({item.id_num: item})

    @staticmethod
    def get_wh_state(database):
        counter = 0
        output = {}
        set_types = {type(x) for x in database.values()}
        for elem in tuple(set_types):
            for value in database.values():
                if isinstance(value, elem):
                    counter += 1
            output.update({elem.__name__: counter})
            counter = 0
        return output

    def give_good(self, item, dept):
        if WareHouse.validate_item(item, self.database_store):
            if WareHouse.validate(self.database_store.get(item.id_num).amortisation) \
                    and WareHouse.validate_service(item):
                self.database_store.pop(item.id_num)
                self.database_given.update({item.id_num: [item, dept]})
                dept.get_good(item)
                print('%s(%s) is given to %s.' % (item.name, item.id_num, dept.name))
            else:
                print('The device is too old!')
        else:
            print('The %s(%s) not stored in %s!' % (item.name, item.id_num, self.name))

    def get_good_back(self, item):
        self.get_item_store(item)

    def __str__(self):
        output = ''
        for k, v in self.database_store.items():
            output += 'Identifying number %s: %s\n' % (k, v)
        return self.name + ' =\n' + output

    @classmethod
    def validate(cls, amortisation):
        return 0 if amortisation < 10 or amortisation > 100 else 1

    @classmethod
    def validate_item(cls, item, storage):
        return 0 if not storage.get(item.id_num) else 1

    @classmethod
    def validate_service(cls, item):
        return 0 if not item.serviceable else 1


class OfficeEquipment(ABC):
    counter = 0

    def __init__(self, id_num, name, model):
        self.id_num = id_num
        self.name = name
        self.model = model
        self.amortisation = 100
        self.serviceable = True
        OfficeEquipment.counter += 1

    def __str__(self):
        output = ''
        for key in self.__dict__.keys():
            output += ('%s = %s.\t' % (key, getattr(self, key)))
        return output

    @abstractmethod
    def get_electricity(self):
        pass

    @abstractmethod
    def active(self):
        pass


class Printer(OfficeEquipment):
    counter_p = 0

    def __init__(self, id_num, model, q_blanks, name='Printer'):
        OfficeEquipment.__init__(self, id_num, name, model)
        self.q_blanks = q_blanks
        Printer.counter_p += 1

    @property
    def q_blanks(self):
        return self.__q_blanks

    @q_blanks.setter
    def q_blanks(self, value):
        if value < 0:
            self.__q_blanks = 10
        elif value > 10000:
            self.__q_blanks = 10000
        else:
            self.__q_blanks = value

    def get_electricity(self):
        return self.q_blanks * 20

    def printer(self, num_pr):
        if self.serviceable and num_pr <= self.q_blanks:
            self.q_blanks -= num_pr
            self.amortisation *= 0.99
            print('Printed %d lists. %d lists left.' % (num_pr, self.q_blanks))
            self.active()
        else:
            print('%s is unserviceable for that task.' % self.name)

    def active(self):
        if self.q_blanks == 0:
            self.serviceable = False


class Scanner(OfficeEquipment):
    counter_s = 0

    def __init__(self, id_num, model, quality, name='Scanner'):
        OfficeEquipment.__init__(self, id_num, name, model)
        self.quality = quality
        Scanner.counter_s += 1

    def get_electricity(self):
        return self.quality ** 0.5

    def scanning(self, img_q):
        self.amortisation *= 0.99
        self.active()
        if self.serviceable:
            print('Scanning with quality: %.2f' % (img_q * self.quality))
        else:
            print('%s is unserviceable.' % self.name)

    def active(self):
        if self.amortisation < 5:
            self.serviceable = False


class Copier(OfficeEquipment):
    counter_c = 0

    def __init__(self, id_num, model, velocity, name='Copier'):
        OfficeEquipment.__init__(self, id_num, name, model)
        self.velocity = velocity
        Copier.counter_c += 1

    def get_electricity(self, two_side=False):
        return (self.velocity * 2) * 220 if two_side else self.velocity * 220

    def copying(self, ls, two_side=False):
        self.active()
        if self.serviceable and two_side:
            print('%d copies made.' % ls * self.velocity)
        elif self.serviceable:
            print('%d copies made.' % ls * self.velocity / 2)
        else:
            print('% is unserviceable for that task' % self.name)
        self.amortisation *= 0.99

    def active(self):
        if self.amortisation < 10:
            self.serviceable = False


class Department(ABC):

    def __init__(self, name):
        self.name = name
        self.storage = {}

    @abstractmethod
    def get_good(self, item):
        pass

    @abstractmethod
    def return_good(self, item, warehouse):
        pass


class Police(Department):

    def __init__(self, name='Police Dept.'):
        Department.__init__(self, name)

    def get_good(self, item):
        self.storage.update({item.id_num: item})

    def return_good(self, item, warehouse):
        print('%s(%s) returned to %s' % (item.name, item.id_num, warehouse.name))
        self.storage.pop(item.id_num)
        warehouse.get_good_back(item)

    def __str__(self):
        output = ''
        for k, v in self.storage.items():
            output += 'Identifying number %s :: %s\n' % (k, v)
        return self.name + ' =\n' + output


class ITRoom(Police):

    def __init__(self, name='IT-room'):
        super().__init__(name)

    def __call__(self, *args):
        for arg in args:
            if arg.amortisation < 100:
                arg.amortisation = 100
                arg.serviceable = True


if __name__ == '__main__':
    ware = WareHouse('Warehouse')
    dept_1 = Police('Police')
    printer_1 = Printer(534, 'Kyocera', 100)
    printer_1.printer(40)
    printer_2 = Printer(533, 'Xerox', 15000)
    printer_2.amortisation = 50
    copier = Copier(333, 'XeroxS', 40)
    scanner = Scanner(123, 'HP', 50)
    scanner.scanning(20)
    printer_1.amortisation = 50
    ware.get_item_store(printer_1, printer_2, copier, scanner)
    try:
        if printer_1.amortisation > 10:
            ware.give_good(printer_1, dept_1)
        else:
            raise OwnException('Cannot give good with amortisation less 10.', printer_1)
    except OwnException as exc:
        exc.check_init()
    print(ware)
    print(dept_1)
    print(ware.get_wh_state(dept_1.storage))
    dept_1.return_good(printer_1, ware)
    dept_2 = ITRoom('IT')
    ware.give_good(printer_2, dept_2)
    # scanner.serviceable = False
    ware.give_good(scanner, dept_2)
    dept_2.return_good(printer_2, ware)
    print(ware)
    print(dept_1)
    print(dept_2)
    print(ware.get_wh_state(ware.database_store))
    # print(ware.database_given)
    dept_2(printer_1, printer_2)
    print(ware)
    ware.give_good(scanner, dept_2)
