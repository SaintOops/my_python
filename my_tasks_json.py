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
        with open('todo.json','r') as file:
            reader = file.read()
            reader.append({"category":categoryV, "name":taskV, "time":timeV})
        with open('todo.json','w') as file:
            file.write(reader)
    elif num == 2:
        with open('todo.json','r') as file:
            reader = file.read()
        [print('Задача:',i["task"],'\nКатегория:',i["category"],'\nВремя:',i["time"]) for i in reader]
    elif num == 3:
        break
    else:
        print('Не верный ввод')
        break
  
