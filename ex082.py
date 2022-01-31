#listas dividindo valores em várias listas

lista = []
pares = []
impares = []

while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    elif num % 2 != 0:
        impares.append(num)
    resp = input(str('Pretende continuar? [S/N]')).upper()
    if resp in 'Nn':
        break
    elif resp not in 'SsNn':
        print('Número inválido!')
print(f'A lista total: {lista}')
print(f'A lista de números pares: {pares}')
print(f'A lista de números impares: {impares}')



