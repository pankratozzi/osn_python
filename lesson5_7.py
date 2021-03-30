import json
import pickle
import os

f_path = os.path.join(os.getcwd(), 'folder', 'text7.txt')
with open(f_path, 'r', encoding='utf-8') as file:
    result = [line.split() for line in file]
sum_profit = 0
firm_res = {}
final_list = []
for x in result:
    x[2], x[3] = float(x[2]), float(x[3])
    if x[3] < x[2]:
        sum_profit += (x[2] - x[3])
    firm_res.update({x[0]: (x[2] - x[3])})
avg_dict = {'average profit': sum_profit}
final_list.extend([firm_res, avg_dict])
print(f'Final list is: {final_list}')

with open('folder/text.json', 'w') as j_file:
    json.dump(final_list, j_file)

with open('folder/text.pkl', 'wb') as j_file:
    pickle.dump(final_list, j_file)
