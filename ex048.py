p = int(input('Choose first number: '))
s = int(input('Choose 2nd number: '))
# entre 1 e 500
t = int(s - p)
plus = 0
cont = 0
for t in range(p, s):
    if t % 2 == 1 and t % 3 == 0:
        plus += t
        cont = cont + 1
print('''O resultado da soma dos números ímpares, múltiplos de 3,
entre 1 e 500 é {} e tem {} números'''.format(plus, cont))