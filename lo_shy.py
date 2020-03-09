import random 
import numpy as np
m =  np.random.randint(1, 100, (3, 3))
length = len(m)
sum_d = sum([m[i][i] for i in range(length)])
sum_dd = sum([m[i][-1-i] for i in range(length)])
sums_count = (list(map(sum,m)) + list(map(sum,m.transpose()))).count(15)
numbers = [j for i in m for j in i if 0 <= j <= 9 ]
if len(numbers) == length**2 and sums_count == length*2 and sum_d == sum_dd == 15 and sum(numbers) == 45:
    print('Это квадрат Ло Шу')
else:
    print('Это не квадрат Ло Шу')
