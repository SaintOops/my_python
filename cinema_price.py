name=input("Введите название фильма:\n")
date=input("Выберите дату фильма(сегодня,завтра):\n")
time=int(input("Выберите время фильма:\n"))
quantity=int(input("Количество билетов:\n"))
if name=="Паразиты":
    if time==12:
        ans=250
    elif time==16:
        ans=350
    else:
        ans=450
if name=="1917":
    if time==10:
        ans=250
    elif time==13 or time==16:
        ans=350
if name=="Соник в кино":
    if time==10:
        ans=350
    elif time==14 or time==18:
        ans=450
ans*=quantity
if date=="сегодня" and quantity>=20:
    sale=0.25
elif date=="сегодня":
    sale=0.05
elif quantity>=20:
    sale=0.2
print("Суммарная стоимость билетов", ans*(1-sale), "руб.")
input("\n\nНажмите Enter. чтобы выйти")





