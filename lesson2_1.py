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