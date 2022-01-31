# Weight

lighter = 0
heaviest = 0

for p in range(1, 4):
    weight = int(input('How much do you weight? '))
    if p == 1:
        lighter = weight
        heaviest = weight
    else:
        if weight > heaviest:
            heaviest = weight
        if weight < lighter:
            lighter = weight

print('The heaviest person weights {} kg and the lightest one has {} kg'.format(heaviest, lighter))

# lista = []
# for c in range(1, 6):
#     peso = float(input(f'Informe o Peso da {c}° pessoa: Kg '))
#     lista.append(peso)
#     ordem = sorted(lista)
# print(f'O Menor Peso é: {ordem[0]}Kg \nO Maior Peso é: {ordem[4]}Kg')

# pesos = [float(input('Informe o peso da pessoa {}: '.format(c+1))) for c in range(5)]
#
# print('Maior peso: {}'.format(max(pesos)))
# print('Menor peso: {}'.format(min(pesos)))
#
# exit()