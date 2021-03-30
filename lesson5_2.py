import os


f_path = os.path.join(os.getcwd(), 'folder', 'text2.txt')
try:
    result = [line for line in open(f_path)]
    count = len(result)
except FileExistsError:
    print('File does not exist!')
else:
    print('Number of strings in file: %d.' % count)
    for i, line in enumerate(result, 1):
        print('Number of words in line %d: %d' % (i, len(line.split())))
