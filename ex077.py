# Tuplas - Reconhecer elementos

vogais = 'aeiou'
palavras = ('Sorrisos', 'Sustentabilidade', 'Amor', 'Paz', 'Carinho', 'Comida', 'Convivio')

for p in palavras:
    print(f'\nEu gosto de {p} - ', end='')
    for letra in p:
        if letra in vogais:
            print(letra, end=' ')
