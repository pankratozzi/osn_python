from random import randint as rn

def task1():
    my_list = []
    type_list = ['str', 'int', 'float', 'list', 'tuple', 'set', 'complex']
    tp = """
    Enter string, integer, float, list (like: 123abc), tuple (like: 123abc), 
    dictionary values (like: 123abc), set (like: 123abc), complex (like: 12)
    Start typing...
    """
    print(tp)
    cnt = 0
    while len(my_list) < len(type_list):
        my_list.append(input('Enter {0}: '.format(type_list[cnt])))
        cnt += 1
    my_list = [eval(type_list[x])(my_list[x]) for x in range(len(my_list))]
    new_val = input('Enter dictionary values using space: ').split()
    my_list.append(dict(zip(range(1, len(new_val)+1), new_val)))
    if my_list:
        for x in my_list:
            print('%s has type: %s' % (x, type(x)))
    else:
        print('You entered not enough data.')
def task2():
    my_list = input('Enter list values, using comma: ').split(',')
    """
    if my_list and len(my_list) % 2 == 0:
        for i in range(0, len(my_list), 2):
            tmp = my_list[i]
            my_list[i] = my_list[i+1]
            my_list[i+1] = tmp
    elif my_list and len(my_list) != 0:
        for i in range(0, len(my_list)-1, 2):
            tmp = my_list[i]
            my_list[i] = my_list[i+1]
            my_list[i+1] = tmp
    """
    if len(my_list) > 1:
        for i in range(0, len(my_list) - 1, 2):
            tmp = my_list[i]
            my_list[i] = my_list[i + 1]
            my_list[i + 1] = tmp
        print(my_list)
    else:
        print('You entered not enough arguments!')
def task3():
    my_dict = {'winter': [1, 2, 12],
               'spring': [3, 4, 5],
               'summer': [6, 7, 8],
               'autumn': [9, 10, 11]}
    while True:
        month = input('Enter number of month: ')
        if month.isdigit() and int(month) in range(1, 13):
            month = int(month)
            for k, v in my_dict.items():
                if month in v:
                    print('The season is: %s' % k)
            break
        else:
            print('Enter month in range 1..12!')
def task4():
    my_list = input('Enter words using space: ').split()
    for i, word in enumerate(my_list, 1):
        print('%*d) \t%s' % (5, i, word[:10]))
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
def task6():
    list_names = ['name', 'price', 'quantity', 'unit']
    list_dict = []
    while True:
        list_values = input('Enter name, price, quantity, unit, using comma (then type "stop"): ').split(',')
        if len(list_values) == 4:
            try:
                list_values[1] = float(list_values[1])
                list_values[2] = int(list_values[2])
            except ValueError:
                print('Price and quantity should be float and integer. Your previous data was lost.\nStart your database from the begining')
                return task6()
            else:
                list_dict.append(dict(zip(list_names, list_values)))
        elif ''.join(list_values) == 'stop':
            break
        else:
            print('Please, enter 4 parameters')
    final_list = [(i, d) for i, d in enumerate(list_dict, 1)]
    if len(final_list):
        print('Your dataset:\n %s \n' % final_list)
        temp_list = [[list_dict[i][k] for i in range(len(list_dict))] for k in list_names]
        for i in range(len(temp_list)): # if we have same goods with different prices or same prices - this would not be correct
            for elem in temp_list[i][:]:
                if i != 2 and temp_list[i].count(elem) > 1: # i != 2 for not to lose total quantity
                    temp_list[i].remove(elem)
        """ if using trick with sets
        for i in range(len(temp_list)):
            if i != 2:
                temp_list[i] = set(temp_list[i])
                temp_list[i] = list(temp_list[i])
        """
        final_dict = {k: v for k, v in zip(list_names, temp_list)}
        print('Analized dictionary is: %s\n' % final_dict)

while True:
    command = input('enter command, like task1, task2, task3, etc. or type exit:')
    if command == 'task1':
        task1()
    elif command == 'task2':
        task2()
    elif command == 'task3':
        task3()
    elif command == 'task4':
        task4()
    elif command == 'task5':
        task5()
    elif command == 'task6':
        task6()
    elif command == 'exit':
        print('experiment is over')
        break
    else:
        print('Wrong command')