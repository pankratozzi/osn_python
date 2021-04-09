import sys
from datetime import date as dt
import traceback


class Date:
    default_date = dt.today()
    __date_list = ['day', 'month', 'year']

    def __init__(self, date):
        self.date = date

    def __str__(self):
        return 'Your date is: %s' % self.date

    @classmethod
    def get_date(cls, value):
        if Date.validate_date(value):
            value = value.split('-')
            value = (int(x) for x in value if x.isdigit())
            value_dict = dict(zip(cls.__date_list, value))
            return value_dict
        else:
            return cls.default_date

    @staticmethod
    def validate_date(value):
        try:
            value = value.split('-')
            for x in value:
                if not x.isdigit():
                    raise ValueError
            if len(value) != 3:
                raise IndexError
        except ValueError:
            print(f'Non digit!:\n, {traceback.format_exc()}')
            return 0
        except IndexError:
            print(f'Have to be 3 parameters:\n, {traceback.format_exc()}')
            return 0
        except AttributeError:
            return f'Wrong attribute:\n, {traceback.format_exc()}'
        else:
            if len(value[0]) != 2 or int(value[0]) not in range(1, 32):
                sys.stderr.write('Wrong parameter day.\n')
                return 0
            if int(value[1]) not in range(1, 13) or len(value[1]) != 2:
                sys.stderr.write('Wrong parameter month.\n')
                return 0
            if len(value[2]) != 4 or int(value[2]) not in range(-2000, 2022):
                sys.stderr.write('Wrong parameter year.\n')
                return 0
            else:
                return 1


if __name__ == '__main__':
    date_ex = Date('21-08-1988')
    get_data = date_ex.get_date(date_ex.date)
    get_data_2 = Date.get_date(date_ex.date)
    print(get_data, get_data_2, sep='\n')
    date_ex_1 = Date('str-08-1988')
    get_data_3 = Date.get_date(date_ex_1.date)
    date_ex_2 = Date('15-1988')
    get_data_4 = Date.get_date(date_ex_2.date)
    date_ex_3 = Date('10-15-1988')
    get_data_5 = Date.get_date(date_ex_3.date)
    print(get_data_5)
