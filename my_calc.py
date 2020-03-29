def my_calc(x,y,oper):
        return eval(x+oper+y)
try:
    print(my_calc(input('число: '),input('число: '),input('оператор: ')))
except ZeroDivisionError:
    print('Ошибка деления на ноль')
