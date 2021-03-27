from functools import reduce
import math

# alternative
# my_list = [x for x in range(100, 1001) if x % 2 == 0]

my_list = [x for x in range(100, 1001, 2)]
print('Generated list: %s' % my_list)
res = reduce(lambda x, y: x * y, my_list)
# outputs logistic result, because the int result is too big
print('The logistic result is: {:,.2f}'.format(math.log(res)))
