# listas - Pares e ímpares
lista = [[], []]
valor = 0
for c in range(0, 6):
    valor = int(input('Digite um número: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    elif valor % 2 != 0:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print(f'Os números pares são : {lista[0]}')
print(f'Os números ímpares são: {lista[1]}')
