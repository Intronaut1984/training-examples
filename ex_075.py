# Mais tuplas
count = 0
num = (int(input('Choose a number: ')),
       int(input('Choose a number: ')),
       int(input('Choose a number: ')),
       int(input('Choose a number: ')),
       int(input('Choose a number: ')))

print(f'Number 9 appeared {num.count(9)} times')

if num == 3:
       print(f'Number 3 was found on position {num.index(3) + 1}')
else:
       print('Não existe nº 3')

for n in num:
       if n % 2 == 0:
              print(f'Even number {n}')


