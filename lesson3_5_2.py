"""
result is cumulatively increases which is incorrect, but why not
"""


def user_list():
    result = 0

    def user_str(*args):
        nonlocal result
        my_list = [int(x) for x in args if x.isdigit()]
        result += sum(my_list)
        print('Final sum entered: %d' % result)

    while True:
        my_list = input('Enter numbers using space: ').split()
        if '$' == my_list[-1]:  # any index in list: if '$' in my_list:
            user_str(*my_list)
            break
        else:
            user_str(*my_list)
    print('Total sum is %d' % result)


if __name__ == '__main__':
    user_list()
