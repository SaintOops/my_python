with open('temp.txt','r') as file:
    reader = file.read()

templist = list(map(float,reader.split('\n')))
print(f'макс. значение - {max(templist)}\nмин.значение - {min(templist)}\nуникальных значений - {len(set(templist))}')

import matplotlib.pyplot as plt
%matplotlib inline

x_coords = range(len(templist))
y_coords = templist

plt.plot(x_coords, y_coords)
plt.xlabel('Месяца')
plt.ylabel('Температура')
plt.show()
