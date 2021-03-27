from sys import argv


def payment(hours, rate, bonus):
    return (hours * rate + bonus)


try:
    hours, rate, bonus = argv[1:]
except ValueError:
    print('You have entered incorrect parameters.')
else:
    my_list = [float(x) if x.replace('.', '').isdigit() else 1 for x in argv[1:]]
    res = payment(*my_list)
    print('#' * 20, 'Payment is: %s $' % res, '#' * 20)
