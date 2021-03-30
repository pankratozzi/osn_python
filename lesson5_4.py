import re
import os

f_path = os.path.join(os.getcwd(), 'folder', 'text4.txt')


def find_and_replace(pattern, line, text_new):
    occurences = re.findall(pattern, line, re.IGNORECASE)
    if len(occurences):
        for occurence in occurences:
            line = line.replace(occurence, text_new)
    return line


str_digits = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре'}
lines = open(f_path, 'r', encoding='utf-8').readlines()
new_lines = []
# with list generator
# new_lines = [line.replace(line.split('-')[0], str_digits.get(int(line.split('-')[1]))) for line in lines]
for line in lines:
    tmp_line = line.split('-')
    line = line.replace(tmp_line[0], str_digits.get(int(tmp_line[1])))
    new_lines.append(line)
with open(r'folder/text4_2.txt', 'w', encoding='utf-8') as file:
    file.writelines(new_lines)

str_digits = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_lines = [find_and_replace(line.split('-')[0], line, str_digits.get(line.split('-')[0])) for line in lines]
with open(r'folder/text4_3.txt', 'w', encoding='utf-8') as file:
    file.writelines(new_lines)
