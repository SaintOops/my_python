name_code=input("Введите код города и длительность разговотра(в минтуах):\n")
code=int(name_code[:3])
if code==343:
    print("стотмость разговора:", int(name_code[3:])*15, "руб.")
elif code==381:
    print("стотмость разговора:", int(name_code[3:])*18, "руб.")
elif code==473:
    print("стотмость разговора:", int(name_code[3:])*13, "руб.")
elif code==485:
    print("стотмость разговора:", int(name_code[3:])*11, "руб.")
input("\n\nНажмите Enter. чтобы выйти")
