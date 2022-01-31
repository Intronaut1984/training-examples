from time import sleep

print('Lets do an arithmetic progression')

for d in range(1, 3):
    sleep(0.5)
    print(' ', end=' ')
print(''' 
''')

t = int(input('First Term: '))
r = int(input('Reason: '))
dec = t + 10 * r

for d in range(1, 4):
    sleep(0.5)
    print('.', end=' ')
print(''' 
''')

while t < dec:
    t = t + r
    print(t, end='')
    print(' --> 'if t < dec else (''), end='')

n = int(input('''
How many more terms would you like to see? '''))

n = n + 10
dec = t + n * r

while t < dec:
    print('End' if n == 0 else '', end='')
    t = t + r
    print(t, end='')
    print(' --> 'if t < dec else (''), end='')
    print('End' if t == '0' else '', end='')
