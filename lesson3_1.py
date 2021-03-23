def two_digits(num_a, num_b):
    return 0 if num_b == 0 else num_a / num_b


def two_digits_try(num_a, num_b):
    return num_a / num_b


if __name__ == '__main__':
    while True:
        try:
            num_a, num_b = input('Enter two numbers using "/": ').split('/')
        except ValueError:
            print('Bad arguments.')
        else:
            if num_a.isdigit() and num_b.isdigit():
                num_a, num_b = float(num_a), float(num_b)
                result = two_digits(num_a, num_b)
                print('The result is %04.2f' % result)
                break
            else:
                print('You had to enter numbers. Restarting the script...')
    try:
        result = two_digits_try(num_a, num_b)
    except ZeroDivisionError:
        print('Division by zero. Restart the script, please.')
    else:
        print('The result is %04.2f' % result)
