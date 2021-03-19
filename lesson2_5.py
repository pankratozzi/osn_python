from random import randint as rn

def task5():
    try:
        length = int(input('Enter length of list: '))
    except ValueError:
        print('Enter integer value!')
        return task5()
    else:
        my_list = sorted([rn(1, 10) for i in range(length)], reverse=True)
        print(my_list)
    while True:
        try:
            digit = int(input('Enter new digit for list: '))
        except ValueError:
            print('You had to enter digit!')
        else:
            if digit == 13:
                print('Goodbye!')
                break
            elif digit > max(my_list):
                my_list[:0] = [digit]
            elif digit < min(my_list):
                my_list.append(digit)
            elif digit in my_list:
                for i in range(len(my_list)-1, -1, -1):
                    if digit == my_list[i]:
                        my_list.insert(i+1, digit)
            else:
                my_list.append(digit)
                my_list.sort(reverse=True)
            print(my_list)
task5()