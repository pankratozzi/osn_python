def my_pow_a(x, y):
    res = 1
    if y == 0:
        return 1
    elif y > 0:
        for i in range(y):
            res *= x
        return res
    else:
        for i in range(abs(y)):
            res *= x
        return 1 / res


def my_pow_neg(x, y):
    def my_pow_pos(x, y):
        return 1 if y == 0 else x * my_pow_pos(x, y - 1)
    return 1 / my_pow_pos(x, abs(y))


def my_pow_b(x, y):
    return 1 if y == 0 else x ** y


if __name__ == '__main__':
    # 1. with for
    res = my_pow_a(2, -4)
    print(res)
    # 2. with recursion
    res = my_pow_neg(2, -4)
    print(res)
    # 3. with operator
    res = my_pow_b(2, -4)
    print(res)
    # 4. with lambda
    res = lambda x, y: x ** y
    print(res(2, -4))
    # 5. test with builtin function
    print(pow(2, -4))
