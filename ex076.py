# Tuplas organizadas

list = ('Caneta', 0.75, 'Lápis', 0.90, 'Caderno', 1.50, 'Porta Lápis', 3.50, 'Mochila', 50, 'Calculadora', 80)
print('-' * 37)
print(f'{"LISTAGEM DE PREÇOS":^37}')
print('-' * 37)

for pos in range(0, len(list)):
    if pos % 2 == 0:
        print(f'{list[pos]:.<30}', end= '')
    else:
        print(f'  €{list[pos]:>1.2f}')
