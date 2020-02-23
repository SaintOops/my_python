number=int(input("Введите число:\n"))
def even_q(x):
    if x%2==0:
        ans="\nчётное число"
    else:
        ans="\nнечётное число"
    return print(ans)
even_q(number)
input("\n\nНажмите Enter. чтобы выйти")
