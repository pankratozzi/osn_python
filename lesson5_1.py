import os
from shutil import copytree, make_archive, rmtree


f_path = os.path.join(os.getcwd(), 'folder', 'text1.txt')
with open(f_path, 'w', encoding='utf-8') as file:
    while True:
        stdin = input('Enter line for file.txt: ')
        if not stdin:
            break
        file.write(stdin + '\n')
print('Write to file "%s", size: %s bytes' % (file.name[-9:], os.path.getsize(f_path)))
try:
    cp_folder = copytree(os.path.join(os.getcwd(), 'folder'), os.path.join(os.getcwd(), 'arc_folder'))
except FileExistsError:
    print('Folder already exists!')
finally:
    make_archive(os.path.join(os.getcwd(), 'arc_folder'), 'zip', os.getcwd())
if os.path.isdir('arc_folder'):
    rmtree(os.path.join(os.getcwd(), 'arc_folder'))
