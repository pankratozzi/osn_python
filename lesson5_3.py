from datetime import datetime
import os


f_path = os.path.join(os.getcwd(), 'folder', 'text3.txt')
avg_sal = 0
try:
    result = [line.split() for line in open(f_path) if 'Average' not in line]
except FileExistsError:
    print('File does not exist!')
else:
    workers_poor = [x[0] for x in result if float(x[-1]) < 20000]
    avg_sal = sum([float(x[-1]) for x in result]) / len(result)
    avg_sal = round(avg_sal, 2)
    print('Poor workers: %s' % ', '.join(workers_poor))
    print('Average salary: %s' % avg_sal)
with open(f_path, 'r+', encoding='utf-8') as file:
    content = file.read()
    n = content.find('Average')
    if n != -1:
        file.seek(n)
        file.write('Average salary: %s = %s' % (avg_sal, datetime.now()))
    else:
        print('Average salary: %s = %s' % (avg_sal, datetime.now()), file=file)
