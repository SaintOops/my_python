translations = {"dog":"собака"}
# можно использовать более обширный словаь с переводами

import tkinter
import random

def test():
    if entry.get() == translations[word]:
        res.set('Угадали')
    else:
        res.set('Неугадали')

window = tkinter.Tk()
window.title('Игра')

word = random.choice(list(translations.keys()))
res = tkinter.StringVar()

label = tkinter.Label(window, text = f"Случайное слово:\n {word}\nУкажите перевод слова:")
label.pack()
entry = tkinter.Entry(window)
entry.pack()
reslabel = tkinter.Label(window, textvariable = res)
reslabel.pack()

button = tkinter.Button(window, text = 'Готово', command = test)
button.pack()
buttonex = tkinter.Button(window, text = 'Выход')
buttonex.pack()


window.mainloop()
