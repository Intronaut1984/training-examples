# Soma
print('If you choose 999 the program will finish')
n = int(input('Choose a number: '))

c = 0
s = 0


if n < 999:
    while c < n:
        c = c + 1
        print(c, end='')
        print(' --> ' if c < n else '', end='')
        s = s + c

else:
    print('END', end='')

print('''
The sum is: ''', s, 'and the total numbers is: ', c, end='')
