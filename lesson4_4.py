from random import randint as rn

my_list = [rn(0, i) for i in range(25)]
print('Start list: %s' % my_list)

my_new_list = [el for el in my_list if my_list.count(el) == 1]
print('Modified list: %s' % my_new_list)