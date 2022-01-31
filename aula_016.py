lanche = ('sumo', 'hamburquer', 'Lasanha', 'sandes', 'arroz')
jantar = ('Vinho', 'Lasanha')
calorias = lanche + jantar

print(calorias.index('Lasanha', 3)) #conta a partir da posição 3, pois já encontramos a primeira posiçãp
print(calorias.index('Lasanha', 0)) #conta a partir da posição 0
print(calorias.count('Lasanha')) # quantas vezes aparece lasanha
print(f'Comi {sorted(lanche)}') #ordem alfabética
print(f'Comi {lanche[0:]}')
print(f'Comi {lanche[1:3]}')

for c in range(0, len(lanche)):
    print(f'Comi {lanche[c]} e sua posição é: {c}')

for p, c in enumerate(lanche):
    print(f'Comi {c} e sua posição é {p}')

