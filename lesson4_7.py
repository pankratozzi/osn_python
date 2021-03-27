def fact(n):
    if n == 1:
        yield 1
    else:
        for x in fact(n - 1):
            yield x
        yield x * n


def fact_u(n):
    return 1 if n == 0 else n * fact_u(n - 1)


def fact_y(n):
    y = 1
    for i in range(1, n + 1):
        y *= i
        yield y


n = int(input('Enter digit to use in fact(): '))
for el in fact(n):
    print(el, end=' ')

print('\n')

for el in fact_y(n):
    print(el, end=' ')
