# Palíndromo
# AME O POEMA
aop = str(input('Escreva um Palíndromo: '))
sop = aop.replace(' ', '').upper()
iop = sop[::-1]
cop = iop.upper()

if sop == iop:
    print(sop, 'é o inverso de:', aop.upper(), 'e é um Palíndromo')
else:
    print(iop, 'é o inverso de:', aop.upper(), 'e não é um Palíndromo')

