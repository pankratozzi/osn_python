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
task6()