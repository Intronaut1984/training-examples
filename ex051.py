# Progressão Aritmética
from time import sleep
print('We will do an AP')
for d in range(1,4):
    sleep(0.5)
    print('.', end = ' ')
print(''' 
''')

t = int(input('First Term: '))
r = int(input('Reason: '))
eq = t + r
dec = t + (10-1) * r
for c in range(t, dec+r, r):
    print('{}'.format(c), end = ' --> ')
print('End')