import tkinter

def test():
    if entry.get().isdigit() :
        res.set(eval(entry.get() + '9/5 +32'))
    else:
        res.set('Ошибка ввода')

window = tkinter.Tk()
window.title('Конвертация')

res = tkinter.StringVar()

label = tkinter.Label(window, text = "Укажите температуру в Цельсиях:")
label.pack()
entry = tkinter.Entry(window)
entry.pack()
reslabel = tkinter.Label(window, textvariable = res)
reslabel.pack()

button = tkinter.Button(window, text = 'Конвертировать', command = test)
button.pack()
buttonex = tkinter.Button(window, text = 'Выход')
buttonex.pack()


window.mainloop()
