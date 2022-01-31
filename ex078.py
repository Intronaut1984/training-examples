# Listas
'''lista = []     #ou list()

for v in range(0, 5):
    n = int(input('Escolha um número para a posição {} '.format(v)))
    lista.append(n)
numesc = 0
print(f'Os números escolhidos foram:')
for i in lista:
    ord = print(i, end=' ')

maior = max(lista)
menor = min(lista)
print(f'\nO maior nº é: {maior} e está na posição {lista.index(maior)}')

print(f'\nO menor número é: {menor} e está na posição {lista.index(menor)} ')'''

lista = []
maior = 0
menor = 0

for num in range(0, 5):
    lista.append(int(input(f'Escolha um número para a posição {num}: ')))
    if num == 0:
        maior = menor = lista[num]
    else:
        if lista[num] > maior:
            maior = lista[num]
        if lista[num] < menor:
            menor = lista[num]
print(f'voce digitou os seguintes números: {lista}')
print(f'o menor valor é: {menor}')
print(f'o maior valor é: {maior}')

print('o maior número está nas posições: ')
for p, n in enumerate(lista):
    if n == maior:
        print(f'{p}...', end='')
print()
print('o menor número está nas posições: ')
for p, n in enumerate(lista):
    if n == menor:
        print(f'{p}...', end='')










