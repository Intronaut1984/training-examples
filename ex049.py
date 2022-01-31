# Multiplicador
from time import sleep

m = int(input('Choose a number: '))
# space
for n in range(1, 11):
    print(m, '*', n, '=', m * n)
    sleep(1)
