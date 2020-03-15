name = input("Введите название фильма:\n").title()
date = input("Выберите дату фильма(сегодня,завтра):\n").title()
time = input("Выберите время фильма:\n")
quantity = int(input("Количество билетов:\n"))

ans = 0
timetable={"Паразиты":{"t":{"12":250,"16":350,"20":450}},"1917":{"t":{"10":250,"13":350,"16":350}},"Соник в кино":{"t":{"10":350,"14":450,"18":450}}}

ans = timetable[name]["t"][time]*quantity

if date=="Cегодня" and quantity>=20:
    sale=0.25
elif date=="Cегодня":
    sale=0.05
elif quantity>=20:
    sale=0.2

if ans==0:
    print("неверный ввод")
else:
    print("Суммарная стоимость билетов", ans*(1-sale), "руб.")
