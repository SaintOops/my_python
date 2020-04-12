def do_append():
    with open('todo.json','r') as file:
        reader = file.read()
        reader.append({"category":entry2.get(), "name":entry1.get(), "time":entry3.get()})
    with open('todo.json','w') as file:
        file.write(reader)

def show_tasks():
    with open('todo.json','r') as file:
        reader = file.read()
    [print('Задача:',i["task"],'\nКатегория:',i["category"],'\nВремя:',i["time"]) for i in reader]
    

import tkinter

window = tkinter.Tk()
window.title('Менеджер задач')

label1 = tkinter.Label(window, text = 'Задача:')
label1.grid(row = 0, column = 0)
label2 = tkinter.Label(window, text = 'Категория:')
label2.grid(row = 1, column = 0)
label3 = tkinter.Label(window, text = 'Время:')
label3.grid(row = 2, column = 0)

entry1 = tkinter.Entry(window)
entry1.grid(row = 0, column = 1)
entry2 = tkinter.Entry(window)
entry2.grid(row = 1, column = 1)
entry3 = tkinter.Entry(window)
entry3.grid(row = 2, column = 1)

button1 = tkinter.Button(window, text = 'Заказать', command = do_append)
button1.grid(row = 4, column = 1)
button2 = tkinter.Button(window, text = 'Список задач', command = show_tasks)
button2.grid(row = 5, column = 1)
button3 = tkinter.Button(window, text = 'Выход')
button3.grid(row = 6, column = 1)


window.mainloop()
