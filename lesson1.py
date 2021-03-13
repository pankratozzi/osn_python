#task1
def task1():
    some_var1 = 'some value'
    some_var2 = 32
    some_var = 3.52
    print(f'First var {some_var}, second var {some_var1}, third var {some_var2}')
    some_var = input('enter string: ')
    some_var1 = int(input('enter int value: '))
    some_var2 = float(input('enter float value: '))
    if type(some_var) == str and type(some_var1) == int and type(some_var2) == float:
        print('First var {0}, second var {1}, third var {2}'.format(some_var, some_var1, some_var2))
    else:
        print('error')
#task2
def task2():
    date_user = int(input('Enter seconds: '))
    if date_user >= 86400:
        date_user = (date_user - (date_user // 86400)*86400)
    if date_user >= 3600:
        hours = date_user // 3600
        minutes = (date_user - (hours * 3600)) // 60
        seconds = date_user - hours*3600 - minutes*60
    else:
        hours = 0
        minutes = date_user // 60
        seconds = date_user - minutes * 60
    print(f'{hours:0>2}::{minutes:0>2}::{seconds:0>2}')

#task3
def task3():
    number_n = input('enter int value in range 1..9: ')
    while True:
        if not number_n.isdigit() or int(number_n) not in range(1, 9):
            number_n = input('enter again: ')
            continue
        else:
            list_num = []
            number_list = ''
            for x in range(3):
                number_list += number_n
                list_num.append(number_list)
            list_num = list(map(lambda y: int(y), list_num)) #list_num = [int(y) for y in list_num]
            print(list_num)
            result = sum(list_num)
            print('result is:\t%*d' % (2, result))
            break
#task4
def task4():
    list_numbers = ''
    while not list_numbers.isdigit() or int(list_numbers) <= 0:
        list_numbers = input('enter int positive number: ')
    array = [int(x) for x in list_numbers]
    for (i, list) in enumerate(array): print('%s)---%d' % (i+1, list), end='\t')
    """
    array = []
    for x in range(len(list_numbers)):
        array.append(list_numbers[x]) # append(int(list_numbers[x]))
    array = list(map(lambda x: int(x), array)) # array = [int(x) for x in list_numbers]
    """
    dd = dict(zip(range(len(array)), array))
    print('\nNew dictionary: ', dd)
    max_val = array[0]
    """ 1 - case: with first member
    for x in range(len(list_numbers)):
        if array[x] > max_val:
            max_val = array[x]
    """
    # 2 - case with std func: max_val = max(array)
    for x in array[1:]:
        if x > max_val:
            max_val = x
    print('Maximum digit is -', max_val)

#task5
def task5():
    fin_unit = input('Enter value of vyr and izd using space: ').split()
    try:
        fin_unit = list(map(lambda x: int(x), fin_unit))
        difference = fin_unit[0]-fin_unit[1]
        if difference <=0:
            print(f'{difference} ubytok')
        else:
            print(f'{difference} is your prib')
            rent = round((difference / fin_unit[0]) * 100, 2)
            print(f'{rent} is your rent')
            number_work = int(input('enter number of workers: '))
            abs_value = round(difference / number_work, 2)
            print(f'{abs_value} is absolute prib for workers')
    except:
        print('Probably your entered only one value')
        task5()

#task6
def task6():
    km_result = input('Enter start distance and desire distance using comma:').split(',')
    km_result = [float(x) for x in km_result] #list(map(lambda x: float(x), km_result))
    if km_result[0] < km_result[1]:
        counter = 1
        while km_result[0] <= km_result[1]:
            print(f'{counter} day the distance is: {km_result[0]:.2f} km')
            counter += 1
            km_result[0] *= 1.1
            #km_result[0] = round(km_result[0], 2)
        print(f'{counter} day the distance is: {km_result[0]:.2f} km')
        print(f'You need {counter} days to reach your target')
    else:
        print('You have already reached your target')

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
        continue