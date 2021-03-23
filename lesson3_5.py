def user_str(*args):
    my_list = [int(x) for x in args if x.isdigit()]
    return sum(my_list)


if __name__ == '__main__':
    result = 0
    while True:
        my_list = input('Enter numbers using space: ').split()
        if '$' in my_list:  # if $ meets in any place in list, else watch lesson3_5_2.py
            result += user_str(*my_list)
            print('Sum entered: %d' % user_str(*my_list))
            break
        else:
            result += user_str(*my_list)
            print('Sum entered: %d' % user_str(*my_list))
    print('Total sum is %d' % result)
