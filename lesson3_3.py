from random import randint as rn


def my_func(numa, numb, numc):
    return sum(sorted([numa, numb, numc])[1:])


def my_func_c(*args):
    return sum(sorted(args, reverse=True)[:2])


if __name__ == '__main__':
    result = my_func(3, 5, 7)
    print('Sum of two max args: %.2f' % result)
    array = [rn(-100, 100) for i in range(100)]
    result = my_func_c(*array)
    print('Sum of two max from %d random args: %.2f' % (len(array), result))
