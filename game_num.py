from random import randint
print('Guess a number. U have tree efforts. Good luck')
x = randint(1,10)
k = 3
while True:
    effort = int(input('your number?(1-10)'))
    if effort == x:
        print('won')
        break
    else:
        k -= 1
       
    if k == 0:
        print('Game over')
        break
    elif effort > x:   
        print('try number smaller')
    else:
        print('try number bigger')
