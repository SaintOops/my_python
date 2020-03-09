tasks = []
while True:    
    num = int(input("""Простой todo: 
    1. Добавить задачу.
    2. Вывести список задач.
    3. Выход.
    
    Укажите число: """))
    
    if num == 1:
        task = input('Сформулируйте задачу: ')
        category = input('Добавьте категорию к задаче:')
        time = input('Добавьте время к задаче: ')
        tasks.append([task, category, time])
    elif num == 2:
        [print('Задача:',i[0],'Категория:',i[1],'Время:',i[2]) for i in tasks]
    elif num == 3:
        break
    else:
        print('Не верный ввод')
        break
