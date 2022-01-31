from random import randint
num=int(input('Choose a number between 1 and 5 and try to win the $5k prize!'))

n = randint(1,5)

if num == n:
    print('Congratulations!! You wone $5k')
else:
    print('The choosen number was {} Try again'.format(n))
print('--END--')