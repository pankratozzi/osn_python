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