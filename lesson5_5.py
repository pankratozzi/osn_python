import os

f_path = os.path.join(os.getcwd(), 'folder', 'text5.txt')
while True:
    numbers = input('Enter numbers, using space: ')
    if not numbers.replace(' ', '').replace('.', '').replace('-', '').isdigit():
        print('Enter numbers only!')
    else:
        break

with open(f_path, 'w+', encoding='utf-8') as file:
    file.write(numbers)
    file.seek(0)
    content = file.read().split()
    content_sum = sum([float(x) for x in content])
print('Sum of numbers in "%s": %.2f' % (file.name[-9:], content_sum))
