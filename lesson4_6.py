from itertools import count, cycle, combinations
import random


def counter(start, step=1, n=32):
    for i in count(start, step):
        if i > n: break
        yield i


while True:
    try:
        args = input('Enter start, step, number of iterations using space: ').split()
        if ''.join(args).lower() == 'stop': break
        args = [int(x) if x.isdigit() else 1 for x in args]
        result = list(counter(*args))
    except TypeError:
        print('Enter at least 1 argument!')
    else:
        for el in result:
            print(el, end=' ')
    print('\n')

new_list = [random.randint(1, 10) for _ in range(10)]
for x in combinations(new_list, len(new_list) - 1):
    c = 0
    x = list(x)
    random.shuffle(x)
    print('New list is: %s' % x)
    stop = random.choice(x)
    for el in cycle(x):
        if c == (stop * 2): break
        print(el, end=' ')
        c += 1
    print('\n')
