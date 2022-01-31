from time import sleep

print('We will do an AP')
for d in range(1,3):
    sleep(0.5)
    print('.', end = ' ')
print(''' 
''')

t = int(input('First Term: '))
r = int(input('Reason: '))
eq = t + r
dec = t + (10) * r

while t < dec:

    t = t + r
    print(t, end = '')
    print(' --> 'if t < dec else print(' '), end='')