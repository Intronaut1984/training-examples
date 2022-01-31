# Several Numbers


flag = str('N')
flag2 = 'S'
s = ''
count = 0
sum = 0
maior = menor = 0
while s != flag:
    n = int(input('Escreve um número: '))
    s = str(input('Quer escrever outro número? [S/N]').upper())
    count += 1
    sum += n
    if count == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

print('A média é de {} e digitou {} números. O maior número é {} e o menor é {}'.format(sum/count, count, maior, menor))

