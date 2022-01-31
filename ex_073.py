# Tuplas

teams = ('Benfica', 'Porto', 'Sporting', 'Boavista', 'Santa Clara', 'Braga', 'Portimonense', 'Guimarães', 'Belenenses', 'Uniao da Madeira', 'Canelas', 'Feirense', 'Nacional', 'Vizela', 'Paços de Ferreira', 'Arouca', 'Famalicão', 'Moreirense', 'Estoril', 'Tondela')

for p in teams[0:5]:
    print(p)

for u in teams[-5:]:
    print(u)

print(sorted(teams))

#Em que posição está o Boavista
print(teams.index('Boavista')+1) 