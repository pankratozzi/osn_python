from random import randint as rn

my_list = [rn(-10, 10) for _ in range(15)]
print('List: %s' % my_list)

my_new_list = [my_list[i + 1] for i in range(len(my_list) - 1) if my_list[i + 1] > my_list[i]]
print('New list is: %s' % my_new_list)
