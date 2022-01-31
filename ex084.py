# Listas - Análise de dados (contém alguns erros de resultado. Por exemplo, se colocar pesos iguais)
lista = []
dados = []
maior = menor = 0
nomemenor = ''
nomemaior = ''
while True:
    dados.append(str(input('Qual o seu nome?')))
    dados.append(int(input('Qual o seu peso?')))
    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
            nomemaior = dados[0]
        if dados[1] < menor:
            menor = dados[1]
            nomemenor = dados[0]
    lista.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N]')).upper()
    if resp in 'Nn':
        break
print(f'Número de pessoas: {len(lista)}')
print(f'A pessoa mais leve é {nomemenor} com {menor}kg e a mais pesada é {nomemaior} com {maior}kg')
