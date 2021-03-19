my_list = input('Enter list values, using comma: ').split(',')
""" long case
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
    for i in range(0, len(my_list)-1, 2):
        tmp = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = tmp
    print(my_list)
else:
    print('You entered not enough arguments!')