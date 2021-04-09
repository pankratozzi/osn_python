import sys


class OwnException(Exception):

    res_list = []

    def __init__(self, text, arg):
        self.text = text
        self.arg = arg

    def check_list(self):
        if self.arg.replace('-', '').isdigit():
            OwnException.res_list.append(int(self.arg))
        else:
            sys.stderr.write('\nValue must not be string: ')


if __name__ == '__main__':
    while True:
        try:
            value = input('Enter digit or type "stop":')
            if value.lower().replace(' ', '') == 'stop':
                break
            raise OwnException('String!', value)
        except OwnException as exc:
            exc.check_list()
    print(OwnException.res_list)
