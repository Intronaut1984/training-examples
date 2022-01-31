# lista - adicionar valores
lista = []


while True:
    num = (int(input('Adicione um número: ')))
    if num in lista:
        lista.pop()
        print(f'Número repetido, não vou adicionar')
    lista.append(num)

    resp = input('Pretende continuar? ').upper()
    if resp == 'S':
        print('programa continua...')
    if resp == 'N':
        break
lista.sort()
print(f'Os números adicionados foram: {lista}')






