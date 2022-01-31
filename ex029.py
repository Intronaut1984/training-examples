from random import randint

cont=int(120)
vel= randint(0,250)
vmax= int(120)
val= (vel - cont)*7

print('You are driving at {} km/h'.format(vel))

if vel >= 120:
    print('TRAFFIC TICKET!! {}$'.format(val))
else:
    print('You are driving safe!')

