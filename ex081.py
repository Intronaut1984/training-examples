# listas extraindo dados

lista = list()

while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Pretende continuar? [S/N]').upper())
    if resp in 'Ss':
        print('Mais um número...')
    elif resp not in 'SsNn':
        print('Inválido')
    if resp in 'Nn':
        break

lista.sort(reverse=True)
print(f'Os números por ordem são: {lista} ')
if 5 in lista:
    print(f'O número 5 está na lista!')
else:
    print('O número 5 n está na lista.')

print(f'Foram digitados {len(lista)} números!')



