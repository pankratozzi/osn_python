#task1
some_var1 = 'some value'
some_var2 = 32
some_var = 3.52
print(f'First var {some_var}, second var {some_var1}, third var {some_var2}')
some_var = input('enter string: ') #always string
some_var1 = int(input('enter int value'))
some_var2 = float(input('enter float value'))
if type(some_var) == str and type(some_var1) == int and type(some_var2) == float:
    print(f'First var {some_var}, second var {some_var1}, third var {some_var2}')
else:
    print('error')
#task2
date_user = input('Enter seconds less than 3600*24: ')
date_user = int(date_user)
if date_user >= 3600:
    hours = date_user // 3600
    minutes = (date_user - (hours * 3600)) // 60
    seconds = date_user - hours*3600 - minutes*60
else:
    hours = 0
    minutes = date_user // 60
    seconds = date_user - minutes * 60
print(f'{hours}::{minutes}::{seconds}')

#task3
number_n = input('enter int value in range 1..9: ')
while True:
    if not number_n.isdigit():
        number_n = input('enter again: ')
        continue
    elif int(number_n) not in range(1,9):
        number_n = input('enter again: ')
        continue
    else:
        list_num = []
        number_list = ''
        for x in range(0, 3):
            number_list += number_n
            list_num.append(number_list)
            list_num[x] = int(list_num[x])
        print(list_num)
        result = list_num[0] + list_num[1] + list_num[2]
        print(f'result is: {result}')
        break
#task4
list_numbers = ''
while not list_numbers.isdigit() or int(list_numbers) <= 0:
    list_numbers = input('enter int positive number')
array = []
for x in range(len(list_numbers)):
    array.append(list_numbers[x]) # append(int(list_numbers[x]))

array = list(map(lambda x: int(x), array)) # make object map as list and func

max = array[0]
for x in range(0, len(list_numbers)):
    if array[x] > max:
        max = array[x]
print(max)

#task5
fin_unit = list(input('Enter value of vyr and izd using space: ').split(' '))
#for x in range(0, len(fin_unit)):
#    fin_unit[x] = int(fin_unit[x])
for list in fin_unit:
    list = int(list)
difference = fin_unit[0]-fin_unit[1]
if difference <=0:
    print(f'{difference} ubytok')
else:
    print(f'{difference} is your prib')
    rent = round((difference / fin_unit[0]) * 100, 2)
    print(f'{rent} is your rent')
    number_work = int(input('enter number of users: '))
    abs_value = round(difference / number_work, 2)
    print(f'{abs_value} is absolute prib for workers')

#task6
km_result = list(input('Enter start distance and desire distance using comma').split(','))
km_result = list(map(lambda x: float(x), km_result))
counter = 1
while km_result[0] <= km_result[1]:
    print(f'{counter} day the distance is: {km_result[0]}')
    counter += 1
    km_result[0] *= 1.1
    km_result[0] = round(km_result[0], 2)
print(f'You need {counter} days')



