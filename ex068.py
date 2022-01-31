# even or odd
from random import randint
r = s = n = c = 0
let = even = odd = ''
while True:
    n = int(input('Choose a number: '))
    let = str(input('What is your choice? [E/O]: ').upper())
    r = int(randint(1, 10))
    s = r + n

    if (n + r) % 2 == 0 and let == 'E':
        c += 1
        print(f' You won!! Computer choose {r}. Sum is {s} and it is Even.')
    elif (n + r) % 2 != 0 and let == 'O':
        c += 1
        print(f'You won!! PC choose {r}. Sum is {s} and it is Odd.')
    else:
        break

print(f'You loose. You choose [{let}] and sum is {s}. You won {c} times')