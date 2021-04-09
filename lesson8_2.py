import sys


class OwnException(Exception):
    def __init__(self, text):
        self.text = text


division = lambda a, b: a / b

try:
    arg_1, arg_2 = input('Enter two values using "/": ').split('/')
    arg_1, arg_2 = float(arg_1), float(arg_2)
    if arg_2 == 0:
        raise OwnException('Zero division!')
    result = division(arg_1, arg_2)
except ValueError:
    sys.stderr.write('Enter float numbers!')
except OwnException as error:
    sys.stderr.write(str(error))
else:
    print('The result is: %.2f' % result)
