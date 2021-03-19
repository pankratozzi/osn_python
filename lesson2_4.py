my_list = input('Enter words using space: ').split()
for i, word in enumerate(my_list, 1):
    print('%*d) \t%s' % (5, i, word[:10]))