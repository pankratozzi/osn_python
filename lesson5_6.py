import os

f_path = os.path.join(os.getcwd(), 'folder', 'text6.txt')


def sum_line(*line):
    res = 0
    for el in line:
        num = ''
        for w in el:
            if w.isdigit():
                num += w
        res += int(num)
    return res


with open(f_path, 'r', encoding='utf-8') as file:
    result = file.readlines()
list_lines = [sum_line(*line.split(':')[1].split()) for line in result]
list_subj = [x.split()[0] for x in result]
dictionary = {k: v for k, v in zip(list_subj, list_lines)}
print('Final dictionary is: %s' % dictionary)
