list = ['самовар','весно','лето']
from random import randint
word = list[randint(0,(len(list)-1))]
letter = word[randint(0,(len(word)-1))]
print(word.replace(letter,'?'))
effort = input('Введите букву: \n')
if effort == letter:
    print('Победа!')
else:
    print('Увы!Попробуёте в другой раз. \nСлово:', word)
