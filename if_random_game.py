import random
num = int(input('number?'))
x = random.randint(1,4)
if num == x:
    print('won')
elif num > x:
    print('lower, lose')
else:
    print('upper, lose')
