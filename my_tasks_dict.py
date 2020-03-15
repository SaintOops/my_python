tasks = []
while True:    
    num = int(input("""Простой todo: 
    1. Добавить задачу.
    2. Вывести список задач.
    3. Выход.
    
    Укажите число: """))
    
    if num == 1:
        taskV = input('Сформулируйте задачу: ')
        categoryV = input('Добавьте категорию к задаче:')
        timeV = input('Добавьте время к задаче: ')
        tasks.append({"task":taskV, "category":categoryV, "time":timeV})
    elif num == 2:
        [print('Задача:',i["task"],'\nКатегория:',i["category"],'\nВремя:',i["time"]) for i in tasks]
    elif num == 3:
        break
    else:
        print('Не верный ввод')
        break

